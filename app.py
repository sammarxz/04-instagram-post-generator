import datetime
import textwrap
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


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


def draw_multiple_line_text(image, text, fontsize, text_color, text_start_height):
    font = ImageFont.truetype('./fonts/AUTHENTICSans-60.otf', fontsize)
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=24)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text((80, y_text), line, font=font, fill=text_color)
        y_text += line_height * 1.2


def generate_images(quotes):
    for i, quote in enumerate(quotes):
        post_width, post_height = 1080, 1080

        image = Image.new('RGB', (post_width, post_height), color='black')

        fontsize = 72

        text1 = quote['text']
        text2 = quote['author']

        text_color = (200, 200, 200)
        author_color = (100, 100, 100)

        text_start_height = 80

        draw_multiple_line_text(image, text1, fontsize, text_color,
                                text_start_height)
        draw_multiple_line_text(image, text2, int(fontsize / 2), author_color, 
                                post_height - text_start_height * 1.4)

        filename = '{}.png'.format(i)
        image.save('./posts/{}'.format(filename))


if __name__ == '__main__':
    quotes = get_quotes()
    generate_images(quotes)
