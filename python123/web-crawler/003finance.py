from requests_html import HTMLSession

session = HTMLSession()
links = ['http://stock.finance.sina.com.cn/usstock/quotes/aapl.html',
         'http://stock.finance.sina.com.cn/usstock/quotes/bidu.html',
         'http://stock.finance.sina.com.cn/usstock/quotes/msft.html'
         ]

for link in links:
    r1 = session.get(link)
    r1.html.render()
    shares = r1.html.find('#hqPrice', first=True)
    print(shares.text)
