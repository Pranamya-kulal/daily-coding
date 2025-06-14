import os
import re

NOTES_DIR = "notes"
README_FILE = "README.md"

def extract_metadata(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    title_match = re.search(r"## 🔢 Problem:\s*(.+)", content)
    diff_match = re.search(r"\*\*Difficulty:\*\*\s*(\w+)", content)
    tags_match = re.search(r"## 📌 Tags\n(.+)", content)

    title = title_match.group(1).strip() if title_match else "Unknown"
    difficulty = diff_match.group(1).strip() if diff_match else "Unknown"
    tags = tags_match.group(1).strip().replace("`", "") if tags_match else "None"
    
    return title, difficulty, tags

def build_table():
    rows = []
    for filename in sorted(os.listdir(NOTES_DIR)):
        if filename.endswith(".md"):
            path = os.path.join(NOTES_DIR, filename)
            date = filename.replace(".md", "")
            title, difficulty, tags = extract_metadata(path)
            link = f"[{title}]({NOTES_DIR}/{filename})"
            rows.append(f"| {date} | {link} | {difficulty} | {tags} |")
    return rows

def update_readme(rows):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start = "<!--START_TABLE-->"
    end = "<!--END_TABLE-->"
    table = "\n".join([
        "| Date | Problem Title | Difficulty | Tags |",
        "|------|----------------|------------|------|",
        *rows
    ])
    updated = re.sub(
        f"{start}.*?{end}",
        f"{start}\n{table}\n{end}",
        content,
        flags=re.DOTALL
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    rows = build_table()
    update_readme(rows)
    print("✅ Dashboard updated in README.md!")
