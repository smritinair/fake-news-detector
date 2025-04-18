import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from fake_useragent import UserAgent

# Initialize
ua = UserAgent()
headers = {'User-Agent': ua.random}
data = []

def scrape_real_news():
    """Scrape real news from reputable sources"""
    try:
        # CNN News
        cnn_url = "https://edition.cnn.com/world"
        cnn_response = requests.get(cnn_url, headers=headers, timeout=10)
        cnn_soup = BeautifulSoup(cnn_response.text, 'html.parser')
        
        for article in cnn_soup.select('h3.container__headline a'):
            title = article.get_text(strip=True)
            if title:
                data.append({'text': title, 'label': 'real', 'source': 'CNN'})

        # BBC News
        bbc_url = "https://www.bbc.com/news/world"
        bbc_response = requests.get(bbc_url, headers=headers, timeout=10)
        bbc_soup = BeautifulSoup(bbc_response.text, 'html.parser')
        
        for article in bbc_soup.select('h3.gs-c-promo-heading__title'):
            title = article.get_text(strip=True)
            if title:
                data.append({'text': title, 'label': 'real', 'source': 'BBC'})

    except Exception as e:
        print(f"Error scraping real news: {e}")

def scrape_fake_news():
    """Scrape questionable news from known fake news sites"""
    try:
        # Fake news site 1 (example)
        fake_url1 = "https://www.theonion.com/"
        fake_response1 = requests.get(fake_url1, headers=headers, timeout=10)
        fake_soup1 = BeautifulSoup(fake_response1.text, 'html.parser')
        
        for article in fake_soup1.select('h4.sc-1qoge05-0'):
            title = article.get_text(strip=True)
            if title:
                data.append({'text': title, 'label': 'fake', 'source': 'The Onion'})

    except Exception as e:
        print(f"Error scraping fake news: {e}")

def save_to_csv():
    """Save collected data to CSV"""
    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset=['text'])
    df.to_csv('data/news_samples.csv', index=False)
    print(f"Saved {len(df)} news samples to data/news_samples.csv")

if __name__ == '__main__':
    scrape_real_news()
    scrape_fake_news()
    save_to_csv()
