
import json
import time

import requests

from bs4 import BeautifulSoup

START_PAGE, END_PAGE, OUTPUT_FILE = 1, 10, 'words.json'

# Identify the URL
URL = "http://www.majortests.com/gre/wordlist_0%d"


def generate_urls(url, start_page, end_page):
    """
    This method takes a 'url' and returns a generated list of url strings

        params: a 'url', 'start_page' number and 'end_page' number
        return value: a list of generated url strings
    """
    urls = []
    for page in range(start_page, end_page):
        urls.append(url % page)
    return urls


def get_resource(url):
    """
    This method takes a 'url' and returns a 'requests.Response' object

        params: a 'url'
        return value: a 'requests.Response' object
    """
    return requests.get(url)


def make_soup(html_string):
    """
    This method takes a 'html string' and returns a 'BeautifulSoup' object

        params: html page contents as a string
        return value: a 'BeautifulSoup' object
    """
    return BeautifulSoup(html_string)


def get_words_from_soup(soup):

    """
    This method extracts word groups from a given 'BeautifulSoup' object

        params: a BeautifulSoup object to extract data
        return value: a dictionary of extracted word groups
    """

    words = {}
    count = 0

    for wordlist_table in soup.find_all(class_='wordlist'):

        count += 1
        title = "Group %d" % count

        new_words = {}
        for word_entry in wordlist_table.find_all('tr'):
            new_words[word_entry.th.text] = word_entry.td.text

        words[title] = new_words
        print " - - Extracted words from %s" % title

    return words


def save_as_json(data, output_file):
    """ Writes the given data into the specified output file"""
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)


def scrapper_bot(urls):
    """
    Scrapper bot:
        params: takes a list of urls

        return value: a dictionary of word lists containing
                      different word groups
    """

    gre_words = {}
    for url in urls:

        print "Scrapping %s" % url.split('/')[-1]

        # step 1
        # get a 'url'

        # step 2
        html = get_resource(url)

        # step 3
        # identify the desired pieces of data in the url using Browser tools

        #step 4
        soup = make_soup(html.text)

        # step 5
        words = get_words_from_soup(soup)

        gre_words[url.split('/')[-1]] = words

        print "sleeping for 5 seconds now"
        time.sleep(5)

    return gre_words

if __name__ == '__main__':

    urls = generate_urls(URL, START_PAGE, END_PAGE)

    gre_words = scrapper_bot(urls)

    save_as_json(gre_words, OUTPUT_FILE)
