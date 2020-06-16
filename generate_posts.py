import datetime
import textwrap
from PIL import Image, ImageDraw, ImageFont


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



def generate_image_filenames(maxrange, i):
    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(maxrange)]

    return '{}.png'.format(date_list[i].strftime('%Y-%m-%d'))


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


        filename = generate_image_filenames(len(quotes), i)
        image.save('./posts/{}'.format(filename))
