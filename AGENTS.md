# AGENTS.md

## Purpose

This repository is a documentation-first Terraform architecture specification project.

The primary goal of any Codex work here is to strengthen the architecture documentation, conventions, ADR linkage, and GitHub Pages documentation quality without fragmenting the source of truth.

## Canonical Documents

The canonical root documents are:

- [README.md](./README.md)
- [terraform-3-layer-architecture-specification.md](./terraform-3-layer-architecture-specification.md)
- [terraform-3-layer-architecture-conventions.md](./terraform-3-layer-architecture-conventions.md)
- [adr-3layer-architecture-contract-workspace.md](./adr-3layer-architecture-contract-workspace.md)

The canonical published portal is:

- [docs/index.md](./docs/index.md)

## Documentation Source of Truth

Use this file as the machine-readable source of truth for document structure and work status:

- [docs/meta/document-registry.json](./docs/meta/document-registry.json)

Use this file as the human-readable generated work index:

- [docs/meta/work-index.md](./docs/meta/work-index.md)

Rules:

- Update `document-registry.json` first when changing document scope, ownership, status, or next actions.
- Regenerate `work-index.md` after updating the registry.
- Keep root documents, `docs/`, and the registry aligned.

## Codex Workflow

When working on this repository:

1. Read [docs/meta/document-registry.json](./docs/meta/document-registry.json).
2. Read [docs/meta/work-index.md](./docs/meta/work-index.md).
3. Read the relevant canonical document sections only.
4. Apply edits.
5. Update the registry if scope, progress, or ownership changed.
6. Regenerate the work index.

Recommended command pattern:

```bash
uv run python skills/terraform-3-layer-doc-maintainer/scripts/render_work_index.py
```

## Skill

Use the repository skill when the task is about strengthening, restructuring, indexing, or maintaining the architecture documentation system:

- [skills/terraform-3-layer-doc-maintainer/SKILL.md](./skills/terraform-3-layer-doc-maintainer/SKILL.md)

## Guardrails

- Treat architecture meaning as more important than wording polish.
- Do not duplicate the same rule across many files unless the duplication is intentional and tracked in the registry.
- Prefer improving structure, examples, templates, and decision support over adding abstract prose.
- Keep docs optimized for Codex maintenance as well as human reading.
- Every Mermaid block must include this config header directly under ````mermaid````:

```yaml
---
config:
  layout: fixed
  theme: redux
  look: neo
---
```
