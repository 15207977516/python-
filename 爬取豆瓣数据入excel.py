
from lxml import etree
import requests
import time
import xlwt
import xlrd

class doubanData(object):

    def __init__(self):
        self.f = xlwt.Workbook()#创建工作薄
        self.sheet1 = self.f.add_sheet(u"影片列表",cell_overwrite_ok=True)#命名table
        self.rowsTitle = [u"影片序号",u"影片链接",u"影片名称",u"影片评分",u"影片评价人数",u"经典评价"]#创建标题
        for i in range(0,len(self.rowsTitle)):
            self.sheet1.write(0,i,self.rowsTitle[i],self.set_style("Times new Roman",220,True))#设置参数样式
            self.f.save('F:/text/爬虫/豆瓣数据表.xls')#保存位置
    def set_style(self,name,height,bold=False):
        style = xlwt.XFStyle()#初始化样式
        font = xlwt.Font()#为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style
    def getUrl(self):
        for a in range(10):
            url = 'https://movie.douban.com/top250?start={}'.format(a * 25)
            self.spiderPage(url)

    def spiderPage(self, url, content=None):
        if url is None:
            return None

        try:
            data = xlrd.open_workbook('F:/text/爬虫/豆瓣数据表.xls')#打开excel文件
            table = data.sheets()[0]#通过索引顺序获取table
            rowCount = table.nrows
           # proxies = {"http":"http://110.73.1.47:8123"}
            header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
            respon = requests.get(url,headers = header)#获取响应
            htmlText=respon.text#打印html内容
            s = etree.HTML(htmlText)#将源码转化为能被XPath匹配的格式
            trs = s.xpath('//*[@id="content"]/div/div[1]/ol/li')#提取相同的前缀
            m = 0
            for tr in trs:
                data = []
                moviesHref = tr.xpath('./div/div[2]/div[1]/a/@href')[0]
                moviesTitle=tr.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
                moviesScore=tr.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
                moviesPeople=tr.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0].strip("(").strip().strip(")")
                moviesScrible =tr.xpath('./div/div[2]/div[2]/p[2]/span/text()')


                #拼装成一个列表
                data.append(rowCount+m)#增加序号
                data.append(moviesHref)
                data.append(moviesTitle)
                data.append(moviesScore)
                data.append(moviesPeople)
                data.append(moviesScrible)

                for i in range(len(data)):
                    self.sheet1.write(rowCount+m,i,data[i])#写入数据到excel

                m+=1 #记录行数增量
                print(m)
                print(moviesHref,moviesTitle,moviesScore,moviesPeople,moviesScrible)

        except Exception as e:
            print("出错",type(e),e)

        finally:
            self.f.save('F:/text/爬虫/豆瓣数据表.xls')

if '_main_':
    dbmovies = doubanData()
    dbmovies.getUrl()







