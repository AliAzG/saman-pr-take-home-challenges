import glob
import os.path
from bs4 import BeautifulSoup
import json

def data_extractor():
    artist_list = []
    dir_path = r"./lot-parser/data/2015-03-18"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split = title.strip().split(":")[0]
        artist_list.append(artist_split)
    return json.dumps(artist_list, ensure_ascii=False)

print(data_extractor())
#a = open('./lot-parser/data/2015-03-18/lot4.html').read()