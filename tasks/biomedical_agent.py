import streamlit as st
from tasks.utils.api.pubmed_api import PubMedClient
import os
from dotenv import load_dotenv

def main(): 
        

    load_dotenv()
    email = os.getenv("PUBMED_EMAIL")

    client = PubMedClient(
        email = email
    )

    query = st.text_input(
        "Enter your PubMed search keyword"
    )

    max_results = st.number_input(
        "How many papers do you want to retrieve?",
        min_value=1,
        max_value=20,
        value=5
    )
    
    if st.button("Search"):
        pmids = client.search(
            query,
            max_results=max_results
        )

        papers = client.fetch_details(pmids)
        st.subheader(f"Found {len(papers)} papers")

        for i, paper in enumerate(papers):

            st.divider()
            st.write(f"### {i+1}. {paper['title']}")
            st.write(
                f"**Year:** {paper['year']}"
            )

            if paper["abstract"]:
                st.write(
                    "**Abstract:**"
                )
                st.write(
                    paper["abstract"][:600]
                )
            else:
                st.write(
                    "No abstract available"
                )


