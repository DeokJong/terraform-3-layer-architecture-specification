# ADR: 3-Layer Architecture and Contract / Workspace Model

## 제목

3-Layer Architecture에서 Layer, Contract, Workspace, Resource Set 규칙 정의

## 상태

Accepted

## 배경

현재 인프라는 여러 서비스와 공유 리소스가 혼재된 상태로 운영되고 있으며, 레이어 간 참조, 공유 리소스 ownership, SSM/Route53/Secret 같은 publication surface의 책임, Terraform Workspace 분리 기준이 일관되게 정리되어 있지 않습니다.

또한 일부 환경은 모놀로식 Terraform Workspace에 과도하게 많은 리소스가 집약되어 있습니다. 이 구조에서는 한 환경에 대한 변경 PR이 올라와 Terraform lock이 잡히면 다른 PR은 같은 환경에 대해 Plan조차 수행하지 못합니다. 그 결과 변경 검증이 직렬화되고, 리뷰와 배포 대기 시간이 길어집니다.

특히 SSM Parameter처럼 개수가 매우 많은 리소스는 Plan 자체만으로도 수 분이 소요됩니다. 실제 운영에서는 특정 환경의 Plan만 약 5분 정도 걸리는 경우가 있으며, lock 대기와 결합되면 작은 변경도 빠르게 검증하기 어렵습니다.

반면 Lambda 계열은 이미 Serverless Framework Stack으로 분리 관리되고 있어, Terraform이 관리하는 주제와 별도 배포 단위가 혼재되어 있습니다. 즉 현재 상태는 "모든 것을 한 Workspace에 둔 단순한 구조"도 아니고, 그렇다고 ownership과 운영 경계를 기준으로 정리된 구조도 아닙니다.

이로 인해 다음 문제가 반복됩니다.

- 상위 레이어 변경이 과도하게 하위 레이어 변경으로 전파된다.
- 공유 리소스와 서비스 전용 리소스의 경계가 불명확하다.
- SSM, Route53 Record, Secret 같은 publication 매체와 ownership이 혼동된다.
- Terraform Workspace가 지나치게 비대해지거나, 반대로 변경 경계 없이 쪼개져 blast radius가 커진다.
- Service 간 직접 참조가 누적되어 강결합이 발생한다.
- lock 경합 때문에 같은 환경의 변경 검증이 병렬화되지 못한다.
- 리소스 수가 많은 workspace는 Plan 비용 자체가 커져 작은 변경도 느리게 검증된다.
- Terraform과 SLS Stack의 관리 경계가 문서로 정리되지 않아 ownership과 운영 주제가 혼동된다.

이 ADR의 목표는 기존 자산을 즉시 전면 재구성하는 것이 아니라, legacy를 허용하면서도 이후 설계와 migration을 일관되게 판단할 기준을 제공하는 것입니다.

이 ADR은 구조를 다시 파악하는 과정에서 HashiCorp의 [Happy Terraforming! Real-world experience and proven best practices](https://www.hashicorp.com/en/resources/terraforming-real-world-experience-best-practices)를 중요한 참고 자료로 삼았습니다. 다만 이 저장소는 해당 내용을 그대로 복제하지 않고, 현재 운영 문제와 legacy 조건에 맞게 `Foundation / Platform / Service`, `Contract`, `Workspace`, `Resource Set` 개념으로 재구성해 문서화합니다.

## 결정

### 1. Layer의 ownership과 dependency direction을 정의한다

인프라는 다음 3개 Layer로 구분한다.

- Foundation: 네트워크 및 전역 공통 기반 리소스
- Platform: 여러 서비스가 공통으로 의존하는 공유 런타임 / 공유 데이터 / 공용 인터페이스
- Service: 개별 서비스와 lifecycle을 같이하는 리소스

참조 방향은 `Foundation -> Platform -> Service` 순서로만 허용한다. 의미상으로는 하위 레이어가 상위 레이어가 게시한 Contract를 소비하는 구조를 따른다.

### 2. Workspace는 Layer와 별개의 운영 단위다

Workspace는 Terraform state, apply, 권한, blast radius를 제어하기 위한 운영 단위다. Layer와 Workspace는 동일 개념이 아니며 1:1 대응을 강제하지 않는다.

같은 Layer 안에서도 다음 특성에 따라 여러 Workspace로 분리할 수 있다.

- 변경 빈도
- blast radius
- apply 주체
- downstream dependency
- rollback 위험
- publication migration 필요성

### 3. 모든 레이어 전달값은 Contract로 간주한다

하위 레이어는 상위 레이어의 implementation value를 직접 참조하지 않고, 상위 레이어가 게시한 Contract만 사용한다.

Contract에는 다음이 포함된다.

- Terraform Output
- SSM Parameter
- Route53 Record
- Secret reference
- IAM principal reference
- Security Group client identity
- bucket name, key ARN, cluster name 같은 경계값

### 4. Contract ownership은 provider에게 있다

Contract ownership은 누가 읽는지, 어디에 저장되는지, 어떤 매체로 전달되는지로 결정하지 않는다.

Contract ownership은 그 Contract가 표현하는 리소스 또는 인터페이스를 누가 제공하고, 그 의미와 안정성을 누가 보장하는지로 결정한다. 즉 consumer가 아니라 provider가 owner다.

### 5. Implementation Value와 Contract Value를 구분한다

하위 레이어는 상위 레이어의 Implementation Value를 직접 참조하지 않는다.

- Implementation Value: 내부 구현 세부사항
- Contract Value: consumer가 소비해도 되는 안정된 값

provider는 가능한 한 stable DNS, standard output, standard parameter path 같은 Contract Value를 게시해야 한다.

### 6. Shared Resource는 Resource Set으로 우선 설명한다

shared resource는 우선 하나의 shared capability를 제공하는 Resource Set으로 정의한다.

예:

- `user-db`
- `book-db`
- `finance-db`
- `shared-cache`

Resource Set 내부 구성요소는 blast radius, 변경 빈도, ownership, rollback 경계에 따라 선택적으로 분리할 수 있다.

대표적인 내부 분리 패턴은 다음과 같다.

- Primary Resource: 본체 리소스
- Binding: allowlist, attachment, grant, policy binding
- Publication: consumer-facing contract 게시

이 패턴은 자주 쓰이는 내부 구조일 뿐, 모든 shared resource에 고정 3분할을 강제하지 않는다.

### 7. Legacy 자산은 허용하되 새 기준으로 해석한다

현재 운영 중인 리소스의 naming, SSM path, DNS 구조를 즉시 강제 변경하지 않는다.

다만 다음 원칙을 적용한다.

- 기존 이름이 legacy여도 ownership은 새 기준으로 해석한다.
- 신규 리소스와 신규 Contract는 새 기준을 우선 적용한다.
- rename보다 병행 게시와 점진 migration을 우선한다.

## 결과

이 결정으로 다음을 기대한다.

- 레이어 간 참조 방향이 명확해진다.
- shared capability와 서비스 독립성이 함께 유지된다.
- SSM / Route53 / Secret ownership 혼선이 줄어든다.
- Workspace를 blast radius와 운영 경계에 맞게 분리할 수 있다.
- Service 간 직접 참조를 줄이고 Contract 중심 구조로 전환할 수 있다.

## 트레이드오프

### 장점

- ownership과 책임 경계가 분명해진다.
- 변경 전파를 제어하기 쉬워진다.
- 공유 리소스 운영과 서비스 독립 배포를 동시에 만족시키기 쉬워진다.
- legacy 환경에서도 점진적으로 정렬할 수 있다.

### 단점

- 초기에는 판단 규칙이 다소 복잡해 보일 수 있다.
- binding workspace, publication workspace 분리로 workspace 수가 증가할 수 있다.
- provider / consumer 구분과 contract lifecycle 관리에 추가 운영 규칙이 필요하다.

## 대안

### 대안 1. 모든 shared를 Platform에 최대한 몰아넣는다

단순해 보이지만 Platform 비대화, apply churn 증가, 서비스 독립성 저하 문제가 있다.

### 대안 2. Layer와 Workspace를 1:1로 강제한다

설명은 쉬우나 실제 운영에서는 변경 특성이 다른 구성요소를 분리하기 어려워 blast radius가 커진다.

### 대안 3. Contract ownership을 저장 위치 기준으로 정한다

SSM, Route53, Secret 같은 publication 매체와 ownership이 혼동되어 잘못된 해석이 반복된다.

## 적용 기준

새 리소스 또는 Contract 추가 시 아래 순서로 판단한다.

1. 누구 lifecycle과 함께 움직이는가
2. 어떤 Layer에 속하는가
3. 어떤 Resource Set capability에 속하는가
4. Implementation Value인가, Contract Value인가
5. Contract라면 provider는 누구인가
6. 변경 빈도와 blast radius가 달라 Workspace 분리가 필요한가

## 예시와 안티패턴

### Example 1. DB + Route53 + SSM

상황:

- DB는 공유 RDS다.
- 애플리케이션은 DB 접속 주소를 SSM에서 읽는다.
- 실제 RDS endpoint를 직접 쓰지 않고 Route53 Record를 거쳐 사용한다.

권장 구조:

- RDS: Platform
- `db-main.internal.example.com`: Platform
- SSM DB host parameter: Platform
- Service는 해당 parameter를 소비한다.

이유:

DB 접속 주소는 backend 설정처럼 보일 수 있지만, 실제로는 Platform이 제공하는 connectivity contract이기 때문이다.

안티패턴:

- backend service workspace가 DB host SSM parameter를 소유한다.
- 서비스가 실제 RDS endpoint를 직접 참조한다.
- DB 교체 시 각 서비스 설정을 직접 수정해야 한다.

### Example 2. Hosted Zone owner와 Record owner 분리

상황:

- internal hosted zone은 Foundation이 관리한다.
- DB DNS는 Platform이 만든다.
- 서비스 API DNS는 Service가 만든다.

권장 구조:

- Hosted Zone: Foundation
- `db-main.internal.example.com`: Platform
- `orders-api.internal.example.com`: Service

이유:

Hosted Zone은 기반 인프라고, 개별 Record의 의미와 lifecycle은 해당 인터페이스 provider가 소유한다.

### Example 3. Shared Redis + Client SG 패턴

상황:

- 여러 서비스가 하나의 Redis를 사용한다.
- 네트워크 access 제어가 필요하다.

권장 구조:

- Redis: Platform
- Redis SG: Platform
- 각 서비스는 고정 Client SG를 가진다.
- Redis ingress allowlist는 Platform binding workspace가 관리한다.

이유:

producer-side ingress ownership을 유지하면서도, 서비스별 식별을 SG 단위로 명확하게 표현할 수 있다.
