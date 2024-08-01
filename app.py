import streamlit as st
from main import scrape

st.title('Comparing different webscraping techniques')

url = st.text_input('Enter URL:')
libraries = ['jina', 'firecrawl', 'beautifulsoup', 'newspaper3k']
#library = st.selectbox('Choose scraping library:', libraries)

selected_libraries = st.multiselect('Choose scraping libraries:', libraries)

if st.button('Scrape'):
    if url and selected_libraries:
        for library in selected_libraries:
            result = scrape(url, library)
            st.subheader(f'Results from {library}:')
            st.text_area(f'Scraping Results from {library}', result)
    else:
        st.error('Please enter a URL and select at least one scraping library.')

if st.button('Scrape'):
    if url and library:
        result = scrape(url, library)
        st.text_area('Scraping Results', result)
    else:
        st.error('Please enter a URL and select a scraping library.')


