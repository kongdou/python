import re
import urllib.request as request

# 京东读书页面
JD_URL = "https://channel.jd.com/1713-3259.html"
#BOOK_REGEX = re.compile('(https://item.jd.com/\d{8}.html)')

BOOKS_URL = []
# 找到每本书的链接地址
def getBooks():
    page = request.urlopen(JD_URL)
    data = page.read()
    print(data.decode('gbk'))
    page.close()
    r = re.findall(r'//item.jd.com/\d{8}.html',data.decode('gbk'))
    if r is not None: r(set)

# 多线程找到ISBN编码
if __name__ == '__main__':
    getBooks()