import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

count = 0
newsList = []

for title in soup.find_all("a", class_="DY5T1d RZIKme", href=True):
    url = "news.google.com/" + title['href']
    news = {
        "title": title.text.strip(),
        "link": url
    }

    newsList.append(news)
    count += 1

with open('google_news_data_' + datetime.now().strftime("%d-%m-%Y") + '.json', 'w') as f:
    json.dump(newsList, f, indent=4)
