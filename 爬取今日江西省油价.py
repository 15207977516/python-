import requests
from lxml import etree
import time

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
url = "http://youjia.chemcp.com/jiangxi/"
you = ["江西今日89号汽油价格:","江西今日92号汽油价格:","江西今日95号汽油价格:","江西今日0号柴油价格:"]

def Get_youjia(url,headers1):
    res = requests.get(url=url,headers=headers1,timeout=2).text
    s = etree.HTML(res)
    file = s.xpath('//*[@class="content"]/font/text()')
    for i in range(len(file)):
       print(time.strftime('%Y-%m-%d %H:%M:%S'), you[i], file[i])


if __name__ == "__main__":
    Get_youjia(url,headers)