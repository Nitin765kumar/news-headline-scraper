import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL to scrape
URL = "https://www.bbc.com/news"

# File to save
OUTPUT_FILE = "headlines.txt"

def scrape_headlines():
    print("Fetching news from BBC...")
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all(['h1', 'h2', 'h3'])  # Multiple tags

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(f"🗓 Headlines Scraped on: {datetime.now()}\n\n")
        count = 0
        for i, tag in enumerate(headlines, 1):
            text = tag.get_text(strip=True)
            if text and len(text) > 10:  # Filter short/empty headlines
                file.write(f"{i}. {text}\n")
                count += 1

    print(f"Scraped {count} headlines and saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    scrape_headlines()