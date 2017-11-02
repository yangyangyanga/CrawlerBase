import requests
from lxml import etree
import time

headers_base = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
}
def dowload_img(page_url):
    response = requests.get(page_url, headers=headers_base)
    img_html = etree.HTML(response.text)
    img_urllist = img_html.xpath('//img[@class="sell_img"]/@src')
    print(img_urllist)
    # print(len(img_urllist))
    for per_img_url in img_urllist:
        res = requests.get(per_img_url, headers=headers_base)
        picname = per_img_url.rsplit('/')[-1]
        print(picname)
        with open('D:/pycharm/project13/day03/down/' + picname, 'wb') as f:
            f.write(res.content)

def page_index():
    for index in range(1, 10):
        # http: // www.gandianli.com / sell / list.php?catid = & page = 2 & price = 0 & thumb = 0 & vip = 0 & day = 0 & order = & list = 1
        page_url = "http://www.gandianli.com/sell/list.php?catid=&page=" + str(index) + "&price=0&thumb=0&vip=0&day=0&order=&list=1"
        time.sleep(2)
        dowload_img(page_url)

page_index()
