# Question: Check if the webpage is serving assets such as images, javascript, css etc from CDNs.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# List of known CDN domains
cdn_domains = [
    "cdn.jsdelivr.net",
    "cdnjs.cloudflare.com",
    "stackpath.bootstrapcdn.com",
    "cloudinary.com",
    # Add more CDN domains as needed
]

def check_cdn_usage(page_url):
    cdn_assets = {}
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all <img>, <script>, and <link> tags
            for tag in soup.find_all(['img', 'script', 'link']):
                src = tag.get('src')
                if src:
                    parsed_url = urlparse(src)
                    if parsed_url.netloc in cdn_domains:
                        cdn_assets[src] = parsed_url.netloc
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    return cdn_assets

def main(url):
    cdn_assets = check_cdn_usage(url)
    if cdn_assets:
        print("CDN assets found:")
        for asset, cdn_domain in cdn_assets.items():
            print(f"{asset} served from {cdn_domain}")
    else:
        print("No CDN assets found or unable to fetch the webpage.")

if __name__ == "__main__":
    test_url = input("Enter URL: ")
    main(test_url)
