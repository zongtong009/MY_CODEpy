from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://movie.douban.com/subject/1292052/')
title = r.html.find('#content > h1 > span:nth-child(1)', first=True)
# r.html.find() 接受一个 CSS 选择器（字符串形式）作为参数
# 返回在网页中使用该选择器选中的内容。

print(title.text)
# app > div > div > div.container > div:nth-child(6) > div:nth-child(5) > div > h1 > b


htm = '''
<div class="content">
  <h3><b>理解网页结构</b></h3>
  <p>我们所看到的所有网站都是由 <b>结构化</b> 的代码构成的，经过浏览器的处理，呈现出各式各样的页面。</p>
  <p>一个网页通常由三部分代码组成：HTML 代码、CSS 代码 和 Javascript 代码。</p>
  <p>下面的文本框中是现在你看到的这段文字背后的代码，尝试进行以下操作：</p>
</div>
'''
