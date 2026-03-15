---
title: Documentation System
description: English overview of the documentation governance section.
hero_kicker: Section Overview
doc_section: meta
nav_key: meta-index
nav_title: Overview
nav_order: 1
---

# Documentation System

This section covers the governance files used to maintain the repository documentation system itself.

## Core files

- [Document Registry](./document-registry.json)
- [Work Index](./work-index/)
- [Agent Instructions Source](./agent-instructions/)

## What this section is for

- Track the canonical source of truth for document structure and status
- Publish the generated human-readable work board
- Define how repository instruction mirrors are maintained
- Keep agent workflows aligned with the Hugo portal and registry

## Maintenance order

1. Update `document-registry.json` first when document structure or status changes.
2. Regenerate `work-index.md` and `work-index.en.md`.
3. If repository guidance changes, update `docs/meta/agent-instructions.md` and re-render `AGENTS.md` and `CLAUDE.md`.
4. Verify that the Hugo portal navigation still matches the actual document set.
