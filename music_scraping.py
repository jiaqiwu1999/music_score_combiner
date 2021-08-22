from Users.wujiaqi.Desktop.my_projects.combine_pdf import combine_pdf
from Users.wujiaqi.Desktop.my_projects.add_background import add_background
import re
import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
import glob
# This project aims to scrape and online images to pdf from a known url
# This project only targets at url from a Chinese platform that do not require a login to access scores!

print("Please select a mode:\n")
print("1: Use script to download\n")
print("2: Use BS to download\n")
choice = input()
url = input("Please enter a desired url: ")


example_url = "https://www.jitashe.org/tab/92993"
response = requests.get(example_url)

soup = BeautifulSoup(response.text, "html.parser")
all_images = soup.find_all("img")
valid_images = []
image_file = []
for image in all_images:
    prop = image.get("alt", None)
    if prop:
        guitar = re.search("吉他", str(prop))
        if guitar:
            valid_images.append(image.get("src"))

if (int(choice) == 1):
    with open('url.txt', 'w') as f:
        f.writelines(valid_images)
else:
    for url in valid_images:
        # construct a filename using the last part of the url
        filename = re.search(r'/([\w_-]+[.](jpg|png))$', url)
        with open(filename.group(), 'wb') as f: # write as binary file
            resp = requests.get(url)
            f.write(resp.content)
        add_background("./before_process", "./after_process", filename)
        image_file.append(filename)

combine_pdf("./after_process", "../result_files", image_file, "myPDF")

# remove redundant files using glob lib
# for file in glob.glob("*.png"):
#     os.remove(file)

# for file in glob.glob("*.jpg"):
#     os.remove(file)