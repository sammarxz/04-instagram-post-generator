import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# from PIL import Image, ImageDraw, ImageFont

# img = Image.new('RGB', (1080, 1080), color = 'black')

# fnt = ImageFont.truetype('./fonts/AUTHENTICSans-60.otf', 22)

# d = ImageDraw.Draw(img)
# d.text((200, 200), "Hello World", font=fnt, fill=(255,255,255))

# img.save('test.png')


url = 'https://www.codeofliving.com/blog/55-powerful-short-quotes-sayings-life/'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
results = soup.find_all('div', class_='exp-smart-read')

quotes = []

for item in results:
    quote_list = item.find('ol')

    for quote in quote_list:
        if not quote.findChildren('img', recursive=False):
            quote_text = quote.text.split('–')[0]
            quote_author = quote.find('strong').text.strip()

            quote = {'quote': quote_text, 'author': quote_author}
            quotes.append(quote)

    print(quotes)

