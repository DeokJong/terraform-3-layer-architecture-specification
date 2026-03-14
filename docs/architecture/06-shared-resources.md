# Shared Resources

## 분리 모델

shared resource는 필요 시 아래처럼 나눌 수 있습니다.

| 영역 | 설명 | 예시 |
| --- | --- | --- |
| Core | 본체 리소스 | DB, bucket, cluster |
| Access | 허용 정책과 binding | SG rule, bucket policy, KMS grant |
| Publication | consumer-facing contract 게시 | DNS, SSM parameter, output |

이 구조는 권장 예시이지 유일한 정답은 아닙니다. 하나의 shared resource를 소수 consumer가 사용하고 access 변경이 드문 경우에는 core, access, publication을 하나의 Workspace에 둘 수 있습니다.

## 일반형 명명 예시

- core resource는 `*-core`
- access rule은 `*-access`
- publication contract는 `*-contract`

## DB 예시

- shared DB 본체는 `platform-db-core`
- DB ingress allowlist는 `platform-db-access`
- DB stable host publication은 `platform-db-contract`

## owner의 책임

shared resource owner는 다음을 책임집니다.

- core lifecycle 관리
- consumer에게 제공할 contract 정의
- access control 정책의 승인 모델 정의
- migration과 compatibility 정책 제공

consumer는 shared resource를 직접 변경하는 대신 access contract와 publication contract를 통해 연결되어야 합니다.

## shared resource 예시 매핑

| 리소스 종류 | Core | Access | Publication |
| --- | --- | --- | --- |
| DB | cluster / instance | SG allowlist, auth binding | DNS, SSM host, output |
| S3 | bucket | bucket policy, principal binding | bucket name, published outputs |
| Redis | cluster | ingress allowlist | stable endpoint |
| KMS | key | grants, key policy binding | key ARN, alias |
| Ingress | ALB / NLB / gateway | listener rule binding, allowlist | stable hostname |

## 다음 문서

- [Service Dependencies](./07-service-dependencies.md)
