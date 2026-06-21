from pathlib import Path
import mkdocs_gen_files

DOCS = Path("docs")
nav = mkdocs_gen_files.Nav()

def pretty(name: str) -> str:
    """
    Format a name for display.
    
    Returns:
        str: The name with underscores and hyphens replaced by spaces and words title-cased.
    """
    return name.replace("_", " ").replace("-", " ").title()

for path in sorted(DOCS.rglob("*.md")):
    if path.name.lower() == "summary.md":
        continue

    rel = path.relative_to(DOCS).as_posix()
    parts = list(path.relative_to(DOCS).with_suffix("").parts)

    # Root docs page
    if path.parent == DOCS and path.name.lower() in {"readme.md", "index.md"}:
        nav[("Home", "Home")] = rel
        continue

    # Turn README/index inside subfolders into section pages
    if parts[-1].lower() in {"readme", "index"}:
        parts[-1] = "Overview"
    else:
        parts[-1] = pretty(parts[-1])

    nav[tuple(["Home", *map(pretty, parts[:-1]), parts[-1]])] = rel

with mkdocs_gen_files.open("SUMMARY.md", "w") as f:
    f.writelines(nav.build_literate_nav())