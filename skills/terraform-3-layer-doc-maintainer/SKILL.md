---
name: terraform-3-layer-doc-maintainer
description: Maintain and strengthen the Terraform 3-layer architecture documentation system in this repository. Use when Codex needs to improve the architecture specification, conventions, ADR linkage, Hugo docs structure, document indexing, source-of-truth tracking, or reusable documentation workflows for this project.
---

# Terraform 3-Layer Doc Maintainer

Use the repository documentation system, not ad hoc edits.

## Core workflow

1. Read `docs/meta/document-registry.json`.
2. Read `docs/meta/work-index.md`.
3. Read only the canonical documents relevant to the task.
4. Edit canonical sources first.
5. Update the registry when document scope, status, or next actions changed.
6. Regenerate `docs/meta/work-index.md` with `scripts/render_work_index.py`.
7. If agent guidance changed, update `docs/meta/agent-instructions.md` and regenerate both `AGENTS.md` and `CLAUDE.md` with `scripts/render_agent_files.py`.

## Canonical sources

- `terraform-3-layer-architecture-specification.md`
- `terraform-3-layer-architecture-conventions.md`
- `adr-3layer-architecture-contract-workspace.md`
- `docs/`

## Use references

- Read `references/repository-map.md` for repository-specific document roles and maintenance rules.
- Read `references/maintenance-playbook.md` when the task is about strengthening document quality or adding structure.

## Required maintenance rules

- Treat `docs/meta/document-registry.json` as the single machine-readable source of truth.
- Keep the human-facing `docs/meta/work-index.md` in sync by regenerating it.
- Prefer adding reusable structure such as templates, matrices, diagrams, and operating procedures over adding broad prose.
- When adding a new document family or section, register it in the registry immediately.
- Every Mermaid block must include this config header directly under ````mermaid```` and must use `flowchart TB`:

```yaml
---
config:
  layout: elk
  theme: redux
  look: neo
---
```

## Script

Regenerate the work index with:

```bash
uv run python skills/terraform-3-layer-doc-maintainer/scripts/render_work_index.py
```

Regenerate the agent instruction mirrors with:

```bash
uv run python skills/terraform-3-layer-doc-maintainer/scripts/render_agent_files.py
```
