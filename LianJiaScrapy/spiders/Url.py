import time
# coding:utf8
import requests
from bs4 import BeautifulSoup

url = 'http://sh.lianjia.com'
urllist = []
def get_s_reion(url):
    '''
    取该城市区域列表
    :param list: 链接list
    :return:
    '''
    try:
        list = []
        html = requests.get(url + '/ershoufang').text
        soup = BeautifulSoup(html, 'html.parser')
        reions = soup.select('div.position')[0].select('div')[0].select('a')
        # reions = soup.select('div.m-filter')[0].select('div[data-role="ershoufang"]')[0].select('a')[1:]
        for reion in reions:
            city_href = url + reion.get('href')
            list.append(city_href)
        return list
    except:
        pass

def get_url_s(url, html_city):
    '''
    取二级区域列表（镇、乡）
    :param url:
    :param html_city:
    :return: 链接list
    '''
    try:
        gethtml = []
        get1 = []
        html = requests.get(html_city)
        respons = html.content
        soup = BeautifulSoup(respons, 'html.parser')
        d = soup.select('div.m-filter')[0].select('div[data-role="ershoufang"]')[0].select('div')[1].select('a')
        for d2 in d:
            diqu = d2.text
            href = d2.get('href')
            get1.append(str(href))
        for i in range(1, len(get1)):
            html = url + get1[i]
            gethtml.append(html)
        return gethtml
    except:
        pass

def Get_url_s(url):
    '''
    取某二级区域页面的房子页数及每页链接
    :param url:
    :return: 各页码链接list
    '''
    list = []
    html = requests.get(url)
    respons = html.content
    try:
        try:
            soup = BeautifulSoup(respons, 'html.parser')
            num = int(soup.select('h2[class="total fl"]')[0].select('span')[0].text.strip())
        except:
            pass
        alist = int(num / 30 + (1 if num % 30 != 0 else 0))
        for i in range(1, alist + 1):
            list.append('%spg%s' % (url, i))
        return list
    except:
        pass

if __name__ == '__main__':
    lists = get_s_reion(url)
    if lists != None:
        for list in lists:
            htmls = get_url_s(url, list)
            if htmls != None:
                for html in htmls:
                    Citys = Get_url_s(html)
                    for city in Citys:
                        urllist.append(city)
    for i in urllist:
        print(i)

