#!/usr/bin/env python3
"""
Normalize all conference/journal names to standard abbreviations
Format: ConferenceName23 (no space, 2-digit year)
"""

import csv
import re
import shutil
from datetime import datetime

def normalize_source(source):
    """
    Convert source to standard format: ConferenceName23
    Examples:
      - "IMWUT 2023" → "IMWUT23"
      - "CHI 2024" → "CHI24"
      - "Ubicomp 2023" → "Ubicomp23"
      - "arXiv(v1) 2024" → "arXiv(v1) 2024" (keep arXiv format)
    """
    # Keep arXiv format as-is
    if source.startswith("arXiv"):
        return source

    # Extract conference name and year
    # Pattern: "NAME YYYY" or "NAME YYYY"
    match = re.search(r'^(.+?)\s+(20\d{2})$', source.strip())
    if match:
        name = match.group(1).strip()
        year = match.group(2)
        short_year = year[2:]  # "2023" → "23"

        # Special cases
        abbreviations = {
            "IMWUT": "IMWUT",
            "Ubicomp": "Ubicomp",
            "CHI": "CHI",
            "UIST": "UIST",
            "ISWC": "ISWC",
            "UbiComp": "Ubicomp",  # Normalize
            "Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies": "IMWUT",
            "Proceedings of the CHI Conference on Human Factors in Computing Systems": "CHI",
            "ACM Symposium on User Interface Software and Technology": "UIST",
        }

        # Try to match known conferences
        for full, abbr in abbreviations.items():
            if full.lower() in name.lower() or name == full:
                return f"{abbr}{short_year}"

        # If not matched, keep original name but use short year
        return f"{name}{short_year}"

    return source

def main():
    input_file = "papers.csv"
    output_file = "papers.csv.tmp"
    backup_file = f"papers.csv.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Backup original
    shutil.copy(input_file, backup_file)
    print(f"✓ Backup created: {backup_file}")

    changes = []

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            old_source = row['Source']
            new_source = normalize_source(old_source)

            if old_source != new_source:
                changes.append((row['Title'], old_source, new_source))
                row['Source'] = new_source

            writer.writerow(row)

    # Replace original with updated
    shutil.move(output_file, input_file)

    # Report changes
    if changes:
        print(f"\n✓ Updated {len(changes)} sources:")
        for title, old, new in changes:
            title_short = title[:60] + "..." if len(title) > 60 else title
            print(f"  • {title_short}")
            print(f"    {old} → {new}")
    else:
        print("\n✓ No changes needed")

    print(f"\n✓ Done! Check papers.csv")
    print(f"  Backup: {backup_file}")

if __name__ == "__main__":
    main()
