import requests
import newspaper
from IPython.display import Markdown
    
def scrape_with_jina(url):
    url_req='https://r.jina.ai/'+str(url)
    headers = {
        # 'Authorization': 'Bearer '
    }

    response = requests.get(url_req, headers=headers)
    return response.text

def scrape_with_firecrawl(url):
  
  from firecrawl import FirecrawlApp

  app = FirecrawlApp(api_key="fc-194e83f319314b5a93b132b6c256fa98")

  crawl_result = app.crawl_url(str(url), {'crawlerOptions': {'excludes': ['blog/*']}})
  for result in crawl_result:
    return result['markdown']
  
def scrape_with_beautifulsoup(url):
  
  from bs4 import BeautifulSoup
  page = requests.get(str(url))
  response = BeautifulSoup(page.content, "html.parser")
  return response.get_text()

def scrape_with_newspaper(url):
  
  
  url2=str(url)
  url_i = newspaper.Article(url="%s" % (url2), language='en')
  url_i.download()
  url_i.parse()
  response = url_i.text
  return response


    

