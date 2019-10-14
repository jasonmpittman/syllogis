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
def read_urls():
    with open('urls.json') as urls_file:
        urls = json.load(urls_file)

    return urls

def download_pdf():
    url = 'https://arxiv.org/abs/1910.04872'
    link = url.replace('/abs/', '/pdf/')

    #with libreq.urlopen("https://arxiv.org/pdf/1910.04872") as response, open('1910.04872.pdf', 'wb') as out_file:
    #    shutil.copyfileobj(response, out_file)







