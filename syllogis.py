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

# read configuration file for download dir and our url file
def read_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    return config

# read url file into collection
def read_urls(urls_file):
    with open(urls_file) as urls_file:
        urls = json.load(urls_file)

    return urls

def download_pdf(urls, dir):
    for url in urls:
        link = url.replace('/abs/', '/pdf/')

        # need to replace open() with filename
        with libreq.urlopen(link) as response, open('1910.04872.pdf', 'wb') as out_file:
            shutil.copyfileobj(response, out_file)


    #url = 'https://arxiv.org/abs/1910.04872'
    #link = url.replace('/abs/', '/pdf/')

    #with libreq.urlopen("https://arxiv.org/pdf/1910.04872") as response, open('1910.04872.pdf', 'wb') as out_file:
    #    shutil.copyfileobj(response, out_file)


def main():
    config = read_config()
    url_file = config['url_file']['path'] + '/' + config['url_file']['name']
    download_dir = config['downloads']['path'] + '/' + config['downloads']['folder']
    
    #print(download_dir)
    
    urls = read_urls(url_file)
    print(urls)
    #download_pdf(urls)


if __name__ == "__main__":
    main()