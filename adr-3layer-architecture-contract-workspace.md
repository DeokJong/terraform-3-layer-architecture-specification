# ADR: 3-Layer Architecture and Contract / Workspace Model

## 제목

3-Layer Architecture에서 Layer, Contract, Workspace의 역할과 ownership 규칙 정의

## 상태

Proposed

## 배경

현재 인프라는 여러 서비스와 공유 리소스가 혼재된 상태로 운영되고 있으며, 레이어 간 참조, 공유 리소스 ownership, SSM/Route53/Secret의 소유 주체, Terraform Workspace 분리 기준이 일관되게 정의되어 있지 않습니다.

이로 인해 다음 문제가 반복될 수 있습니다.

- 상위 레이어 변경이 과도하게 하위 레이어 변경을 유발함
- 공유 리소스와 서비스 전용 리소스 경계가 불명확함
- SSM, Route53 Record, Secret 등 Contract 전달 매체의 ownership이 혼동됨
- Terraform Workspace가 과도하게 비대해지거나, core / access / publication이 뒤섞여 blast radius가 커짐
- Service 간 직접 참조가 누적되어 강결합이 발생함

기존 운영 중인 자산이 존재하므로, 본 결정은 현재 자산을 즉시 전면 개편하기보다 향후 설계와 점진적 정렬을 위한 기준을 제공하는 것을 목표로 합니다.

또한 이 ADR은 HashiCorp가 게시한 자료인 [Happy Terraforming! Real-world experience and proven best practices](https://www.hashicorp.com/en/resources/terraforming-real-world-experience-best-practices)를 중요한 참고 자료로 삼았습니다. 해당 자료는 대규모 조직에서 Terraform 코드를 `bootstrap`, `foundation`, `services` 레이어로 나누어 워크플로우, 책임 분리, lifecycle 차이, monolith 방지를 다루고 있습니다.

본 ADR은 그 문제의식과 layering 접근에서 영향을 받았지만, 이 저장소에서는 이를 그대로 복제하지 않고 다음과 같이 재해석했습니다.

- `bootstrap / foundation / services` 개념을 현재 문맥에 맞게 `Foundation / Platform / Service` 모델로 재구성
- 단순 폴더 분리보다 `ownership`, `Contract`, `Workspace`, `blast radius` 기준을 더 강하게 명시
- shared resource 운영을 위해 `Core / Access / Publication` 분리 모델을 추가
- 기존 운영 자산을 즉시 재구성하지 않고 `legacy 허용 + 점진 migration` 원칙으로 완화

## 결정

### 1. Layer는 ownership과 dependency direction을 정의한다

인프라는 다음 3개의 Layer로 구분한다.

- Foundation: 네트워크 및 전역 공통 기반 리소스
- Platform: 여러 서비스가 공통으로 의존하는 공유 런타임 / 공유 데이터 / 공용 인터페이스
- Service: 개별 서비스와 lifecycle을 같이하는 리소스

참조 방향은 `Foundation → Platform → Service` 순으로만 허용한다. 의미상으로는 하위 레이어가 상위 레이어를 참조하는 구조를 따른다.

### 2. Workspace는 Layer와 별개의 운영 단위다

Workspace는 Terraform state, apply, 권한, blast radius를 제어하기 위한 운영 단위다. Layer와 Workspace는 동일 개념이 아니며, 1:1 대응을 강제하지 않는다.

같은 Layer 안에서도 다음 특성에 따라 여러 Workspace로 분리할 수 있다.

- 변경 빈도
- blast radius
- apply 주체
- downstream dependency
- rollback 위험
- core / access / publication의 성격 차이

### 3. 모든 레이어 간 전달값은 Contract로 간주한다

하위 레이어는 상위 레이어의 내부 구현값을 직접 참조하지 않고, 상위 레이어가 게시한 Contract만 참조해야 한다.

Contract에는 다음이 포함된다.

- Terraform Output
- SSM Parameter
- Route53 Record
- Secret reference
- IAM principal reference
- Security Group client identity
- bucket name, key ARN, cluster name 등 표준 식별자

### 4. Contract ownership은 provider가 가진다

Contract ownership은 다음으로 결정하지 않는다.

- 누가 읽는지
- 어디에 저장되는지
- 어떤 도구로 전달되는지

Contract ownership은 그 Contract가 대표하는 리소스/인터페이스를 누가 제공하고, 그 의미와 안정성을 누가 보장하는지로 결정한다. 즉, consumer가 아니라 provider가 owner다.

### 5. Implementation Value와 Contract Value를 구분한다

하위 레이어는 상위 레이어의 Implementation Value를 직접 참조하지 않는다.

- Implementation Value: 내부 구현 세부사항
- Contract Value: 하위 레이어가 의존해도 되는 안정된 값

상위 레이어는 가능하면 stable DNS, standard output, standard parameter path 등 Contract Value를 게시해야 한다.

### 6. Shared resource는 Core / Access / Publication으로 분리 가능해야 한다

공유 리소스는 필요 시 아래 단위로 분리한다.

- Core: 본체 리소스
- Access: allowlist, attachment, grant, policy binding
- Publication: consumer-facing contract 게시

특히 access churn이 높은 경우, Core와 Access를 별도 Workspace로 분리하는 것을 권장한다.

### 7. 기존 자산은 legacy로 허용한다

현재 운영 중인 리소스의 naming, SSM path, DNS 구조는 즉시 강제 변경하지 않는다.

다만 다음 원칙은 적용한다.

- 기존 이름이 legacy여도 ownership은 새 기준으로 해석한다
- 신규 리소스와 신규 Contract는 본 기준을 우선 적용한다
- rename 대신 신규 Contract 병행 게시 후 점진 마이그레이션을 우선한다

## 결과

이 결정을 통해 다음을 기대한다.

- 레이어 간 의존 방향이 명확해진다
- 상위 레이어 안정성을 유지하면서 하위 서비스 독립성을 높일 수 있다
- SSM / Route53 / Secret ownership 혼선을 줄일 수 있다
- Terraform Workspace를 blast radius와 변경 특성에 맞게 분리할 수 있다
- Service 간 직접 참조를 줄이고 Contract 중심 구조로 전환할 수 있다

## 트레이드오프

### 장점

- ownership과 책임 경계가 분명해진다
- 변경 전파를 제어하기 쉬워진다
- 공용 리소스 운영과 서비스 독립 배포를 동시에 만족시키기 쉬워진다
- legacy 환경에서도 점진적으로 정렬할 수 있다

### 단점

- 초기에는 판단 규칙이 다소 복잡해 보일 수 있다
- access workspace, publication workspace 분리로 workspace 수가 증가할 수 있다
- provider / consumer 구분과 contract lifecycle 관리가 추가 운영 규칙을 요구한다

## 대안

### 대안 1. 모든 shared를 Platform에 최대한 몰아넣는다

단순해 보이지만 Platform 비대화, apply churn 증가, 서비스 독립성 저하 문제가 있다.

### 대안 2. Layer와 Workspace를 1:1로 강제한다

설명은 쉬우나 실제 운영에서는 core / access / publication 분리가 어려워 blast radius가 커진다.

### 대안 3. Contract ownership을 저장 위치 기준으로 정한다

SSM, Route53, Secret의 전달 매체와 ownership이 혼동되어 실무 해석이 흔들리기 쉽다.

## 적용 기준

새 리소스 또는 새 Contract 추가 시 다음 순서로 판단한다.

1. 이것은 누구 lifecycle과 함께 움직이는가
2. 이것은 Core / Access / Publication 중 무엇인가
3. 이것은 Implementation Value인가, Contract Value인가
4. Contract라면 provider는 누구인가
5. 변경 빈도와 blast radius가 달라 workspace 분리가 필요한가

## 예시와 안티패턴

### Example 1. DB + Route53 + SSM

상황:

- DB는 공유 RDS
- 애플리케이션은 DB 접속 주소를 SSM에서 읽음
- 실제 RDS endpoint를 직접 쓰지 않고 Route53 Record를 거쳐 사용

권장 구조:

- RDS: Platform
- `db-main.internal.example.com`: Platform
- SSM DB host parameter: Platform
- Service는 해당 parameter를 소비

이유:

DB 접속 주소는 backend 설정처럼 보일 수 있지만, 실제로는 Platform이 제공하는 connectivity contract이기 때문입니다.

안티패턴:

- backend service workspace가 DB host SSM parameter를 소유
- 앱이 실제 RDS endpoint를 직접 참조
- DB 교체 시 각 서비스 설정을 직접 수정해야 함

### Example 2. Hosted Zone owner와 Record owner 분리

상황:

- internal hosted zone은 Foundation이 관리
- DB DNS는 Platform이 만들고
- 서비스 API DNS는 Service가 만듦

권장 구조:

- Hosted Zone: Foundation
- `db-main.internal.example.com`: Platform
- `orders-api.internal.example.com`: Service

이유:

Hosted Zone은 기반 인프라고, 개별 Record는 각 인터페이스의 provider가 소유할 수 있습니다.

안티패턴:

- Hosted Zone이 Foundation에 있으므로 모든 Record도 Foundation이 직접 관리
- DNS 추가/변경이 전부 Foundation workspace에 몰림
- 서비스 배포마다 Foundation apply가 필요해짐

### Example 3. Shared Redis + Client SG 패턴

상황:

- 여러 서비스가 하나의 Redis를 사용
- 네트워크 허용 제어가 필요

권장 구조:

- Redis: Platform
- Redis SG: Platform
- 각 서비스는 고정 Client SG 보유
- Redis ingress allowlist는 Platform access workspace가 관리

이유:

Producer-side ingress ownership 원칙을 지키면서도, 서비스 식별을 CIDR 대신 의미 있는 SG 단위로 유지할 수 있습니다.

안티패턴:

- 각 서비스가 Redis SG rule을 직접 수정
- Redis SG ingress가 CIDR 기반으로만 열려 있음
- 플랫폼 core와 ingress allowlist가 하나의 workspace에 섞여 잦은 apply 유발

### Example 4. Shared S3 Bucket과 Bucket Policy 분리

상황:

- 공용 bucket은 여러 서비스가 사용
- 서비스별 접근 권한은 자주 바뀜

권장 구조:

- Bucket 본체: Platform core
- Bucket policy / principal binding: Platform access
- 필요 시 public contract는 publication workspace 또는 core output으로 게시

이유:

버킷은 안정적으로 유지하고, 서비스 온보딩/오프보딩에 따른 접근 정책만 따로 변경할 수 있어야 합니다.

안티패턴:

- Bucket 본체와 모든 consumer policy를 하나의 workspace에서 관리
- 서비스 하나 추가할 때마다 bucket core apply가 실행
- policy churn이 core stability를 침범

### Example 5. KMS Core와 Grants 분리

상황:

- 여러 서비스가 공용 KMS key를 사용
- grant / key policy 변경이 자주 발생

권장 구조:

- KMS key: Foundation 또는 Platform core
- grants / consumer binding: 별도 access workspace

이유:

Key 자체 lifecycle과 consumer allowlist lifecycle은 다릅니다.

안티패턴:

- 신규 서비스 온보딩 때마다 KMS core workspace 직접 변경
- key creation, rotation, grant 변경이 하나의 state에 뒤섞임

### Example 6. Service-owned API Endpoint

상황:

- Orders 서비스가 internal API를 제공
- 다른 서비스가 이 API를 호출할 수 있음

권장 구조:

- `orders-api.internal.example.com`: Orders Service contract
- 호출 서비스는 해당 stable hostname만 참조
- backing ALB, target group, internal implementation은 Orders service 내부

이유:

공용 인프라 위에 올라가 있더라도, 인터페이스 의미와 lifecycle이 Orders 서비스에 귀속되면 Service ownership입니다.

안티패턴:

- 호출하는 쪽이 Orders의 ALB physical DNS를 직접 사용
- 다른 서비스가 Orders workspace 내부 output에 직접 강하게 결합
- shared ingress 아래 있다는 이유로 endpoint ownership을 Platform으로 착각

### Example 7. Service-to-Service Dependency

상황:

- Service A가 Service B의 기능을 사용해야 함

권장 구조:

- Service B가 stable API contract를 게시
- Service A는 그 contract만 사용
- 필요한 auth / allowlist는 access dependency로 분리 관리

이유:

Service 간 직접 구현 참조를 막고, provider/consumer 관계를 명확히 하기 위해서입니다.

안티패턴:

- Service A가 Service B의 secret path를 직접 참조
- Service A가 Service B의 queue, bucket path, internal DNS를 임의 사용
- Service A가 B의 runtime implementation에 직접 결합

### Example 8. Contract Aggregation Workspace

상황:

- 여러 platform output이나 endpoint를 한 번에 조회하기 쉽게 모아두고 싶음

권장 구조:

- aggregation은 publication / convenience 목적까지만 허용
- source of truth는 원 producer에 유지
- ownership은 aggregation workspace로 이동하지 않음

이유:

조회 편의와 ownership을 분리해야 원래 provider 책임이 흐려지지 않습니다.

안티패턴:

- aggregation workspace가 사실상 source of truth가 됨
- 원 producer 변경 없이 aggregation 쪽 값만 따로 수정
- consumer가 실제 provider 대신 aggregation에만 의존

### Example 9. Platform은 Service를 몰라야 한다 vs access control 필요

상황:

- DB는 Platform이 운영
- 어떤 서비스에 접근을 열어줄지는 알아야 함

권장 구조:

- Platform은 서비스의 일반 리소스 상태를 직접 관리하지 않음
- 다만 access control을 위한 최소 식별자(Client SG, Role ARN)는 예외적으로 참조 가능
- 이 결합은 access workspace에 격리

이유:

원칙을 지키면서도 현실적인 onboarding을 가능하게 합니다.

안티패턴:

- Platform core workspace가 모든 서비스 목록을 지속적으로 들고 있음
- 서비스 하나 추가할 때마다 cluster / DB / ingress core 전체가 흔들림

### Example 10. Legacy naming이 존재하는 경우

상황:

- 이미 운영 중이라 SSM path, DNS name, workspace name이 뒤섞여 있음

권장 구조:

- 이름은 당장 바꾸지 않음
- ownership, contract type, workspace role만 새 기준으로 분류
- 신규 contract부터 표준화
- 기존 contract 교체가 필요하면 병행 게시 후 점진 migration

이유:

현재 운영을 깨지 않으면서도 앞으로의 판단 기준을 통일할 수 있습니다.

안티패턴:

- naming이 엉켜 있으니 원칙 적용을 포기
- 반대로 모든 naming을 한 번에 바꾸려다 대규모 breaking change 유발

## 문서에 같이 넣으면 좋은 Anti-pattern Rules

- Service가 Platform의 implementation value를 직접 참조하는 것
- Platform이 서비스 목록을 일반 리소스 관리 목적으로 직접 열거하는 것
- Shared resource의 core와 access rule을 같은 workspace에 무분별하게 섞는 것
- Active Contract를 in-place rename 하거나 의미를 조용히 바꾸는 것
- SSM, Route53, Secret의 저장 위치만 보고 ownership을 판단하는 것
- 여러 서비스가 쓴다는 이유만으로 무조건 Platform ownership으로 승격하는 것
- Service 간 직접 구현 참조를 허용하는 것
