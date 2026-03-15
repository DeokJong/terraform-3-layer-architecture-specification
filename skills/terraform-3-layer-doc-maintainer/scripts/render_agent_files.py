from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "docs" / "meta" / "agent-instructions.md"
TARGETS = {
    "AGENTS.md": ROOT / "AGENTS.md",
    "CLAUDE.md": ROOT / "CLAUDE.md",
}

TITLE_PREFIX = "# "
BODY_MARKER = "<!-- BEGIN MIRROR BODY -->"


def build_document(target_name: str, source_text: str) -> str:
    _, marker, body = source_text.partition(BODY_MARKER)
    if not marker:
        raise ValueError(f"Missing mirror body marker: {BODY_MARKER}")
    note = [
        f"<!-- Generated from docs/meta/agent-instructions.md for {target_name}. -->",
        "<!-- Edit the source file, then re-render both AGENTS.md and CLAUDE.md together. -->",
        "",
        f"{TITLE_PREFIX}{target_name}",
        "",
    ]
    return "\n".join(note) + body.lstrip()


def main() -> None:
    source_text = SOURCE.read_text(encoding="utf-8")
    for target_name, target_path in TARGETS.items():
        target_path.write_text(build_document(target_name, source_text), encoding="utf-8")


if __name__ == "__main__":
    main()
