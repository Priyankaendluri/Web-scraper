import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    print(f"Found {len(links)} links on {url}:\n")
    for link in links:
        text = link.get_text(strip=True)
        href = link.get('href')
        print(f"Text: {text or 'N/A'} | URL: {href or 'N/A'}")

# Example usage
if __name__ == "__main__":
    target_url = "https://example.com"
    scrape_links(target_url)

