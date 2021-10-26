import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse


class Game:
    def __init__(self, game, store, link):
        self.game = game
        self.store = store
        self.link = link


# the following function removes the HTML content and return the value inside the HTML tags
def parser(content):
    result = []
    for i in content:
        result.append(i.text)
    return result


# the following function extracts the href attribute content from a tags from HTML
def link_getter(content):
    result = []
    for i in content:
        result.append(i['href'])
    return result


# the following function gets the domain of a given link and removes the unwanted stuff such as 'http' and parameters
def link_parser(content):
    result = []
    for i in content:
        url_info = urlparse(i)
        domain = url_info.netloc
        result.append(domain)
    return result


# remove 'WWW' and domain name (.com/.co/.org/.uk/...) from the links:
def link_cleaner(content):
    for i in range(len(content)):
        content[i] = content[i].replace('www.', '')
        if content[i][-4] == '.':
            content[i] = content[i][:-4]
        else:
            content[i] = content[i][:-3]
    return content


page = requests.get('https://gamesfree.today/')

source = page.content

soup = BeautifulSoup(source, 'lxml')

games_inner = soup.find_all(
    'h3', class_='my-1 text-lg font-bold md:my-0 md:py-1')

links_inner = soup.find_all(
    'a', class_="w-10/12 px-5 py-3 m-auto text-lg text-center text-white no-underline transition transform "
                "bg-yellow-600 rounded-lg md:w-11/12 hover:bg-yellow-700 md:text-base")

games = parser(games_inner)

full_links = link_getter(links_inner)

site = link_getter(links_inner)
site = link_parser(site)
site = link_cleaner(site)

data = []

for i in range(len(games)):
    data.append(Game(games[i], site[i], full_links[i]))
