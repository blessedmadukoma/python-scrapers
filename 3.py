from bs4 import BeautifulSoup
import requests

url = input("Enter url: ") # e.g. https://mblessed.vercel.app
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find and list all <style> tags and style attributes in other tags
style_tags = soup.find_all('style')
inline_styles = soup.find_all(style=True)

print("Style Tags:")
for tag in style_tags:
    print(tag)

print("\nInline Styles:")
for tag in inline_styles:
    print(f'{tag.name}[style] = {tag["style"]}')
