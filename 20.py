# Question: Find out if the webpage is using .webp for image displays. List all the image links that are not .webp format

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def find_non_webp_images(page_url):
    non_webp_images = []
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for img in soup.find_all('img'):
                src = img.get('src')
                if src:
                    parsed_url = urlparse(src)
                    if parsed_url.path.endswith('.webp'):
                        print(f"{src}: Using .webp format")
                    else:
                        non_webp_images.append(urljoin(page_url, src))
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    return non_webp_images

def main(url):
    non_webp_images = find_non_webp_images(url)
    if non_webp_images:
        print("\nNon .webp image links:")
        for image in non_webp_images:
            print(image)
    else:
        print("No non .webp image links found or unable to fetch the webpage.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    main(url)
