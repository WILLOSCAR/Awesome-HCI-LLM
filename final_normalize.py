#!/usr/bin/env python3
"""
Final normalization rules:
- AI/HCI Conferences: Use compact format (CHI23, Ubicomp23, CVPR24, ICLR24, NIPS23, UIST24)
- Journals/Workshops: Keep original format (IMWUT 2024, ISWC 2023)
"""

import csv
import re
import shutil
from datetime import datetime

def normalize_final(source):
    """
    Conferences → Compact (ConferenceName23)
    Journals → Original (IMWUT 2024)
    """
    # Skip arXiv
    if source.startswith("arXiv"):
        return source

    # Extract name and year
    match = re.search(r'^(.+?)\s+(20\d{2})$', source.strip())
    if match:
        name = match.group(1).strip()
        year = match.group(2)
        short_year = year[2:]

        # Conferences (use compact format)
        conferences = [
            "CHI", "CVPR", "ICLR", "NIPS", "NeurIPS", "ICML",
            "Ubicomp", "UbiComp", "UIST", "AAAI", "IJCAI",
            "EMNLP", "ACL", "NAACL", "ICCV", "ECCV"
        ]

        for conf in conferences:
            if conf.lower() == name.lower() or conf in name:
                # Normalize name
                if "neurips" in name.lower():
                    return f"NIPS{short_year}"
                elif "ubicomp" in name.lower():
                    return f"Ubicomp{short_year}"
                else:
                    return f"{conf}{short_year}"

        # Journals/Workshops (keep original)
        journals = ["IMWUT", "ISWC", "TOCHI", "TVCG"]
        for journal in journals:
            if journal.lower() in name.lower():
                return source  # Keep as-is

    return source

def main():
    input_file = "papers.csv"
    output_file = "papers.csv.tmp"
    backup_file = f"papers.csv.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    shutil.copy(input_file, backup_file)
    print(f"✓ Backup: {backup_file}")

    changes = []

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            old_source = row['Source']
            new_source = normalize_final(old_source)

            if old_source != new_source:
                changes.append((row['Title'], old_source, new_source))
                row['Source'] = new_source

            writer.writerow(row)

    shutil.move(output_file, input_file)

    if changes:
        print(f"\n✓ Normalized {len(changes)} sources:")
        for title, old, new in changes:
            title_short = title[:45] + "..." if len(title) > 45 else title
            print(f"  {old:20} → {new:15} ({title_short})")
    else:
        print("\n✓ No changes needed")

    print("\n📋 Format Summary:")
    print("  Conferences: CHI23, Ubicomp23, CVPR24, ICLR24, NIPS23")
    print("  Journals:    IMWUT 2024, ISWC 2023 (kept original)")

if __name__ == "__main__":
    main()
