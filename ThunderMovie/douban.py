# encoding: utf-8
import httplib2
from urllib.parse import urlencode
import json
import random
import string
import time


class douban:
    '''
    获取电影 豆瓣信息
    '''

    def get_film_douban_id(self, name, year):
        '''
        获取电影ID
        :return: 豆瓣id
        '''

        douban_id = ""
        try:
            h = httplib2.Http()
            # data = {
            #     "q": name
            # }

            headers = {
                # "User-Agent": spider.make_random_useragent("pc"),
                # "Host": "movie.douban.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, sdch, br",
                "Accept-Language": "zh-CN, zh; q=0.8, en; q=0.6",
                "Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
            }
            # resp, content = h.request("https://api.douban.com/v2/movie/search", "POST", urlencode(data, encoding="utf-8"),
            #                              headers={'Content-Type': 'application/x-www-form-urlencoded'})
            urlstr = 'https://api.douban.com/v2/movie/search' + '?q=' + name
            resp, content = h.request(urlstr, headers=headers)
            content = json.loads(str(content, encoding="utf-8"))

            for item in content['subjects']:
                if year == item['year']:
                    douban_id = item['id']
                    break

            if douban_id == "":
                for item in content['subjects']:
                    if name == item['title']:
                        douban_id = item['id']
                        break

        except Exception as e:
            douban_id = "error"
            return douban_id
        return douban_id

    def get_film_detail(self, douban_id):
        '''
        获取电影基本信息
        :return:
        '''
        try:
            h = httplib2.Http()
            urls = "https://api.douban.com/v2/movie/subject/"+douban_id
            # data = {
            #
            # }
            # resp, content = h.request(urls, "POST", urlencode(data, encoding="utf-8"),
            #                           headers={'Content-Type': 'application/x-www-form-urlencoded'})
            headers = {
                # "User-Agent": spider.make_random_useragent("pc"),
                # "Host": "movie.douban.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, sdch, br",
                "Accept-Language": "zh-CN, zh; q=0.8, en; q=0.6",
                "Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
            }

            resp,content = h.request(urls, headers=headers)
            content = json.loads(str(content, encoding="utf-8"))
            if content['rating']:
                return content
            else:
                return None
        except:
            return None

    def get_photos(self):
        '''
        获取电影剧照
        :return:
        '''

        return
