from PIL import Image
import os
# adapted from https://blog.waicung.net/adding-background-to-png/
def add_background(before_directory, after_directory, filename):
    os.chdir(before_directory)
    im = Image.open(filename)
    fill_color = (255,255,255)  # white background color
    im = im.convert("RGBA")  
    background = Image.new('RGBA', im.size, fill_color)
    background.paste(im, (im.split()[-1])) # alpha mask - transparency
    im = background 
    os.chdir("..")
    os.chdir(after_directory)
    im.convert("RGB").save(filename)


