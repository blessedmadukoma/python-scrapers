# Question: Test and report if all the JS used by the website are minified
import requests

def is_js_minified(js_content):
    """
    Simple heuristic to check if JavaScript is minified.
    This checks for the absence of newlines and comments as a proxy for minification.
    """
    lines = js_content.count('\n')
    comments = js_content.count('//') + js_content.count('/*') + js_content.count('*/')
    # Consider JS minified if it has fewer than a certain number of newlines
    # and not many comment lines.
    # These numbers can be adjusted based on your observations of minified JS files.
    return lines < 5 and comments < 5

def fetch_js_urls(page_url):
    """Fetch all JavaScript file URLs from a webpage."""
    js_urls = []
    try:
        response = requests.get(page_url)
        if response.status_code == 200:
            js_urls = [url for url in response.text.split() if url.endswith('.js')]
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    return js_urls

def main(url):
    js_urls = fetch_js_urls(url)
    for js_url in js_urls:
        try:
            response = requests.get(js_url)
            if response.status_code == 200:
                minified = is_js_minified(response.text)
                status = "Minified" if minified else "Not Minified"
                print(f"{js_url}: {status}")
            else:
                print(f"Failed to fetch {js_url}")
        except requests.RequestException as e:
            print(f"Error fetching JS: {e}")

if __name__ == "__main__":
    url = input("Enter URL: ")
    main(url)
