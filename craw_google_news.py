import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


class Crawler(object):

    def __init__(self):
        self.col = ['title', 'timestamp', 'source', 'URL']
        self.df = pd.DataFrame(columns=self.col)
        self.url = 'https://news.google.com'
        par = {'hl': 'zh-TW', 'gl': 'TW', 'ceid': 'TW:zh-Hant'}
        res = requests.get(self.url, params=par)
        sp = BeautifulSoup(res.text, 'html.parser')
        self.al = sp.findAll('article', {'class': re.compile('EjqUne')})

    def crawler(self):
        for i in self.al:
            herf_ = self.url + i.find('a')['href'][1:]
            where = i.findAll('a')[-1].text
            if i.find('time'):
                time_ = i.find('time')['datetime']
            else:
                time_ = 'no timestamp'
            if i.find('h3'):
                title = i.find('h3').text
            else:
                title = i.find('h4').text
            self.record(title, time_, where, herf_)
        self.df.to_csv('google_news.csv')

    def record(self, title, time_, where, herf_):
        df2 = pd.DataFrame([[title, time_, where, herf_]], columns=self.col)
        self.df = self.df.append(df2, ignore_index=True)


if __name__ == "__main__":
    c = Crawler()
    c.crawler()
