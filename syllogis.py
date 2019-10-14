#!/usr/bin/python3

"""syllogis.py: CLI driven tool to automate downloading research articles listed in url file"""

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2019"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPL v3.0"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Production"

import urllib.request as libreq
import shutil
import json
import datetime

# read configuration file for download dir and our url file
def read_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    return config

# read url file into collection
def read_urls(urls_file):  
    with open(urls_file) as urls_file:
        urls = json.load(urls_file)

    #for url in urls:
    now = datetime.datetime.now()
    today = now.strftime("%Y%m%d")

    return urls['urls'][today]

def download_pdf(urls, dir):
    iterator = 1

    for url in urls:
        link = url.replace('/abs/', '/pdf/')
        
        with libreq.urlopen(link) as response, open(dir + '/' + str(iterator) + '.pdf', 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

        iterator += 1

def main():

    config = read_config()
    url_file = config['url_file']['path'] + '/' + config['url_file']['name']
    download_dir = config['downloads']['path'] + '/' + config['downloads']['folder']
        
    urls = read_urls(url_file)
    
    download_pdf(urls, download_dir)


if __name__ == "__main__":
    main()