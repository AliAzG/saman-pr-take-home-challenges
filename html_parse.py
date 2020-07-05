import glob
import os.path
from bs4 import BeautifulSoup
import json

#**Write a script that parses the HTML files in that directory, extracts the artist names and outputs a JSON array of the unique names to stdout.**

def data_extractor_step1():
    artist_list = []
    dir_path = r"./lot-parser/data/2015-03-18"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split = title.strip().split(":")[0]
        print(30*"#", title.strip().split(":")[1])
        artist_list.append(artist_split)
    return json.dumps(artist_list, ensure_ascii=False)
#print(data_extractor_step1())

def data_extractor_step2():
    artist_list = []
    dir_path = r"./lot-parser/data/2015-03-18"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split, works = title.strip().split(":", 1)
        #works = title.split(":")[1].strip()
        art_work_dict = {"artist": artist_split, "works": [works.strip()]}
        artist_list.append(art_work_dict)
    return json.dumps(artist_list, ensure_ascii=False)
#print(data_extractor_step2())