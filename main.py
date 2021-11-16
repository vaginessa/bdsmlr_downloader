from scraping import scraping
from parsing import parse
import os, time, requests

EMAIL = ""
PW = ""

def download_shit(urls):
    for url in urls:
        filename = url.split('/')[-1]
        with open( 'stuff/' + filename, 'wb') as f:
            r = requests.get(url)
            f.write(r.content)

blog = input("blog: ")
pages = input("max pages: ")

scrp = scraping()
scrp.login(EMAIL, PW)
time.sleep(2)
prs = parse(scrp.blog(2, blog))
download_shit(prs.get_imgs())
