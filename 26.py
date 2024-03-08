# Question: Test and report if all the CSS used by the website are minified

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def is_css_minified(css_content):
    """
    Simple heuristic to check if CSS is minified.
    This checks for the absence of newlines and comments as a proxy for minification.
    """
    lines = css_content.count('\n')
    comments = css_content.count('/*')
    # Consider a CSS minified if it has fewer than a certain number of newlines
    # and not many comment blocks.
    # These numbers can be adjusted based on your observations of minified CSS files.
    return lines < 5 and comments < 5

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

def main(url):
    css_urls = fetch_css_urls(url)
    for css_url in css_urls:
        try:
            response = requests.get(css_url)
            if response.status_code == 200:
                minified = is_css_minified(response.text)
                status = "Minified" if minified else "Not Minified"
                print(f"{css_url}: {status}")
            else:
                print(f"Failed to fetch {css_url}")
        except requests.RequestException as e:
            print(f"Error fetching CSS: {e}")

if __name__ == "__main__":
    url = input("Enter URL: ")
    main(url)
