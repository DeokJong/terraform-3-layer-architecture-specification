---
title: 마이그레이션과 롤아웃 시나리오
doc_section: architecture
nav_parent: architecture-index
nav_order: 14
---

# 마이그레이션과 롤아웃 시나리오

## 계약 마이그레이션

1. 현재 Active 계약를 식별합니다.
2. 새 계약를 정의하고 병행 게시합니다.
3. 소비자와 마이그레이션 순서를 식별합니다.
4. 마이그레이션 동안 두 계약을 함께 운영합니다.
5. 마이그레이션 이후 기존 계약을 Deprecated로 전환합니다.
6. 안정화 이후에만 제거합니다.

## 공유 리소스 접근 확장

상황:

- 새 서비스가 shared DB 또는 shared bucket에 접근해야 합니다.

권장 순서:

1. Client SG 또는 principal 같은 새 소비자 식별자를 만듭니다.
2. access workspace만 수정합니다.
3. core workspace는 그대로 둡니다.
4. 게시된 계약을 통해 서비스를 연결합니다.

## 공유 리소스 교체

상황:

- DB engine 교체, cluster 교체, 또는 bucket 재설계가 필요합니다.

권장 순서:

1. 소비자가 implementation value를 직접 읽지 않는지 확인합니다.
2. 새 core resource를 준비합니다.
3. 기존 계약가 새 core를 계속 대표할 수 있는지 확인합니다.
4. 가능하면 contract meaning을 유지한 채 게시만 전환합니다.
5. 불가능하면 새 계약를 병행 게시하고 소비자를 마이그레이션합니다.

## 서비스 롤아웃 실패

상황:

- 서비스 runtime 배포가 실패하거나 새 contract consumer rollout이 실패합니다.

권장 순서:

1. 서비스 workspace만 롤백합니다.
2. shared core와 기존 계약은 그대로 유지합니다.
3. 문제가 access 관련이면 access workspace만 되돌립니다.

## 레거시 전환

상황:

- 기존 이름과 경로는 유지해야 하지만 ownership 해석은 새 모델로 옮겨야 합니다.

권장 순서:

1. 현재 값을 legacy contract 또는 implementation으로 식별합니다.
2. 새 규칙 아래에서 provider ownership을 다시 해석합니다.
3. 새 소비자는 새 contract 모델로 연결합니다.
4. 기존 소비자는 점진적으로 마이그레이션합니다.


