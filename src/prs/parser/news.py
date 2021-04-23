from requests_html import HTMLSession
from abc import ABC, abstractclassmethod
import re
from bs4 import BeautifulSoup
import requests
import lxml
import pprint as pp

SELECTORS = {
    "name":"body > div.s-wrapper > div > div > section > div > header > h1",
    #"phone":"body > div.popup-scrollable.m-rounded.m-500.active > div > div.scrollable-c > div:nth-child(1) > div > div:nth-child(1) > div > div.split-list-m > span",
    "address":"body > div.s-wrapper > div > div > section > div > div > div.company-card-info > ul > li:nth-child(1) > div > a",
    "site":"body > div.s-wrapper > div > div > section > div > div > div.company-card-info > ul > li:nth-child(4) > div > a",
    "description":"body > div.s-wrapper > div > div > section > div > header > div > p",
}

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}


class Parser(ABC):
    @abstractclassmethod
    def get_data(self):
        ...

    @abstractclassmethod
    def process_data(self):
        ...

    @abstractclassmethod
    def save_data(self):
        ...


class ParserLinks(Parser):
    _url = "https://tam.by/avto/arenda/page{}"

    def __init__(self, num_page):
        self._num_page = num_page
        self._links = []

    def active_page(self):
        try:
            pager = self.dom.find("div", class_="b-pagination")
            page = pager.find("li", class_="p-item")
            return self._num_page == int(page.get_text())

        except Exception:
            return False

    def get_data(self):
        response = requests.get(self._url.format(self._num_page), headers=HEADERS)
        if response.status_code == 200:
            self.dom = BeautifulSoup(response.text, "lxml")
        else:
            raise AttributeError(f"Error {response.status_code}")

    def process_data(self):
        if not self.active_page():
            raise AttributeError("The page {self._num_page} unavailable ")
        try:
            conteiner = self.dom.find("section", class_="b-section result-company-list")
            links = conteiner.find_all("a", class_="tam-card-whole-link")
        # link=case.find_all("a",class_="tam-card-whole-link")
        except AttributeError:
            raise AttributeError("Call method get_data()")
        self._links = [i["href"] for i in links]

    def save_data(self):
        pass

    @property
    def links(self):
        return self._links


class ParsInfo(Parser):
    def __init__(self, url):
        self._url = url
        self._info = {}

    def get_data(self):
        session = HTMLSession()
        response = session.get(self._url)
        if response.status_code == 200:
            self.dom=response.html
        else:
            raise AttributeError(f"Error status code {response.status_code}")
        
    def process_data(self):
        try:
            name=self.dom.find(SELECTORS['name'],first=True)
            address=self.dom.find(SELECTORS['address'],first=True)
            #phone=self.dom.find(SELECTORS['phone'])
            site=self.dom.find(SELECTORS['site'],first=True)
            description=self.dom.find(SELECTORS['description'],first=True)

        except AttributeError:
            raise AttributeError("Call method get_data()")

        self._info.update(name=name.text,
                        address=address.text,
                        site=site.text,
                        description=description.text,
                        url=self._url)

    
    @property
    def info(self):
        return self._info
        
    def save_data(self):
        pass


if __name__ == "__main__":
    parser_links = ParserLinks(1)
    parser_links.get_data()
    parser_links.process_data()
    info=ParsInfo(parser_links.links[0])
    info.get_data()
    info.process_data()
    pp.pprint(info.info)

    
