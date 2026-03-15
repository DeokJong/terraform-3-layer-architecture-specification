---
title: 문서 시스템
description: 문서 registry, work index, agent guidance를 포함해 저장소의 문서 유지보수 체계를 관리하는 메타 섹션입니다.
hero_kicker: Section Overview
doc_section: meta
nav_key: meta-index
nav_title: 개요
nav_order: 1
---

# Documentation System

이 섹션은 저장소의 문서 시스템 자체를 유지보수하기 위한 메타 문서입니다.

## 핵심 파일

- [Document Registry](./document-registry.json)
- [Work Index](./work-index.md)
- [Agent Instructions Source](./agent-instructions.md)

## 역할

- 어떤 문서가 canonical source인지 추적합니다.
- 현재 어떤 문서가 어떤 상태인지, 보강이 필요한지 표시합니다.
- 다음에 어떤 문서를 강화해야 하는지 작업 순서를 보여줍니다.
- Codex가 문서를 강화할 때 어디를 읽고 어디를 수정해야 하는지 기준을 제공합니다.

## 유지보수 원칙

1. 문서 구조와 상태를 바꾸려면 먼저 `document-registry.json`을 갱신합니다.
2. 그 다음 `work-index.md`를 다시 생성합니다.
3. agent guidance가 바뀌면 `docs/meta/agent-instructions.md`를 수정하고 mirror 파일을 함께 재생성합니다.
4. 마지막으로 실제 문서 본문과 portal navigation을 맞춥니다.
