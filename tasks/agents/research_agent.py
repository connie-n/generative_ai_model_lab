from tasks.utils.api.pubmed_api import PubMedClient

class ResearchAgent:
    def __init__(self):
        self.pubmed=PubMedClient()

    def run(self, question):
        needs_ev