from urllib.request import urlopen
from bs4 import BeautifulSoup
from word import *


class LatdictWrapper:

    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.letterURL = 'http://www.latin-dictionary.net/list/letter/'
        self.defineURL = 'http://www.latin-dictionary.net/definition/'
        self.searchURL = 'http://www.latin-dictionary.net/search/latin/'

    def search_word(self, word, results=1):
        search_page = urlopen(self.searchURL + word)
        search_page = BeautifulSoup(search_page, 'html.parser')
        search_page = search_page.find(id="pager-pager-top")
        lst = []
        if hasattr(search_page, 'p'):
            pages = ''.join(
                [i for i in str(search_page).split('<strong>')[2] if i.isdigit()])
            words = ''.join(
                [i for i in str(search_page).split('<strong>')[3] if i.isdigit()])
        else:
            pages = 1
        for i in range(int(pages)):
            lst += self.process_url(self.searchURL + word + '/' + str(i + 1))
            if len(lst) > results:
                break
        return lst[:results]

    def fetch_letter(self, letter):
        letter_page = urlopen(self.letterURL + letter[0])
        letter_page = BeautifulSoup(letter_page, 'html.parser')
        letter_page = [i.get('href') for i in letter_page.find_all('a')[35:-8]]
        print("Fetched all '" + letter + "' words.")
        return letter_page

    def fetch_all(self):
        lst = []
        for letter in self.alphabet:
            lst.append(self.fetch_letter(letter))

    def process_url(self, url):
        word_page = urlopen(url)
        word_page = BeautifulSoup(word_page, 'html.parser')
        entries = word_page.find_all("div", class_="entry")
        lst = []
        for entry in entries:
            part = str(entry).split("entry-content")[1]
            part = str(part).split("</p>")[0]
            part = str(part).split(">")[2]
            part = part.lower()
            if part == 'noun':
                lst.append(Noun(entry))
            elif part == 'adjective':
                lst.append(Adjective(entry))
            elif part == 'verb':
                lst.append(Verb(entry))
            elif part == 'preposition':
                lst.append(Preposition(entry))
            else:
                lst.append(Word(entry))
        return lst
