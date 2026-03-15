---
title: 네트워크와 IAM 규약
doc_section: conventions
nav_parent: conventions-index
nav_order: 6
---

# 네트워크와 IAM 규약

## 보안 그룹

- ingress rule은 받는 쪽 owner가 관리한다.
- shared producer SG는 Platform이 소유한다.
- 서비스 식별은 가능하면 고정 Client SG로 표현한다.

권장 예:

- `orders-client-sg`
- `billing-client-sg`

## IAM

- workload role은 원칙적으로 해당 workload와 함께 선언한다.
- shared platform component role만 Platform ownership을 가질 수 있다.
- 서비스별 role 목록을 Platform이 일반 리소스 관리 목적으로 직접 관리하지 않는다.

