# Question: Check and report if website is using cache headers for all CSS resource

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_css_urls(page_url):
    """Fetch all CSS file URLs from a webpage."""
    css_urls = []
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('link'):
                if 'stylesheet' in link.get('rel', []):
                    href = link.get('href')
                    if href:
                        css_urls.append(urljoin(page_url, href))
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    return css_urls

def check_cache_headers(css_urls):
    """Check and report cache headers for given CSS URLs."""
    for css_url in css_urls:
        try:
            response = requests.get(css_url)
            cache_control = response.headers.get('Cache-Control')
            etag = response.headers.get('ETag')
            if cache_control or etag:
                print(f"{css_url}: Uses cache headers. Cache-Control='{cache_control}', ETag='{etag}'")
            else:
                print(f"{css_url}: Does NOT use standard cache headers.")
        except requests.RequestException as e:
            print(f"Error fetching CSS: {e}")

def main(url):
    css_urls = fetch_css_urls(url)
    if css_urls:
        check_cache_headers(css_urls)
    else:
        print("No CSS files found or unable to fetch the webpage.")

if __name__ == "__main__":
    url = input("Enter URL:")
    main(url)
