from requests_html import HTMLSession

session = HTMLSession()
links = ['https://movie.douban.com/subject/1292052/',
         'https://movie.douban.com/subject/1962665/',
         'https://movie.douban.com/subject/26752088/'
         ]

for link in links:
    r1 = session.get(link)
    # r1.html.render()
    title = r1.html.find('#content > h1 > span:nth-child(1)', first=True)
    year = r1.html.find('#content > h1 > span.year', first=True)
    print(title.text, year.text)
