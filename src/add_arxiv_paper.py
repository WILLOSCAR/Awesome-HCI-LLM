
import sys
import arxiv
import csv
import re
from datetime import datetime

def get_arxiv_paper_details(arxiv_link):
    # Extract paper ID from link
    match = re.search(r'(\d{4}\.\d{4,5})', arxiv_link)
    if not match:
        print("Error: Could not extract a valid arXiv ID from the link.")
        return None
    paper_id = match.group(1)

    try:
        client = arxiv.Client(page_size=1, delay_seconds=3.0, num_retries=3)
        search = arxiv.Search(id_list=[paper_id])
        paper = next(client.results(search))
    except Exception as e:
        print(f"Error fetching data from arXiv API: {e}")
        return None

    if not paper:
        print(f"Could not find paper with ID: {paper_id}")
        return None

    # --- Extract all details ---
    title = paper.title
    
    # Authors (up to 3)
    authors = ", ".join([author.name for author in paper.authors[:3]])
    if len(paper.authors) > 3:
        authors += ", et al."

    # Version and Date
    version_match = re.search(r'v(\d+)$', paper.pdf_url)
    version = f"v{version_match.group(1)}" if version_match else 'v1'
    updated_date = paper.updated
    year = updated_date.year
    date_formatted = updated_date.strftime('%Y.%m')

    source = f"arXiv({version}) {year}"
    subjects = ", ".join(paper.categories)
    doi = paper.doi or ''
    journal_ref = paper.journal_ref or ''

    return {
        'Source': source,
        'Title': title,
        'Authors': authors,
        'DOI': doi,
        'Journal_Ref': journal_ref,
        'Link': paper.entry_id,
        'Tag': 'arxiv',
        'Subjects': subjects,
        'Additional_Info': paper.comment or '',
        'Date': date_formatted,
    }

def append_to_csv(file_path, paper_details, topic):
    paper_details['Topic'] = topic
    fieldnames = ['Source', 'Title', 'Authors', 'DOI', 'Journal_Ref', 'Link', 'Tag', 'Subjects', 'Additional_Info', 'Date', 'Topic']
    
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            # Write header only if the file is new/empty
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(paper_details)
        print(f"Successfully added '{paper_details['Title']}' to {file_path}")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_arxiv_paper.py <ARXIV_PAPER_LINK_OR_ID> <TOPIC>")
        sys.exit(1)

    arxiv_identifier = sys.argv[1]
    topic = sys.argv[2]

    details = get_arxiv_paper_details(arxiv_identifier)
    if details:
        append_to_csv('papers.csv', details, topic)
