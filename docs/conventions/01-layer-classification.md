# Layer Classification Convention

## Foundation

다음 특성이 강하면 Foundation으로 분류합니다.

- 전역 또는 환경 기반 자원이다.
- 여러 상위 영역이 공통으로 사용한다.
- 변경 빈도가 낮다.
- 특정 서비스 lifecycle에 종속되지 않는다.

예:

- VPC
- Subnet
- Hosted Zone
- shared KMS key

## Platform

다음 특성이 강하면 Platform으로 분류합니다.

- 여러 서비스가 공통으로 소비한다.
- shared capability를 제공한다.
- provider로서 stable Contract를 게시한다.
- 서비스별 runtime과 분리된 shared lifecycle을 가진다.

## Service

다음 특성이 강하면 Service로 분류합니다.

- 특정 서비스와 함께 배포된다.
- 특정 서비스 장애/롤백 단위에 속한다.
- 특정 서비스만을 위한 설정 또는 엔드포인트다.
