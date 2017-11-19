from urllib.request import urlopen
from bs4 import BeautifulSoup

class Book:
    def __init__(self,code):
        url = 'http://www.perseus.tufts.edu/hopper/xmltoc?doc=' + code
        self.XML = urlopen(url)
        self.XML = self.XML.read()
        soup = BeautifulSoup(self.XML,'lxml-xml')
        chunks = soup.find_all('chunk')
        types = []
        self.section_dict = {}
        for i in chunks:
            types.append(i.get('type'))
        for i in chunks:
            tup = (i.parent.head.get_text(),i.head.get_text())
            self.section_dict[tup]= i.get('ref')
