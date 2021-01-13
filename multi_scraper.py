from random import randint
from time import sleep
import subprocess
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
from multiprocessing import Pool

#path to textfile containing links
path = "/path/to/links/"
with open(path+"main_links.txt", 'r') as file:
    data = file.read()
    
links = data.split("\n")

def scrape(url):
    headers = {"user-agent" : UserAgent().random}
    r = s.get(url, headers=headers)
    file = open(path+url.split("/")[-1]+".txt", "w") 
    file.write(r.text) 
    file.close()
    sleeptime = randint(3,5)
    sleep(sleeptime)
    
#Pool(number of parallel processes)
p = Pool(10)
p.map(scrape, links)

#end parallel processes
p.terminate()
p.join()
