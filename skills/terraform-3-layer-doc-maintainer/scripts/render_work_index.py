import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "docs" / "meta" / "document-registry.json"
OUTPUT = ROOT / "docs" / "meta" / "work-index.md"
OUTPUT_EN = ROOT / "docs" / "meta" / "work-index.en.md"
STATIC_REGISTRY = ROOT / "static" / "meta" / "document-registry.json"

TEXT = {
    "ko": {
        "title": "작업 인덱스",
        "description": "문서 레지스트리에서 생성한 사람이 읽는 작업 상태 보드입니다.",
        "hero_kicker": "문서 거버넌스",
        "heading": "# 작업 인덱스",
        "generated_from": "이 파일은 `docs/meta/document-registry.json`에서 생성합니다.",
        "how_to_use": "## 사용 방법",
        "how_to_use_items": [
            "레지스트리를 기계가 읽는 source of truth로 사용합니다.",
            "이 파일을 사람이 읽는 상태 보드로 사용합니다.",
            "레지스트리를 갱신한 뒤 이 파일을 다시 생성합니다.",
        ],
        "summary": "## 요약",
        "last_updated": "마지막 갱신",
        "canonical_source": "정본 소스",
        "purpose": "목적",
        "owner": "담당",
        "status": "상태",
        "next_actions": "다음 작업",
    },
    "en": {
        "title": "Work Index",
        "description": "Human-readable work status board generated from the document registry.",
        "hero_kicker": "Documentation Governance",
        "heading": "# Work Index",
        "generated_from": "This file is generated from `docs/meta/document-registry.json`.",
        "how_to_use": "## How to use",
        "how_to_use_items": [
            "Use the registry as the machine-readable source of truth.",
            "Use this file as the human-readable status board.",
            "Regenerate this file after registry updates.",
        ],
        "summary": "## Summary",
        "last_updated": "Last updated",
        "canonical_source": "Canonical source",
        "purpose": "Purpose",
        "owner": "Owner",
        "status": "Status",
        "next_actions": "Next actions",
    },
}


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


def render(registry, language):
    text = TEXT[language]
    lines = [
        "---",
        f"title: {text['title']}",
        f"description: {text['description']}",
        f"hero_kicker: {text['hero_kicker']}",
        "doc_section: meta",
        "nav_parent: meta-index",
        "nav_order: 3",
        "---",
        "",
        text["heading"],
        "",
        text["generated_from"],
        "",
        text["how_to_use"],
        "",
    ]

    for item in text["how_to_use_items"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            text["summary"],
            "",
            f"- {text['last_updated']}: `{registry['last_updated']}`",
            f"- {text['canonical_source']}: `{registry['source_of_truth']}`",
            "",
        ]
    )

    for section in registry["sections"]:
        lines.append(f"## {section['name']}")
        lines.append("")
        lines.append(section["description"])
        lines.append("")
        for item in section["documents"]:
            link = relative_link(item["path"])
            lines.append(f"### [{item['title']}]({link})")
            lines.append("")
            lines.append(f"- {text['purpose']}: {item['purpose']}")
            lines.append(f"- {text['owner']}: {item['owner']}")
            lines.append(f"- {text['status']}: `{item['status']}`")
            if item.get("next_actions"):
                lines.append(f"- {text['next_actions']}:")
                for action in item["next_actions"]:
                    lines.append(f"  - {action}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    registry = load_registry()
    OUTPUT.write_text(render(registry, "ko"), encoding="utf-8")
    OUTPUT_EN.write_text(render(registry, "en"), encoding="utf-8")
    STATIC_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REGISTRY, STATIC_REGISTRY)


if __name__ == "__main__":
    main()
