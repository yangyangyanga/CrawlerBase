import requests
from lxml import etree
import time
import json

headers = {
    'Host':'www.qianmu.org',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
}

# 获得每个学校的链接
def get_school_url(qianmu_url):
    res = requests.get(qianmu_url, headers=headers)
    # print(res.text)
    reshtml = etree.HTML(res.text)
    school_url = reshtml.xpath("//div[@id='content']/table/tbody/tr/td[2]/a/@href")
    # print(school_url)
    return school_url

# get_school_url('http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D')

# 获取每个学校的一些基本信息
# 学校名   地址  本科生人数   研究生人数    师生比    国际学生比例    网址
def get_school_message():
    # 每个学校存为一个字典
    all_schooldict = {}
    error = 0   # 错误的学校次数
    school_url_list =  get_school_url('http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D')
    for school_url_index in range(800):
        try:
            school_res = requests.get(school_url_list[school_url_index], headers=headers)
            school_html = etree.HTML(school_res.text)
            # 学校基本信息存入一个字典
            schooldict = {}
            schoolname = school_html.xpath("//h1[@class='wikiTitle']/text()")
            # print("schoolname=",schoolname[0])
            # 加入学校名
            schooldict["schoolname"] = schoolname[0]
            # 表格全部内容
            namelist = school_html.xpath("//div[@class='infobox']/table/tbody/tr/td[1]/p/text() | //div[@class='infobox']/table/tbody/tr/td[2]/p[1]/text() | //div[@class='infobox']/table/tbody/tr/td[2]/p/a/text()")
            print(namelist)
            # print(len(namelist))

            address = ''
            benke = ''
            yanjiu = ''
            shishengbi = ''
            nastu = ''
            schoolnet = ''
            for index in range(len(namelist)):
                if namelist[index] in ['国家', '州省', '城市']:
                    address += namelist[index+1]
                elif namelist[index] == '本科生人数':
                    benke += namelist[index+1]
                elif namelist[index] == '研究生人数':
                    yanjiu += namelist[index+1]
                elif namelist[index] == '师生比':
                    shishengbi += namelist[index+1]
                elif namelist[index] == '国际学生比例':
                    nastu += namelist[index+1]
                elif namelist[index] == '网址':
                    schoolnet += namelist[index+1]
            # 加入地址  本科生人数   研究生人数    师生比    国际学生比例    网址
            schooldict['address'] = address
            schooldict['benke'] = benke
            schooldict['yanjiu'] = yanjiu
            schooldict['shishengbi'] = shishengbi
            schooldict['nastu'] = nastu
            schooldict['schoolnet'] = schoolnet

            for key, value in schooldict.items():
                print(key, "===", value)
            print("-------------------------------------------")
            all_schooldict[str(school_url_index)] = schooldict
            time.sleep(1)
        except:
            error += 1
            pass
    with open(r'D:\pycharm\project13\day03\qianmuwang\school1.json', 'a', encoding='utf-8') as f:
        json.dump(all_schooldict, f)
    print("失败次数：%d"%error)

if  __name__ == "__main__":
    get_school_message()

