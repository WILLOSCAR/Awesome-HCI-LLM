#!/usr/bin/env python3
"""
Fix over-normalization: Only normalize long conference names
Keep short ones like CVPR, ICLR, NIPS, ISWC unchanged
"""

import csv
import shutil
from datetime import datetime

def restore_short_names(source):
    """
    Restore short conference names that shouldn't be normalized
    Only normalize: CHI, Ubicomp, UIST (long names)
    Keep as-is: CVPR, ICLR, NIPS, ISWC, IMWUT (already short)
    """
    # Mapping to restore
    restore_map = {
        "CVPR24": "CVPR 2024",
        "CVPR23": "CVPR 2023",
        "ICLR24": "ICLR 2024",
        "ICLR23": "ICLR 2023",
        "NIPS24": "NIPS 2024",
        "NIPS23": "NIPS 2023",
        "NIPS22": "NIPS 2022",
        "ISWC24": "ISWC 2024",
        "ISWC23": "ISWC 2023",
        "ISWC22": "ISWC 2022",
        "IMWUT24": "IMWUT 2024",
        "IMWUT23": "IMWUT 2023",
        "IMWUT22": "IMWUT 2022",
    }

    # Keep these normalized (long names)
    # CHI23, CHI24, Ubicomp23, Ubicomp24, UIST23, UIST24

    return restore_map.get(source, source)

def main():
    input_file = "papers.csv"
    output_file = "papers.csv.tmp"
    backup_file = f"papers.csv.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Backup
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
            new_source = restore_short_names(old_source)

            if old_source != new_source:
                changes.append((row['Title'], old_source, new_source))
                row['Source'] = new_source

            writer.writerow(row)

    shutil.move(output_file, input_file)

    if changes:
        print(f"\n✓ Restored {len(changes)} sources:")
        for title, old, new in changes:
            title_short = title[:50] + "..." if len(title) > 50 else title
            print(f"  • {old} → {new}")
            print(f"    ({title_short})")
    else:
        print("\n✓ No changes needed")

    print(f"\n✓ Done!")
    print("\nNormalized (compact): CHI23, Ubicomp23, UIST23")
    print("Kept original: CVPR 2024, ICLR 2024, NIPS 2023, ISWC 2023, IMWUT 2024")

if __name__ == "__main__":
    main()
