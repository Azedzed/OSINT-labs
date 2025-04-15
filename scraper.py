import time
import requests
import bs4
from bs4 import BeautifulSoup

url = "https://pastebin.com/archive"

repsonse= requests.get(url)

soup = BeautifulSoup(repsonse.text, 'html.parser')

usernames = soup.find_all("div", class_="username")

for username in usernames:
    username_text = username.find('a').text.strip()
    print(username_text)

    