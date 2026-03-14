# Repository Map

## Canonical root documents

- `README.md`: repository entry point
- `terraform-3-layer-architecture-specification.md`: architecture technical specification
- `terraform-3-layer-architecture-conventions.md`: implementation conventions
- `adr-3layer-architecture-contract-workspace.md`: root ADR

## Published docs

- `docs/index.md`: public documentation portal
- `docs/architecture/`: architecture pages
- `docs/conventions/`: conventions pages
- `docs/adr/`: ADR pages

## Governance and indexing

- `docs/meta/document-registry.json`: machine-readable source of truth
- `docs/meta/work-index.md`: generated human-readable work index

## Maintenance rule

If a document is added, renamed, split, promoted, deprecated, or substantially rewritten, update the registry first or immediately after the edit and regenerate the work index.

## Python tooling

Use the repository-local `uv` workflow for maintenance scripts.

- Dependency manifest: `pyproject.toml`
- Preferred execution: `uv run python ...`
