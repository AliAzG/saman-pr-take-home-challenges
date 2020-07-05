import glob
import os.path
from bs4 import BeautifulSoup
import json
import argparse
#**Write a script that parses the HTML files in that directory, extracts the artist names and outputs a JSON array of the unique names to stdout.**

def data_extractor_step1():
    artist_list = []
    dir_path = r"./lot-parser/data/2015-03-18"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split = title.strip().split(":")[0]
        artist_list.append(artist_split)
    print(json.dumps(artist_list, ensure_ascii=False))
#print(data_extractor_step1())

#**Modify your script to extract the title of the work as well. Modify your output format to be an array of objects.**
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
    print(json.dumps(artist_list, ensure_ascii=False))
#print(data_extractor_step2())

#**Modify your script yet again, extracting the price realized and including it alongside the works.**
def data_extractor_step3():
    artist_list = []
    dir_path = r"./lot-parser/data/2015-03-18"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split, works = title.strip().split(":", 1)
        all_divs = soup.find_all('div')
        price = all_divs[1].text
        #works = title.split(":")[1].strip()
        art_work_dict = {"artist": artist_split, "works": [{"title": works.strip(), "price": price}]}
        #print(art_work_dict)
        artist_list.append(art_work_dict)
    print(json.dumps(artist_list, ensure_ascii=False))
#print(data_extractor_step3())

#**Modify your script one more time, separating the currency from the amount.**

def data_extractor_step4():
    artist_list = []
    dir_path = r"./lot-parser/data/2015-03-18"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split, works = title.strip().split(":", 1)
        all_divs = soup.find_all('div')
        price = all_divs[1].text
        currency, amount = price.split(' ')
        #amount = price.split(' ')[1]
        #works = title.split(":")[1].strip()
        art_work_dict = {"artist": artist_split, "works": [{"title": works.strip(), "currency": currency, "amount": amount}]}
        #print(art_work_dict)
        artist_list.append(art_work_dict)
    print(json.dumps(artist_list, ensure_ascii=False))

#print(data_extractor_step4())

#**Write a script that parses the HTML files in that directory, extracts the artist names and outputs a JSON array of the unique names to stdout for 2017-12-20 directory.**

def data_extractor_step5():
    artist_list = []
    dir_path = r"./lot-parser/data/2017-12-20"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split = title.strip().split(":")[0]
        artist_list.append(artist_split)
    print(json.dumps(artist_list, ensure_ascii=False))
#print(data_extractor_step5())

#**Modify your script to extract the title of the work as well. Modify your output format to be an array of objects for 2017-12-20 directory.**
def data_extractor_step6():
    artist_list = []
    dir_path = r"./lot-parser/data/2017-12-20"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split, works = title.strip().split(":", 1)
        art_work_dict = {"artist": artist_split, "works": [works.strip()]}
        artist_list.append(art_work_dict)
    print(json.dumps(artist_list, ensure_ascii=False))
#print(data_extractor_step6())

#**Modify your script yet again, extracting the price realized and including it alongside the works for 2017-12-20 directory.**
def data_extractor_step7():
    artist_list = []
    dir_path = r"./lot-parser/data/2017-12-20"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split, works = title.strip().split(":", 1)
        all_divs = soup.find_all('div')
        price = all_divs[1].text
        #works = title.split(":")[1].strip()
        art_work_dict = {"artist": artist_split, "works": [{"title": works.strip(), "price": price}]}
        #print(art_work_dict)
        artist_list.append(art_work_dict)
    print(json.dumps(artist_list, ensure_ascii=False))
#print(data_extractor_step7())

#**Modify your script one more time, separating the currency from the amount for 2017-12-20 directory.**

def data_extractor_step8():
    artist_list = []
    dir_path = r"./lot-parser/data/2017-12-20"
    for file_name in glob.glob(os.path.join(dir_path, "*.html")):
        with open(file_name) as html_file:
            soup = BeautifulSoup(html_file, features="lxml")
        title = soup.find('title').get_text()
        artist_split, works = title.strip().split(":", 1)
        all_divs = soup.find_all('span')
        amount = all_divs[1].text
        currency = soup.find('span', {'class': 'currency'}).get_text()
        art_work_dict = {"artist": artist_split, "works": [{"title": works.strip(), "currency": currency, "amount": amount}]}
        artist_list.append(art_work_dict)
    print(json.dumps(artist_list, ensure_ascii=False))

#print(data_extractor_step8())
parser = argparse.ArgumentParser()
FUNCTION_MAP = {'step1': data_extractor_step1, 'step2': data_extractor_step2,
                'step3': data_extractor_step3, 'step4': data_extractor_step4,
                'step5': data_extractor_step5, 'step6': data_extractor_step6,
                'step7': data_extractor_step7, 'step8': data_extractor_step8}
parser.add_argument('command', choices=FUNCTION_MAP)
args = parser.parse_args()

func = FUNCTION_MAP[args.command]
func()