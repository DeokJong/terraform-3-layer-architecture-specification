# Shared Resource Convention

## 분리 규칙

가능하면 다음 3개로 분리 검토합니다.

- Core: 본체 리소스
- Access: allowlist, attachment, grant, policy binding
- Publication: consumer-facing contract

## 대표 적용 예

shared DB:

- DB instance / cluster: `platform-db-core`
- SG allowlist: `platform-db-access`
- stable endpoint publication: `platform-db-contract`

shared S3:

- bucket: `platform-storage-core`
- bucket policy binding: `platform-storage-access`
- public or consumer-facing outputs: `platform-storage-contract`

shared Redis:

- cluster: `platform-cache-core`
- ingress allowlist: `platform-cache-access`
- endpoint publication: `platform-cache-contract`
