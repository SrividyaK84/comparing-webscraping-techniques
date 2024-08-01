from utils import scrape_with_jina, scrape_with_firecrawl, scrape_with_beautifulsoup, scrape_with_newspaper

def scrape(url, library):
    if library == 'jina':
        return scrape_with_jina(url)
    elif library == 'firecrawl':
        return scrape_with_firecrawl(url)
    elif library == 'beautifulsoup':
        return scrape_with_beautifulsoup(url)
    elif library == 'newspaper3k':
        return scrape_with_newspaper(url)
    else:
        return 'Invalid library selected.'

