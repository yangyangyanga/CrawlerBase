import requests
from lxml import etree
import time

headers_base ={
    'Host':'www.douyu.com',
    'Referer':'https://www.douyu.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
}

def download_author(page_url):
    response = requests.get(page_url, headers=headers_base)
    text_html = etree.HTML(response.text)
    # text_name = text_html.xpath("//span[@class='dy-name ellipsis fl']/text()")
    # print(text_name)
    # text_click = text_html.xpath("//span[@class='dy-num fr']/text()")
    # print(text_click)
    # te_list = text_html.xpath("//ul[@id='live-list-contentbox']/li")
    # print(te_list)
    table = []
    # for li in te_list:
    text = text_html.xpath("//span[@class='dy-name ellipsis fl']/text() | //span[@class='dy-num fr']/text()")
    # print(text)
    pos = 0
    row = []
    for t in text:
        if pos < 2:
            row.append(t)
            if pos == 1:
                table.append(row)
            pos += 1
        else:
            row = []
            row.append(t)
            pos = 1
    for r in table:
        print(r)
        with open('auth.txt', 'a', encoding="utf-8") as f:
            for line in r:
                f.write(line+"  ")
                if r[-1] == line:
                    f.write('\n')
    print(len(table))



# ajax: 发送请求    - 接收数据
# 不同的是，并没有在浏览器的url中显示ajax发送请求的url
# 这时候，要通过抓包工具，来分析它的数据交互
# 最重要的，就是获取ajax提交请求的url

# https://www.douyu.com/directory/all?page=3&isAjax=1

for index in range(1, 9):
    douyu_url = "https://www.douyu.com/directory/all?page="+str(index)+"&isAjax=1"
    time.sleep(2)
    download_author(douyu_url)
