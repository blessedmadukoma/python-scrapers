# Question: Check and find out if the website is using any iframe or frame set

from bs4 import BeautifulSoup
import requests

url = input("Enter url: ") # e.g. https://mblessed.vercel.app

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

iframes = soup.find_all('iframe')
framesets = soup.find_all('frameset')

print("Iframes:", len(iframes))
print("Framesets:", len(framesets))
