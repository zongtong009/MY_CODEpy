# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


''' def get_url_list():
    response = requests.get(
        "http://www.interactivepython.org/courselib/static/pythonds/index.html")
    soup = BeautifulSoup(response.content, 'html.parser')
    div_list = soup.find('div', attrs={'class': 'toctree-wrapper compound'})
# print(div_list)
    a_s = div_list.find_all('a', attrs={'class': 'reference internal'})
    urls = []
    names = []
    for a in a_s:
        #    url = a['href']
        url = "http://interactivepython.org/courselib/static/pythonds/" + \
            a['href']
        name = a.get_text()
        urls.append(url)
        names.append(name)
    return urls, names


if __name__ == '__main__':
    urls, names = get_url_list()
    # path_wkthmltopdf = r'C:\wkhtmltopdf.exe'
    # config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    for i in range(len(urls)):
        print(i)
        pdfkit.from_url(urls[i], names[i]+'.pdf') '''
