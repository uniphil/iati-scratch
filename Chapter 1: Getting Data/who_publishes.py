#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    scraper
    ~~~~~~~

    This script crawls the iatiregistry publishers listings, and pings each
    publisher's website to see if everything is on the up-and-up.

    Doing so is tricky and messy. I can't find any outbound links to publisher
    websites, so we find email addresses and look at their domains.


    run the boring way

        $ ./scraper.py

    run with four threads:
    
        $ ./scraper.py threads

    run with n threads:
    
        $ ./scraper.py threads 8

    multiprocess

        $ ./scraper.py procs 2
"""

import os
import pickle
from functools import wraps
from base64 import urlsafe_b64encode as encode
import logging as log
import requests
from bs4 import BeautifulSoup

REG_BASE = 'http://www.iatiregistry.org'
URLS = dict(
    PUBLISHERS='/publisher',
    DATASET='/dataset'
)

_py_map = map


def filecache(f):
    if 'cache' not in os.listdir('.'):
        os.makedirs('cache')
    folder = f.__name__
    if folder not in os.listdir('cache'):
        os.makedirs(os.path.join('cache', folder))
    @wraps(f)
    def wrapped(*args, **kwargs):
        cache_name = encode(unicode(args))
        try:
            with open(os.path.join('cache', folder, cache_name), 'rb') as cached:
                response = pickle.load(cached)
                print('hit')
        except IOError:
            response = f(*args, **kwargs)
            with open(os.path.join('cache', folder, cache_name), 'wb') as cache:
                pickle.dump(response, cache)
                print('miss')
        return response
    return wrapped


@filecache
def grab_from_reg(relative_url):
    resp = requests.get(REG_BASE + relative_url)
    return resp.content


def get_publishers():
    resp = grab_from_reg(URLS['PUBLISHERS'])
    primary = BeautifulSoup(resp).article
    for row in primary.tbody.tr.next_siblings:
        if not row.name:
            continue
        yield {'name': unicode(row.a.string), 'link': row.a.get('href')}


def get_dataset_links(publisher_resp):
    publisher_primary = BeautifulSoup(publisher_resp)
    dataset_list = publisher_primary.find(class_='dataset-list')
    if dataset_list is not None:
        for row in dataset_list.li.next_siblings:
            if not row.name:
                continue
            title = unicode(row.h3.a.string)
            link = row.find_all('p')[-1].a.get('href')
            yield {'title': title, 'link': link}


@filecache
def get_dataset_meta(link):
    meta = grab_from_reg(link['link'])
    meta_primary = BeautifulSoup(meta)
    email = unicode(meta_primary.find('aside', class_='secondary').dl.dd.string)
    print(link['title'], email)
    return {'title': link['title'], 'email': email}


def get_publisher_dataset(publisher):
    """dataset pages have contact emails which we use to find the website"""
    publisher_resp = grab_from_reg(publisher['link'])
    links = get_dataset_links(publisher_resp)
    info = _py_map(get_dataset_meta, links)
    return {'publisher': publisher['link'], 'datasets': info}


@filecache
def scrape(map):
    print('getting publishers...')
    publishers = get_publishers()
    print('getting datasets...')
    datasets = map(get_publisher_dataset, publishers)
    return datasets


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'threads':
            from multiprocessing.dummy import Pool
        elif sys.argv[1] == 'procs':
            from multiprocessing import Pool
        else:
            print(__doc__)
            raise SystemExit(1)

        n = 4  # default

        if len(sys.argv) > 2:
            try:
                n = int(sys.argv[2])
            except ValueError:
                print(__doc__)
                raise SystemExit(1)

        pool = Pool(n)
        map = pool.map  # global redefine

    scrape(map)
