
import sys
import arxiv

def test_arxiv_api(paper_id):
    """
    Fetches paper data from the arXiv API using the 'arxiv' library
    and prints all available attributes of the result object.
    """
    try:
        # Use the Client to respect API rate limits
        client = arxiv.Client(
            page_size=1,
            delay_seconds=3.0, # Comply with arXiv's rate limit
            num_retries=3
        )
        
        # Search for the paper by its ID
        search = arxiv.Search(id_list=[paper_id])
        paper = next(client.results(search))

        if paper:
            print(f"--- Full API Response for arXiv ID: {paper_id} ---")
            # Iterate over all attributes of the paper object and print them
            for attr in dir(paper):
                # Ignore private attributes and methods
                if not attr.startswith('_') and not callable(getattr(paper, attr)):
                    value = getattr(paper, attr)
                    print(f"{attr}: {value}")
            print("-----------------------------------------------------")
        else:
            print(f"Could not find paper with ID: {paper_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_arxiv_api.py <ARXIV_PAPER_ID>")
        sys.exit(1)
    
    paper_id_to_test = sys.argv[1]
    test_arxiv_api(paper_id_to_test)
