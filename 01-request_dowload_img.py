import requests

headers_base = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
}

# 提交图片url请求
response = requests.get('http://www.gandianli.com/file/upload/201610/27/1552087363.png.thumb.png',
                        headers=headers_base)

print(response.text)

# 新建打开一个文件
# 将响应数据以二进制方式写入文件
with open('pic.jpg', 'wb') as f:
    f.write(response.content)