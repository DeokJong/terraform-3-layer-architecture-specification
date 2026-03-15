import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "docs" / "meta" / "document-registry.json"
OUTPUT = ROOT / "docs" / "meta" / "work-index.md"
STATIC_REGISTRY = ROOT / "static" / "meta" / "document-registry.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def relative_link(path):
    if path == "docs/_index.md":
        return "../"
    if path.startswith("docs/") and path.endswith("/_index.md"):
        return f"../{path.removeprefix('docs/').removesuffix('/_index.md')}/"
    if path == "docs/meta/document-registry.json":
        return "./document-registry.json"
    if path.startswith("docs/meta/"):
        return path.removeprefix("docs/meta/")
    if path.startswith("docs/"):
        return f"../{path.removeprefix('docs/')}"
    return f"../../{path}"


def render(registry):
    lines = [
        "---",
        "title: Work Index",
        "description: document registry에서 생성된 사람용 작업 상태 보드입니다.",
        "hero_kicker: Documentation Governance",
        "doc_section: meta",
        "nav_parent: meta-index",
        "nav_order: 3",
        "---",
        "",
        "# Work Index",
        "",
        "This file is generated from `docs/meta/document-registry.json`.",
        "",
        "## How to use",
        "",
        "- Use the registry as the machine-readable source of truth.",
        "- Use this file as the human-readable status board.",
        "- Regenerate this file after registry updates.",
        "",
        "## Summary",
        "",
        f"- Last updated: `{registry['last_updated']}`",
        f"- Canonical source: `{registry['source_of_truth']}`",
        "",
    ]

    for section in registry["sections"]:
        lines.append(f"## {section['name']}")
        lines.append("")
        lines.append(section["description"])
        lines.append("")
        for item in section["documents"]:
            link = relative_link(item["path"])
            lines.append(f"### [{item['title']}]({link})")
            lines.append("")
            lines.append(f"- Purpose: {item['purpose']}")
            lines.append(f"- Owner: {item['owner']}")
            lines.append(f"- Status: `{item['status']}`")
            if item.get("next_actions"):
                lines.append("- Next actions:")
                for action in item["next_actions"]:
                    lines.append(f"  - {action}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    registry = load_registry()
    OUTPUT.write_text(render(registry), encoding="utf-8")
    STATIC_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REGISTRY, STATIC_REGISTRY)


if __name__ == "__main__":
    main()
