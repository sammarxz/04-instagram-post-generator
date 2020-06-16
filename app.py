from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1080, 1080), color = 'black')

fnt = ImageFont.truetype('./fonts/AUTHENTICSans-60.otf', 22)

d = ImageDraw.Draw(img)
d.text((200, 200), "Hello World", font=fnt, fill=(255,255,255))

img.save('test.png')
