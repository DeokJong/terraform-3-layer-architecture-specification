import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "docs" / "meta" / "document-registry.json"
OUTPUT = ROOT / "docs" / "meta" / "work-index.md"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def relative_link(path):
    if path.startswith("docs/meta/"):
        return path.removeprefix("docs/meta/")
    if path.startswith("docs/"):
        return f"../{path.removeprefix('docs/')}"
    return f"../../{path}"


def render(registry):
    lines = [
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


if __name__ == "__main__":
    main()
