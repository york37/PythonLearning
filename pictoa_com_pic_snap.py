#
#
#  works for http://www.pictoa.com
#
#

from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import requests
import re

o = "C:/Users/yuego/Downloads/Images"

while True:
    first_link = input("link: ")

    if first_link == "q":
        break

    link = first_link
    counter = 0
    while True:
        web_html = requests.get(link)
        soup = BeautifulSoup(web_html.text, "html.parser")

        # capture image src and next page url
        tag_a = soup.find(id="img-next", rel="nofollow")
        next_link = tag_a["href"]
        tag_img = tag_a.find("img")
        image_src = tag_img["src"]
        tag_b = soup.find("h1")
        tag_title = tag_b.find("a")
        title = re.sub('[^a-zA-Z0-9\n\.]', ' ', tag_title.get_text()).rstrip()


        print(next_link)

        # save the image
        directory = os.path.join(o, title)
        if not os.path.exists(directory):
            os.makedirs(directory)
        output_file = os.path.join(directory, str(counter) + '.jpg')
        web_image = requests.get(image_src)
        i = Image.open(BytesIO(web_image.content))
        i.save(output_file)
        counter += 1

        # break if come back to first page
        if next_link == first_link:
            os.system('cls')
            break
        else:
            link = next_link
