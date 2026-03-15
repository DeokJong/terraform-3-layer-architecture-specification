---
title: Work Index
description: document registry에서 생성된 사람용 작업 상태 보드입니다.
hero_kicker: Documentation Governance
doc_section: meta
nav_parent: meta-index
nav_order: 3
---

# Work Index

This file is generated from `docs/meta/document-registry.json`.

## How to use

- Use the registry as the machine-readable source of truth.
- Use this file as the human-readable status board.
- Regenerate this file after registry updates.

## Summary

- Last updated: `2026-03-15`
- Canonical source: `docs/meta/document-registry.json`

## Canonical Root Documents

These files define the canonical architecture meaning and repository entry points.

### [README](../../README.md)

- Purpose: Repository entry point and top-level navigation.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Keep terminology aligned with the canonical specification.

### [Architecture Specification](../../terraform-3-layer-architecture-specification.md)

- Purpose: Canonical architecture technical specification for the Terraform 3-layer model.
- Owner: architecture-specification
- Status: `stable`
- Next actions:
  - Keep templates and rollout scenarios aligned with published architecture pages.

### [Architecture Conventions](../../terraform-3-layer-architecture-conventions.md)

- Purpose: Canonical implementation and review conventions.
- Owner: architecture-conventions
- Status: `stable`
- Next actions:
  - Keep concrete examples aligned with the canonical specification.

### [ADR-0001 Root Record](../../adr-3layer-architecture-contract-workspace.md)

- Purpose: Root ADR that records the architecture decision and rationale.
- Owner: adr
- Status: `stable`
- Next actions:
  - Keep in sync with the published ADR page when ADR structure evolves.

## Published Documentation Portal

These files support the GitHub Pages reading experience.

### [Docs Portal Index](../index.md)

- Purpose: Human-friendly documentation landing page.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep task-based navigation aligned with section indexes and documentation governance pages.

### [Architecture Section Index](../architecture/index.md)

- Purpose: Section entry point for architecture specification pages.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep chapter structure aligned with the canonical specification and scenario/template pages.

### [Architecture Overview Page](../architecture/01-overview.md)

- Purpose: Portal chapter for architecture purpose, scope, and design principles.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep scope and non-goals aligned with the canonical specification overview.

### [Glossary and Views Page](../architecture/01a-glossary-and-views.md)

- Purpose: Shared glossary and Mermaid views for the published architecture section.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep terminology and diagrams aligned with the canonical specification.

### [Layers Page](../architecture/02-layers.md)

- Purpose: Published explanation of Foundation, Platform, and Service layer responsibilities.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep layer examples and dependency rules aligned with the canonical specification.

### [Contracts Page](../architecture/03-contracts.md)

- Purpose: Published definition of the contract model, lifecycle, and compatibility rules.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep contract examples and terminology synchronized with the canonical specification.

### [Ownership and References Page](../architecture/04-ownership-and-references.md)

- Purpose: Published guidance for resource ownership and allowed reference directions.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep allowed exceptions and anti-patterns aligned with the canonical specification.

### [Workspace Model Page](../architecture/05-workspace-model.md)

- Purpose: Published explanation of workspace roles, split criteria, and anti-patterns.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep workspace role terminology aligned with the canonical specification and conventions.

### [Shared Resources Page](../architecture/06-shared-resources.md)

- Purpose: Published guidance for resource sets and optional internal partitioning.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep resource set examples aligned with the canonical specification and concrete examples.

### [Service Dependencies Page](../architecture/07-service-dependencies.md)

- Purpose: Published rules for service-to-service contracts and mediated dependencies.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep service dependency examples aligned with conventions and ADR rationale.

### [Operations Page](../architecture/08-operations.md)

- Purpose: Published guidance for change propagation, breaking changes, and legacy modernization.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep migration procedure wording aligned with the canonical specification.

### [Safety and Resilience Page](../architecture/09-safety-and-resilience.md)

- Purpose: Published safety model for blast radius control, rollback, and migration.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep review questions and failure expectations aligned with the canonical specification.

### [Decision Checklist Page](../architecture/10-decision-checklist.md)

- Purpose: Published quick checklist for classifying layers, contracts, and workspace splits.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep the checklist consistent with the canonical decision sequence.

### [Shared Resource Design Template Page](../architecture/11-shared-resource-design-template.md)

- Purpose: Reusable template for documenting new shared resource designs.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Extend the template only when new shared resource patterns appear.

### [Migration and Rollout Scenarios Page](../architecture/12-migration-and-rollout-scenarios.md)

- Purpose: Scenario-driven guidance for contract migration, rollout, and rollback.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Add new scenarios when real rollout patterns emerge.

### [Conventions Section Index](../conventions/index.md)

- Purpose: Section entry point for implementation conventions.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep chapter navigation aligned with the actual conventions document set.

### [Layer Classification Convention Page](../conventions/01-layer-classification.md)

- Purpose: Published convention for classifying resources into Foundation, Platform, and Service.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep classification examples aligned with the canonical conventions.

### [Ownership Convention Page](../conventions/02-ownership.md)

- Purpose: Published convention for determining lifecycle ownership.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep ownership rules aligned with contract provider semantics.

### [Contract Convention Page](../conventions/03-contracts.md)

- Purpose: Published convention for contract naming, lifecycle, and publication.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep publication examples synchronized with the canonical conventions.

### [Workspace Convention Page](../conventions/04-workspaces.md)

- Purpose: Published convention for workspace design and split signals.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep naming guidance and split heuristics aligned with the canonical conventions.

### [Network and IAM Convention Page](../conventions/05-network-and-iam.md)

- Purpose: Published convention for SG ownership and workload role placement.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep network and IAM guidance aligned with ownership and access-control rules.

### [Shared Resource Convention Page](../conventions/06-shared-resources.md)

- Purpose: Published convention for resource set-first design and optional partitioning.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep examples aligned with the architecture shared resource pages.

### [Service-to-Service Convention Page](../conventions/07-service-to-service.md)

- Purpose: Published convention for service contracts and prohibited direct implementation dependencies.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep service interface examples aligned with the architecture dependency model.

### [Legacy Convention Page](../conventions/08-legacy.md)

- Purpose: Published convention for interpreting and migrating legacy assets.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep modernization guidance aligned with the canonical legacy transition procedure.

### [Safety Convention Page](../conventions/09-safety.md)

- Purpose: Published convention for change safety, blast radius control, and rollback expectations.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep anti-patterns aligned with the canonical safety section.

### [Review Checklist Page](../conventions/10-review-checklist.md)

- Purpose: Published review checklist for evaluating ownership, contracts, and workspace design.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep review questions aligned with the canonical conventions checklist.

### [Concrete Examples Page](../conventions/11-concrete-examples.md)

- Purpose: Operator-facing examples for workspace, naming, and shared resource conventions.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep examples synchronized with the canonical conventions.

### [ADR Index Page](../adr/index.md)

- Purpose: Published entry point for ADR navigation.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep the ADR listing aligned with the canonical ADR set.

### [ADR-0001 Published Page](../adr/adr-0001-3layer-architecture-contract-workspace.md)

- Purpose: Published ADR summary that links back to the root decision record.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep the status and summary aligned with the root ADR.

## Documentation Governance

These files govern how Codex should maintain the documentation system itself.

### [Repository AGENTS](../../AGENTS.md)

- Purpose: Rendered repository-specific agent instructions for maintaining the documentation system.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Regenerate together with CLAUDE.md after updating docs/meta/agent-instructions.md.

### [Repository CLAUDE](../../CLAUDE.md)

- Purpose: Rendered Claude-compatible repository instructions mirrored from the shared agent guidance source.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Regenerate together with AGENTS.md after updating docs/meta/agent-instructions.md.

### [Agent Instructions Source](agent-instructions.md)

- Purpose: Canonical source for the mirrored AGENTS.md and CLAUDE.md repository instruction files.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Update this file first whenever repository agent guidance changes.

### [Documentation System Index](index.md)

- Purpose: Entry point for the documentation maintenance and indexing system.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Keep linked from the docs portal and AGENTS guidance.

### [Document Registry](document-registry.json)

- Purpose: Single machine-readable source of truth for document scope, ownership, and progress.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Expand tracked documents whenever new portal or governance documents are added.

### [Work Index](work-index.md)

- Purpose: Human-readable status board generated from the registry.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Regenerate after every registry update.

### [Terraform 3-Layer Doc Maintainer Skill](../../skills/terraform-3-layer-doc-maintainer/SKILL.md)

- Purpose: Repository-local Codex skill for strengthening and maintaining the documentation system.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Keep the workflow and referenced local files aligned with the repository layout.

### [Repository Map Reference](../../skills/terraform-3-layer-doc-maintainer/references/repository-map.md)

- Purpose: Repository-local reference map for document roles and maintenance boundaries used by the skill.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Update when document families or canonical ownership boundaries change.

### [Maintenance Playbook Reference](../../skills/terraform-3-layer-doc-maintainer/references/maintenance-playbook.md)

- Purpose: Repository-local playbook for strengthening document structure and consistency.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Refine after real maintenance tasks expose workflow gaps.
