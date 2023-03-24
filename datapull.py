from bs4 import BeautifulSoup
import requests
import os
from os import path
import sys
from PIL import Image

def geog_location(url):
    lat_long = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    # provides info on coordinates for each round
    for x in eval(str(soup).split('"rounds":[')[1].split(']')[0]):
        lat_long.append(str(x['lat'])+','+str(x['lng'])+','+x['streakLocationCode'])
        
    # how screenshots are automatically labelled upon being taken
    screenshot_list = ['screenshot.png','screenshot 1.png','screenshot 2.png','screenshot 3.png','screenshot 4.png']
    # screenshot folder
    old_path = '/Users/emmakrentz/Downloads/screenshots/'
    # cleaned image folder
    new_path = '/Users/emmakrentz/Downloads/geoguessr data/'
    
    # crop images to correct geoguessr image size
    # rename each screenshot with its location coordinates, then move out of screenshot folder and into cleaned folder
    for y in range(5):
        old_file = screenshot_list[y]
        new_file = lat_long[y]+'.png'
        im = Image.open(old_path+old_file)
        imCrop = im.crop((0, 272, 2880, 1626)) #corrected
        imCrop.save(new_path + new_file, "PNG", quality=100)
        os.remove(old_path+old_file)
