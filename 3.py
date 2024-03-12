""" 
Without Playwright - VueJS and HTML sites
"""
# from bs4 import BeautifulSoup
# import requests

# url = input("Enter url: ") # e.g. https://mblessed.vercel.app
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find and list all <style> tags and style attributes in other tags
# style_tags = soup.find_all('style')
# inline_styles = soup.find_all(style=True)

# print("Style Tags:")
# for tag in style_tags:
#     print(tag)

# print("\nInline Styles:")
# for tag in inline_styles:
#     print(f'{tag.name}[style] = {tag["style"]}')

""" 
With Playwright - React/NextJS sites
"""
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

url = input("Enter url: ") # e.g. https://aefinancialservicesllc.com/

# Launch the Playwright browser
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Navigate to the URL
    page.goto(url)
    
    # Wait for the page to load completely
    page.wait_for_load_state('networkidle')
    
    # Get the HTML content of the page
    html_content = page.content()

    # Close the browser
    browser.close()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find and list all <style> tags and style attributes in other tags
style_tags = soup.find_all('style')
inline_styles = soup.find_all(style=True)

print("Style Tags:")
for tag in style_tags:
    print(tag)

print("\nInline Styles:")
for tag in inline_styles:
    print(f'{tag.name}[style] = {tag["style"]}')
