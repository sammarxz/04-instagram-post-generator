import datetime
from scrap_quotes import get_quotes
from generate_posts import generate_images
from post_on_instagram import post

today = datetime.date.today()
filename = '{}.png'.format(today)

text = '''
-
#motivational #quote #motivationalquote #minimalquote #youcandothis
#inpiration #motivationalinspiration #minimal
'''

if __name__ == '__main__':
    # print(filename)
    quotes = get_quotes()
    generate_images(quotes)
    # post(filename, text)
