---
title: 작업 인덱스
description: 문서 레지스트리에서 생성한 사람이 읽는 작업 상태 보드입니다.
hero_kicker: 문서 거버넌스
doc_section: meta
nav_parent: meta-index
nav_order: 3
---

# 작업 인덱스

이 파일은 `docs/meta/document-registry.json`에서 생성합니다.

## 사용 방법

- 레지스트리를 기계가 읽는 source of truth로 사용합니다.
- 이 파일을 사람이 읽는 상태 보드로 사용합니다.
- 레지스트리를 갱신한 뒤 이 파일을 다시 생성합니다.

## 요약

- 마지막 갱신: `2026-03-15`
- 정본 소스: `docs/meta/document-registry.json`

## Canonical Root Documents

These files define the canonical architecture meaning and repository entry points.

### [README](../../README.md)

- 목적: Repository entry point and top-level navigation.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Keep terminology aligned with the canonical specification.

### [Architecture Specification](../../terraform-3-layer-architecture-specification.md)

- 목적: Canonical architecture technical specification for the Terraform 3-layer model.
- 담당: architecture-specification
- 상태: `stable`
- 다음 작업:
  - Keep templates and rollout scenarios aligned with published architecture pages.

### [Architecture Conventions](../../terraform-3-layer-architecture-conventions.md)

- 목적: Canonical implementation and review conventions.
- 담당: architecture-conventions
- 상태: `stable`
- 다음 작업:
  - Keep concrete examples aligned with the canonical specification.

### [ADR-0001 Root Record](../../adr-3layer-architecture-contract-workspace.md)

- 목적: Root ADR that records the architecture decision and rationale.
- 담당: adr
- 상태: `stable`
- 다음 작업:
  - Keep in sync with the published ADR page when ADR structure evolves.

## Published Documentation Portal

These files support the published Hugo documentation portal.

### [Docs Portal Index](../)

- 목적: Human-friendly documentation landing page.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep task-based navigation aligned with section indexes and documentation governance pages.

### [Architecture Section Index](../architecture/)

- 목적: Section entry point for architecture specification pages.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep chapter structure aligned with the canonical specification and scenario/template pages.

### [Architecture Overview Page](../architecture/01-overview.md)

- 목적: Portal chapter for architecture purpose, scope, and design principles.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep scope and non-goals aligned with the canonical specification overview.

### [Glossary and Views Page](../architecture/01a-glossary-and-views.md)

- 목적: Shared glossary and Mermaid views for the published architecture section.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep terminology and diagrams aligned with the canonical specification.

### [Layers Page](../architecture/02-layers.md)

- 목적: Published explanation of Foundation, Platform, and Service layer responsibilities.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep layer examples and dependency rules aligned with the canonical specification.

### [Contracts Page](../architecture/03-contracts.md)

- 목적: Published definition of the contract model, lifecycle, and compatibility rules.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep contract examples and terminology synchronized with the canonical specification.

### [Ownership and References Page](../architecture/04-ownership-and-references.md)

- 목적: Published guidance for resource ownership and allowed reference directions.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep allowed exceptions and anti-patterns aligned with the canonical specification.

### [Workspace Model Page](../architecture/05-workspace-model.md)

- 목적: Published explanation of workspace roles, split criteria, and anti-patterns.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep workspace role terminology aligned with the canonical specification and conventions.

### [Shared Resources Page](../architecture/06-shared-resources.md)

- 목적: Published guidance for resource sets and optional internal partitioning.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep resource set examples aligned with the canonical specification and concrete examples.

### [Service Dependencies Page](../architecture/07-service-dependencies.md)

- 목적: Published rules for service-to-service contracts and mediated dependencies.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep service dependency examples aligned with conventions and ADR rationale.

### [Operations Page](../architecture/08-operations.md)

- 목적: Published guidance for change propagation, breaking changes, and legacy modernization.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep migration procedure wording aligned with the canonical specification.

### [Safety and Resilience Page](../architecture/09-safety-and-resilience.md)

- 목적: Published safety model for blast radius control, rollback, and migration.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep review questions and failure expectations aligned with the canonical specification.

### [Decision Checklist Page](../architecture/10-decision-checklist.md)

- 목적: Published quick checklist for classifying layers, contracts, and workspace splits.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep the checklist consistent with the canonical decision sequence.

### [Shared Resource Design Template Page](../architecture/11-shared-resource-design-template.md)

- 목적: Reusable template for documenting new shared resource designs.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Extend the template only when new shared resource patterns appear.

### [Migration and Rollout Scenarios Page](../architecture/12-migration-and-rollout-scenarios.md)

- 목적: Scenario-driven guidance for contract migration, rollout, and rollback.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Add new scenarios when real rollout patterns emerge.

### [Conventions Section Index](../conventions/)

- 목적: Section entry point for implementation conventions.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep chapter navigation aligned with the actual conventions document set.

### [Layer Classification Convention Page](../conventions/01-layer-classification.md)

- 목적: Published convention for classifying resources into Foundation, Platform, and Service.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep classification examples aligned with the canonical conventions.

### [Ownership Convention Page](../conventions/02-ownership.md)

- 목적: Published convention for determining lifecycle ownership.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep ownership rules aligned with contract provider semantics.

### [Contract Convention Page](../conventions/03-contracts.md)

- 목적: Published convention for contract naming, lifecycle, and publication.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep publication examples synchronized with the canonical conventions.

### [Workspace Convention Page](../conventions/04-workspaces.md)

- 목적: Published convention for workspace design and split signals.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep naming guidance and split heuristics aligned with the canonical conventions.

### [Network and IAM Convention Page](../conventions/05-network-and-iam.md)

- 목적: Published convention for SG ownership and workload role placement.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep network and IAM guidance aligned with ownership and access-control rules.

### [Shared Resource Convention Page](../conventions/06-shared-resources.md)

- 목적: Published convention for resource set-first design and optional partitioning.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep examples aligned with the architecture shared resource pages.

### [Service-to-Service Convention Page](../conventions/07-service-to-service.md)

- 목적: Published convention for service contracts and prohibited direct implementation dependencies.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep service interface examples aligned with the architecture dependency model.

### [Legacy Convention Page](../conventions/08-legacy.md)

- 목적: Published convention for interpreting and migrating legacy assets.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep modernization guidance aligned with the canonical legacy transition procedure.

### [Safety Convention Page](../conventions/09-safety.md)

- 목적: Published convention for change safety, blast radius control, and rollback expectations.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep anti-patterns aligned with the canonical safety section.

### [Review Checklist Page](../conventions/10-review-checklist.md)

- 목적: Published review checklist for evaluating ownership, contracts, and workspace design.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep review questions aligned with the canonical conventions checklist.

### [Concrete Examples Page](../conventions/11-concrete-examples.md)

- 목적: Operator-facing examples for workspace, naming, and shared resource conventions.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep examples synchronized with the canonical conventions.

### [ADR Index Page](../adr/)

- 목적: Published entry point for ADR navigation.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep the ADR listing aligned with the canonical ADR set.

### [ADR-0001 Published Page](../adr/adr-0001-3layer-architecture-contract-workspace.md)

- 목적: Published ADR summary that links back to the root decision record.
- 담당: docs-portal
- 상태: `stable`
- 다음 작업:
  - Keep the status and summary aligned with the root ADR.

## Documentation Governance

These files govern how Codex should maintain the documentation system itself.

### [Repository AGENTS](../../AGENTS.md)

- 목적: Rendered repository-specific agent instructions for maintaining the documentation system.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Regenerate together with CLAUDE.md after updating docs/meta/agent-instructions.md.

### [Repository CLAUDE](../../CLAUDE.md)

- 목적: Rendered Claude-compatible repository instructions mirrored from the shared agent guidance source.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Regenerate together with AGENTS.md after updating docs/meta/agent-instructions.md.

### [Agent Instructions Source](agent-instructions.md)

- 목적: Canonical source for the mirrored AGENTS.md and CLAUDE.md repository instruction files.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Update this file first whenever repository agent guidance changes.

### [Documentation System Index](../meta/)

- 목적: Entry point for the documentation maintenance and indexing system.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Keep linked from the docs portal and AGENTS guidance.

### [Document Registry](./document-registry.json)

- 목적: Single machine-readable source of truth for document scope, ownership, and progress.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Expand tracked documents whenever new portal or governance documents are added.

### [Work Index](work-index.md)

- 목적: Human-readable status board generated from the registry.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Regenerate after every registry update.

### [Terraform 3-Layer Doc Maintainer Skill](../../skills/terraform-3-layer-doc-maintainer/SKILL.md)

- 목적: Repository-local Codex skill for strengthening and maintaining the documentation system.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Keep the workflow and referenced local files aligned with the repository layout.

### [Repository Map Reference](../../skills/terraform-3-layer-doc-maintainer/references/repository-map.md)

- 목적: Repository-local reference map for document roles and maintenance boundaries used by the skill.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Update when document families or canonical ownership boundaries change.

### [Maintenance Playbook Reference](../../skills/terraform-3-layer-doc-maintainer/references/maintenance-playbook.md)

- 목적: Repository-local playbook for strengthening document structure and consistency.
- 담당: documentation-system
- 상태: `stable`
- 다음 작업:
  - Refine after real maintenance tasks expose workflow gaps.
