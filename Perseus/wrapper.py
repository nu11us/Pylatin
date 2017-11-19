from urllib.request import urlopen
from bs4 import BeautifulSoup
from book import Book

class PerseusWrapper:

    def __init__(self):
        self.BookURL = 'http://www.perseus.tufts.edu/hopper/collection?collection=Perseus%3Acorpus%3Aperseus%2CLatin%20Texts'

    def get_books(self):        
        books = urlopen(self.BookURL)
        books = str(books.read())
        soup = BeautifulSoup(books, 'html.parser')
        links = soup.findAll("a", { "class" : "aResultsHeader" })
        formatted_links = {}
        for link in links:
            formatted_links[link.get_text()] = link.get('href')[9:]
        return formatted_links

    def load_book(self,code):
        if 'Perseus' not in code:
            books = self.get_books()
            code = books[code]          
        load = Book(code)
        return load

x = PerseusWrapper()
x.load_book('Aeneid')

