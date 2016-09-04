# encoding: utf-8
import httplib2
from urllib.parse import urlencode
import json


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
            data = {
                "q": name
            }
            resp, content = h.request("https://api.douban.com/v2/movie/search", "POST", urlencode(data, encoding="utf-8"),
                                         headers={'Content-Type': 'application/x-www-form-urlencoded'})

            content = json.loads(str(content, encoding="utf-8"))
            if content["msg"]:
                douban_id = "error"
            else:
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
            pass
        return douban_id

    def get_film_detail(self, douban_id):
        '''
        获取电影基本信息
        :return:
        '''
        try:
            h = httplib2.Http()
            urls = "https://api.douban.com/v2/movie/subject/"+douban_id
            resp, content = h.request(urls, "POST", headers={'Content-Type': 'application/x-www-form-urlencoded'})
            content = json.loads(str(content, encoding="utf-8"))
            return content
        except:
            return None

    def get_photos(self):
        '''
        获取电影剧照
        :return:
        '''

        return
