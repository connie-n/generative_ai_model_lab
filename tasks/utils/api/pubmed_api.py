from Bio import Entrez
from Bio import Medline

class PubMedClient:
    def __init__(self, email):
        Entrez.email = email

    def search(self, query, max_results=5):
        #max_result k로 변경하기
        handle = Entrez.esearch(
            db="pubmed",
            term=query,
            retmax=max_results
        )

        results = Entrez.read(handle)

        return results["IdList"]

    def fetch_details(self, pmids):

        handle = Entrez.efetch(
            db="pubmed",
            id=pmids, 
            rettype="medline",
            retmode="text"
        )

        records = Medline.parse(handle)

        papers = []

        for record in records:
            abstract = record.get("AB")
            if abstract:
                papers.append({
                    "pmid": record.get("PMID"),
                    "title": record.get("TI"),
                    "abstract": abstract,
                    "journal": record.get("JT"),
                    "year": record.get("DP")
                })

        return papers


