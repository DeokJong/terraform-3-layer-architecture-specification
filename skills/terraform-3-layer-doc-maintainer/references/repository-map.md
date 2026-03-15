# Repository Map

This reference explains how the Terraform 3-layer documentation repository is organized and which files act as canonical or derived sources.

## Canonical architecture sources

- `terraform-3-layer-architecture-specification.md`
  Defines the architecture meaning, layer model, contract model, workspace model, and safety rules.
- `terraform-3-layer-architecture-conventions.md`
  Defines implementation and review conventions derived from the architecture specification.
- `adr-3layer-architecture-contract-workspace.md`
  Records the architectural decision and rationale behind the 3-layer, contract, and workspace model.
- `README.md`
  Acts as the repository entry point and high-level navigation surface.

## Published portal sources

- `docs/index.md`
  Main landing page for the GitHub Pages portal.
- `docs/architecture/`
  Published chapter split of the architecture specification.
- `docs/conventions/`
  Published chapter split of the conventions document.
- `docs/adr/`
  Published ADR navigation and summary pages.
- `docs/meta/`
  Documentation governance and indexing pages for maintainers.

## Documentation governance sources

- `docs/meta/document-registry.json`
  Machine-readable source of truth for tracked documents, ownership, status, and next actions.
- `docs/meta/work-index.md`
  Generated human-readable status board. Regenerate this after every registry change.
- `docs/meta/agent-instructions.md`
  Canonical source for the rendered `AGENTS.md` and `CLAUDE.md` mirrors.

## Generated or mirrored outputs

- `docs/meta/work-index.md`
  Generated from `docs/meta/document-registry.json`.
- `AGENTS.md`
  Generated from `docs/meta/agent-instructions.md`.
- `CLAUDE.md`
  Generated from `docs/meta/agent-instructions.md`.

## Local maintenance tooling

- `skills/terraform-3-layer-doc-maintainer/SKILL.md`
  Repository-local maintenance skill.
- `skills/terraform-3-layer-doc-maintainer/scripts/render_work_index.py`
  Regenerates the work index from the registry.
- `skills/terraform-3-layer-doc-maintainer/scripts/render_agent_files.py`
  Regenerates `AGENTS.md` and `CLAUDE.md` from the canonical agent instructions source.

## Maintenance boundaries

- Edit canonical root documents first when architecture meaning changes.
- Edit `docs/` pages when the published portal structure or chapter wording needs to be aligned with the canonical source.
- Edit `docs/meta/document-registry.json` first when tracked scope, ownership, status, or next actions change.
- Do not edit `docs/meta/work-index.md`, `AGENTS.md`, or `CLAUDE.md` manually unless you immediately regenerate them from their canonical source files.
