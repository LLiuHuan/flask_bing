# -*- coding: utf-8 -*-
import requests
import shutil
import os
from bs4 import BeautifulSoup
import re
import time
import pymysql

conn = pymysql.connect(host="49.233.178.154", user="root", password="LLiuHuan980724.", database="bing", charset="utf8")
cursor = conn.cursor()


def addslashes(s):
    d = {'"': '\\"', "'": "\\'", "\0": "\\\0", "\\": "\\\\"}
    return ''.join(d.get(c, c) for c in s)


def parse_page(url):
    """
    根据 url 下载页面并转换成 soup 对象
    :param url: 页面 url 链接
    :return: soup 对象
    """
    page = requests.get(url).content
    return BeautifulSoup(page, 'html.parser')


def parse_page_num(soup):
    """
    解析页面，返回总页数
    :param soup: 页面 soup 对象
    :return: 总页数
    """
    total_page_num = 0
    page_div = soup.find('div', attrs={'class': 'page'})
    if page_div and page_div.span:
        page_span_str = page_div.span.string
        page_num_list = page_span_str.split(' / ')
        if len(page_num_list) == 2:
            total_page_num = int(page_num_list[1])
    return total_page_num


def parse_pic_names(soup):
    """
    解析页面，返回当前页面图片名
    :param soup: 页面 soup 对象
    :return: 图片名称列表
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

    pic_img_list = soup.find_all('img', attrs={'class': 'progressive__img progressive--not-loaded'})
    pic_h3_list = soup.find_all('h3')
    pic_em_list = soup.find_all('em', attrs={'class': 't'})
    ii = 0
    for i in range(len(pic_img_list)):
        copyright = re.search(r'<h3>(.*?)</h3>', str(pic_h3_list[i]))
        copyright = copyright.group(1)
        while True:
            try:
                newdate = re.search(r'<em class="t">(.*?)</em>', str(pic_em_list[(ii)]))
                newdate = newdate.group(1)
                str_time = time.localtime(time.mktime(time.strptime(newdate, "%Y-%m-%d")) - 24 * 60 * 60)
                ii += 1
                break
            except Exception as e:
                # print()
                ii += 1
        # print(str_time)
        startdate = time.strftime("%Y%m%d", str_time)
        enddate = ''.join(newdate.split('-'))
        fullstartdate = enddate + '1600'
        img = enddate + '.jpg'
        img_stream = requests.get(str(pic_img_list[i]['data-progressive']), stream=True, headers=headers)
        if img_stream.status_code == 200:
            with open('/data/www/images/' + img, 'wb') as fw:
                shutil.copyfileobj(img_stream.raw, fw)
        sql = "insert into bingImg(copyright, startdate, fullstartdate, enddate, imgUrl, addTime, http, bot, drk, title, top, wp, hs, url, hsh, copyrightlink) values "
        sql += " ('%s', '%s', '%s', '%s', '%s', '%s', 'https://cn.bing.com', '1', '1', '', '1', 'True', '[]', '', '', '')" % (
            addslashes(copyright), startdate, fullstartdate, enddate, addslashes(os.getcwd() + '\\' + img),
            newdate + ' 00:00:01'
        )
        # print(sql)
        cursor.execute(sql)
        conn.commit()


def main():
    """ 爬虫主函数 """
    print('---------- Crawling Start ----------')
    base_page_url = 'https://bing.ioliu.cn'
    # base_pic_url = 'http://h1.ioliu.cn/bing/%s_%s.jpg'
    all_pic_names = []
    # 下载页面并转换成 soup 对象
    soup = parse_page(base_page_url)
    # 获取总页数
    total_page_num = parse_page_num(soup)
    for page in range(total_page_num):
        print('Processing page: %s' % (page + 1))
        page_url = base_page_url + '/?p=' + str(page + 1)
        soup = parse_page(page_url)
        # 获取当前页面所有图片名
        parse_pic_names(soup)
        # all_pic_names.extend(pic_names)

    # 图片爬取结束
    print('---------- Crawling End ----------')
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
