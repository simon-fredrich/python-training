from bs4 import BeautifulSoup
import requests

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.google.com/search?q=wie+alt+ist+das+universum', headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

snippet = soup.find("span", class_="hgKElc")
print(snippet.text)