import pandas as pd
import re

def generate_md_tables_by_topic(csv_file):
    df = pd.read_csv(csv_file)
    df.fillna('', inplace=True)
    tables = {}
    # Group by Topic, but only include topics that are actually in the DataFrame
    if 'Topic' not in df.columns or df['Topic'].isnull().all():
        return tables # Return empty if no topics exist

    for topic, group in df.groupby('Topic'):
        if group.empty:
            continue # Skip topics with no papers
        # Define the new, more concise header
        md_table = "| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |\n"
        md_table += "|---|---|---|---|---|---|---|\n"
        for index, row in group.iterrows():
            # Safely get all data for the row
            title = row.get('Title', '')
            link = row.get('Link', '')
            source = row.get('Source', '')
            authors_full = row.get('Authors', '')
            journal_ref = row.get('Journal_Ref', '')
            tag = row.get('Tag', '')
            subjects = row.get('Subjects', '')
            additional_info = row.get('Additional_Info', '')
            date = row.get('Date', '')
            
            # Combine Source and Journal Ref
            if journal_ref:
                source = f"{source} ({journal_ref})"

            # Format authors for display: first author + et al.
            if authors_full:
                first_author = authors_full.split(',')[0]
                authors_display = f"{first_author}, et al."
            else:
                authors_display = ''

            linked_title = f"[{title}]({link})" if link else title
            
            # Construct the row with the new, more concise fields
            md_table += f"| {source} | {linked_title} | {authors_display} | {tag} | {subjects} | {additional_info} | {date} |\n"
        tables[topic] = md_table
    return tables

def update_readme(readme_file, tables):
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()

    for topic, table in tables.items():
        start_marker = f"<!-- TABLE_START: {topic} -->"
        end_marker = f"<!-- TABLE_END: {topic} -->"
        
        pattern = re.compile(f"(?s){re.escape(start_marker)}(.*?){re.escape(end_marker)}")
        
        if pattern.search(content):
            content = pattern.sub(f"{start_marker}\n{table}{end_marker}", content)
        else:
            content += f"\n# {topic}\n{start_marker}\n{table}{end_marker}\n"

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    csv_file = "papers.csv"
    readme_file = "README.md"
    tables = generate_md_tables_by_topic(csv_file)
    update_readme(readme_file, tables)
    print(f"Successfully updated the README.md file with {len(tables)} topic(s).")