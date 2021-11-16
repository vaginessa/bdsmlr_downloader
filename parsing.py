from bs4 import BeautifulSoup

class parse:
    def __init__(self, source):
        self.soup = BeautifulSoup(source, 'html.parser')

    def get_imgs(self):
        mags = self.soup.find_all('a', class_='magnify')
        urls = [a['href'] for a in mags]
        return urls