from distutils.log import info
from requests_html import HTMLSession

class Scrapper():
    def scrapedata(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        session = HTMLSession()
        r = session.get(url)
        print(r.status_code)
        quotes_list = []
        quotes = r.html.find('div.quote')
        
        for q in quotes:
            item = {
                'text' : q.find('span.text', first = True).text.strip(),
                'Author' : q.find('small.author', first = True).text.strip()
                #'Details' : q.find('a.href', first = True).text.strip()
            }
            print(item)
            quotes_list.append(item)
        return quotes_list

#session = HTMLSession()
#r = session.get('https://quotes.toscrape.com/')
quotes = Scrapper()
quotes.scrapedata('life')