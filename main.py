from PIL import Image, ImageDraw, ImageFont 
import os, random

font_size = int(input("Font size (number only) >> "))
fuerte = str(input("Strong people >> "))
debil = str(input("Weak people >> "))

templates = os.listdir("assets")

while('font.ttf' in templates):
    templates.remove('font.ttf')

image = Image.open("assets/" + str(random.choice(templates)))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("assets/font.ttf", 30)



def writeText(text, font, color, pos): 
    lines = text.splitlines()
    width = font.getsize(max(lines, key=lambda s: len(s)))[0]
    height = font.getsize(text)[1] * len(lines)

    x, y = image.size 

    text_x = x-width-10
    if pos == "bottom":
        text_y=y-height-10    
    if pos == "center":
        text_y=y/2-height-10
    if pos == "top":
        text_y=height+10
    draw.text((text_x, text_y), text, font=font, fill=color)

writeText(fuerte,font,"white","top")
writeText(debil,font,"white","bottom")

image.save("output.png")