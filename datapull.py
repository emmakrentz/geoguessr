# function to parse metadata from a geoguessr game and automatically label game screenshots with their latitude-longitude coordinates 
# process: play game of geoguessr, manually screenshot each location, copy game url, run script
# each image is cropped, resized, labelled with its coordinates and country codes, moved to cleaned data folder for analysis


# import packages
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
    new_path = '/Users/emmakrentz/Downloads/data science practice/geoguessr/geoguessr data/'
    # resizing images at 2% original size for analysis
    resized_path1 = '/Users/emmakrentz/Downloads/data science practice/geoguessr/resized data (58,27)/'
    # resizing images at 4% original size for analysis
    resized_path2 = '/Users/emmakrentz/Downloads/data science practice/geoguessr/resized data (115,54)/'
    
    # crop images to correct geoguessr image size
    # rename each screenshot with its location coordinates, then move out of screenshot folder and into cleaned folder
    for y in range(5):
        old_file = screenshot_list[y]
        new_file = lat_long[y]+'.png'
        im = Image.open(old_path+old_file)
        imCrop = im.crop((0, 272, 2880, 1626)) # removes header and taskbar, leaving only image
        imCrop.save(new_path + new_file, "PNG", quality=100)
        os.remove(old_path+old_file) # remove files from screenshots folder
    # create new file folder with images at 2% and 4% the size for analysis
        imCrop.resize((58,27)).save(resized_path1 + new_file, "PNG")
        imCrop.resize((115,54)).save(resized_path2 + new_file, "PNG")
