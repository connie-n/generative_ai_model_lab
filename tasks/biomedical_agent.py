from tasks.utils.api.pubmed_api import PubMedClient
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("PUBMED_EMAIL")

client = PubMedClient(
    email = email
)

max_results = int(
    input("How many papers do you want to retreive?")
)

pmids = client.search(
    "diabetes",
    max_results=max_results
)

print(pmids)

papers = client.fetch_details(pmids)


for paper in papers:
    print("\n----------------")
    print(paper["title"])
    print(paper["year"])
    print(paper["abstract"][:600])


