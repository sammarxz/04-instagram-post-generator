import requests
from bs4 import BeautifulSoup


def get_quotes():
    url = 'https://www.codeofliving.com/blog/55-powerful-short-quotes-sayings-life/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='exp-smart-read')

    quotes = []

    for item in results:
        quote_list = item.find('ol')

        if quote_list:
            for item in quote_list:
                if not item.findChildren('img', recursive=False):
                    quote_text = item.text.split('–')[0]
                    quote_author = item.find('strong').text.strip()

                    quote = {'text': quote_text, 'author': quote_author}
                    quotes.append(quote)

    return quotes

