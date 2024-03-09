# Question: Image caching - Check and report if website is using cache headers for images and browser is displaying images from cache.

import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import urljoin

def fetch_image_urls(page_url):
    """Fetch all image URLs from a webpage."""
    image_urls = []
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for img in soup.find_all('img'):
                src = img.get('src')
                if src:
                    image_urls.append(urljoin(page_url, src))
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    return image_urls

def check_cache_headers(image_urls):
    """Check and report cache headers for given image URLs."""
    for image_url in image_urls:
        try:
            response = requests.head(image_url)
            cache_control = response.headers.get('Cache-Control')
            etag = response.headers.get('ETag')
            if cache_control or etag:
                print(f"{image_url}: Uses cache headers. Cache-Control='{cache_control}', ETag='{etag}'")
            else:
                print(f"{image_url}: Does NOT use standard cache headers.")
        except requests.RequestException as e:
            print(f"Error fetching image: {e}")

def main(url):
    image_urls = fetch_image_urls(url)
    if image_urls:
        check_cache_headers(image_urls)
        webbrowser.open(url)
    else:
        print("No image URLs found or unable to fetch the webpage.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    main(url)
