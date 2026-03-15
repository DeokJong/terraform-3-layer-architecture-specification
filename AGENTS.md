<!-- Generated from docs/meta/agent-instructions.md for AGENTS.md. -->
<!-- Edit the source file, then re-render both AGENTS.md and CLAUDE.md together. -->

# AGENTS.md
## Purpose

This repository is a documentation-first Terraform architecture specification project.

The primary goal of any agent work here is to strengthen the architecture documentation, conventions, ADR linkage, and Hugo portal quality without fragmenting the source of truth.

## Mirror Policy

- Treat `docs/meta/agent-instructions.md` as the canonical source for both `AGENTS.md` and `CLAUDE.md`.
- Do not edit `AGENTS.md` or `CLAUDE.md` directly unless you immediately re-render both mirror files from `docs/meta/agent-instructions.md`.
- If either mirror file changes, update `docs/meta/agent-instructions.md` first and then regenerate both mirror files together.

Recommended command pattern:

```bash
uv run python skills/terraform-3-layer-doc-maintainer/scripts/render_agent_files.py
```

## Canonical Documents

The canonical root documents are:

- `README.md`
- `terraform-3-layer-architecture-specification.md`
- `terraform-3-layer-architecture-conventions.md`
- `adr-3layer-architecture-contract-workspace.md`

The canonical published portal is:

- `docs/_index.md`

## Documentation Source of Truth

Use this file as the machine-readable source of truth for document structure and work status:

- `docs/meta/document-registry.json`

Use this file as the human-readable generated work index:

- `docs/meta/work-index.md`

Use this published static mirror when the portal needs a raw registry download:

- `static/meta/document-registry.json`

Rules:

- Update `document-registry.json` first when changing document scope, ownership, status, or next actions.
- Regenerate `work-index.md` after updating the registry.
- Keep the static registry mirror aligned with the canonical registry.
- Keep root documents, `docs/`, the registry, and the agent instruction mirrors aligned.

## Agent Workflow

When working on this repository:

1. Read `docs/meta/document-registry.json`.
2. Read `docs/meta/work-index.md`.
3. Read the relevant canonical document sections only.
4. Apply edits.
5. Update the registry if scope, progress, or ownership changed.
6. If agent instructions changed, update `docs/meta/agent-instructions.md` and regenerate both `AGENTS.md` and `CLAUDE.md`.
7. Regenerate the work index.

Recommended command pattern:

```bash
uv run python skills/terraform-3-layer-doc-maintainer/scripts/render_work_index.py
```

## Skill

Use the repository skill when the task is about strengthening, restructuring, indexing, or maintaining the architecture documentation system:

- `skills/terraform-3-layer-doc-maintainer/SKILL.md`

## Guardrails

- Treat architecture meaning as more important than wording polish.
- Do not duplicate the same rule across many files unless the duplication is intentional and tracked in the registry.
- Prefer improving structure, examples, templates, and decision support over adding abstract prose.
- Keep docs optimized for agent maintenance as well as human reading.
- Every Mermaid block must include this config header directly under ````mermaid```` and must use `flowchart TB`:

```yaml
---
config:
  layout: elk
  theme: redux
  look: neo
---
```

