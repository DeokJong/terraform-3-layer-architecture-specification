# Maintenance Playbook

Use this playbook when strengthening document structure, consistency, and maintainability across the repository.

## 1. Start from the source of truth

1. Read `docs/meta/document-registry.json`.
2. Read `docs/meta/work-index.md`.
3. Read only the canonical documents relevant to the task.

## 2. Prefer structural fixes over prose expansion

- Fix broken navigation before rewriting explanations.
- Add or improve reusable templates, checklists, matrices, and operating procedures before adding abstract text.
- Remove ambiguity between canonical, published, and generated files.

## 3. Keep canonical and published docs aligned

- If a root canonical document changes meaning, update the corresponding `docs/` pages that publish that meaning.
- If a `docs/` page introduces a new structure or page family, register it in `docs/meta/document-registry.json`.
- When navigation changes, update section indexes so readers can find the full set consistently.

## 4. Keep governance artifacts working

- Update `docs/meta/document-registry.json` before regenerating `docs/meta/work-index.md`.
- Update `docs/meta/agent-instructions.md` before regenerating `AGENTS.md` and `CLAUDE.md`.
- Ensure local skills reference files that actually exist in the repository.

## 5. Review checklist for maintenance tasks

- Is the canonical source explicit?
- Are generated files clearly identified as derived artifacts?
- Does the registry track the real published document set?
- Do section indexes match the files they are supposed to expose?
- Are ADR status and summary pages aligned with the root ADR?
- Are maintenance instructions executable without missing references?

## 6. Regeneration commands

```bash
uv run python skills/terraform-3-layer-doc-maintainer/scripts/render_work_index.py
uv run python skills/terraform-3-layer-doc-maintainer/scripts/render_agent_files.py
```
