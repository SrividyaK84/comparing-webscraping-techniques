import streamlit as st
from main import scrape

st.title('Comparing different webscraping techniques')

url = st.text_input('Enter URL:')
library = st.selectbox('Choose scraping library:', ['jina', 'firecrawl', 'beautifulsoup', 'newspaper3k'])

if st.button('Scrape'):
    if url and library:
        result = scrape(url, library)
        st.text_area('Scraping Results', result)
    else:
        st.error('Please enter a URL and select a scraping library.')


