# Work Index

This file is generated from `docs/meta/document-registry.json`.

## How to use

- Use the registry as the machine-readable source of truth.
- Use this file as the human-readable status board.
- Regenerate this file after registry updates.

## Summary

- Last updated: `2026-03-14`
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
  - Keep in sync with published ADR page when ADR structure evolves.

## Published Documentation Portal

These files support the GitHub Pages reading experience.

### [Docs Portal Index](../index.md)

- Purpose: Human-friendly documentation landing page.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep task-based navigation aligned with templates and scenario guides.

### [Architecture Pages](../architecture/index.md)

- Purpose: Section entry point for architecture specification pages.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep reading order aligned with canonical specification and scenario/template pages.

### [Convention Pages](../conventions/index.md)

- Purpose: Section entry point for implementation conventions.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep example-driven quick links aligned with canonical conventions.

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

### [Concrete Examples Page](../conventions/11-concrete-examples.md)

- Purpose: Operator-facing examples for workspace, naming, and shared resource conventions.
- Owner: docs-portal
- Status: `stable`
- Next actions:
  - Keep examples synchronized with canonical conventions.

## Documentation Governance

These files govern how Codex should maintain the documentation system itself.

### [Repository AGENTS](../../AGENTS.md)

- Purpose: Repository-specific agent instructions for maintaining the documentation system.
- Owner: documentation-system
- Status: `stable`
- Next actions:
  - Keep aligned with the skill and registry workflow.

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
  - Expand tracked documents as templates and scenario guides are added.

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
  - Iterate after real maintenance tasks expose gaps.
