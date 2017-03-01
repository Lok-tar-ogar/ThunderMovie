# encoding:utf-8
import os
import sys
import getopt
import django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.insert(0, pathname)
# sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ThunderMovie.settings")
django.setup()

import logging
from core.models import *
from douban import douban as doubanclass
import time


class DoubanInformation:
    '''
    循环获取豆瓣 电影、影人的信息
    '''
    def get_movie_base_information(self):
        '''
        获取豆瓣电影基本信息
        :return:
        '''
        try:
            try:
                start_id = FILM.objects.filter(if_useapi=1).order_by('-id')[0].id+1
            except Exception as e:
                start_id = FILM.objects.all().order_by('id')[0].id
            end = FILM.objects.all().order_by('-id')[0].id

            while start_id <= end:
                try:
                    film = FILM.objects.get(id=start_id)
                except Exception as e:
                    start_id += 1
                    logging.warning("数据库不存在id为"+ str(start_id) +"的数据！")
                    continue
                if film:
                    time.sleep(37)
                    db = doubanclass()
                    douban_movie = db.get_film_douban_id(film.film_name, film.film_pub_year)
                    if douban_movie == "error" or douban_movie == "":
                        logging.warning('id为：' + str(start_id) + "的电影从豆瓣导出失败！")
                        film.if_useapi = "1"
                        film.save()
                        start_id += 1
                        continue

                    film.stars = douban_movie["rating"]["average"]
                    # film.ratings_count = douban_movie["ratings_count"]
                    # film.reviews_count = douban_movie["reviews_count"]
                    # film.comments_count = douban_movie["comments_count"]
                    # film.wish_count = douban_movie["wish_count"]
                    # film.film_intro = douban_movie["summary"]
                    film.collect_count = douban_movie["collect_count"]
                    film.origin_title = douban_movie["original_title"]
                    film.alt = douban_movie["alt"]
                    film.if_useapi = "1"
                    film.douban_id = douban_movie["id"]
                    film.douban_title = douban_movie["title"]
                    film.film_pub_year = douban_movie["year"]
                    if douban_movie["images"]:
                        film.small_douban_image = douban_movie["images"]["small"]
                        film.middle_douban_image = douban_movie["images"]["medium"]
                        film.big_douban_image = douban_movie["images"]["large"]

                    if douban_movie["casts"]:
                        for item in douban_movie["casts"]:
                            if item["id"] is None:
                                actor = ACTORS.objects.filter(name=item["name"])
                                if actor:
                                    if film.actors.filter(film__actors__name=actor[0].name) is None:
                                        film.actors.add(actor)
                                else:
                                    act = ACTORS()
                                    act.douban_id = item["id"]
                                    act.alt = item["alt"]
                                    act.name = item["name"]
                                    if item["avatars"]:
                                        act.small_douban_image = item["avatars"]["small"]
                                        act.middle_douban_image = item["avatars"]["medium"]
                                        act.big_douban_image = item["avatars"]["large"]
                                    act.save()
                                    film.actors.add(act)
                            else:
                                actor = ACTORS.objects.filter(douban_id=item["id"])
                                if actor:
                                    if film.actors.filter(film__actors__douban_id=actor[0].douban_id) is None:
                                        film.actors.add(actor)
                                else:
                                    act = ACTORS()
                                    act.douban_id = item["id"]
                                    act.alt = item["alt"]
                                    act.name = item["name"]
                                    if item["avatars"]:
                                        act.small_douban_image = item["avatars"]["small"]
                                        act.middle_douban_image = item["avatars"]["medium"]
                                        act.big_douban_image = item["avatars"]["large"]
                                    act.save()
                                    film.actors.add(act)
                    if douban_movie["directors"]:
                        for item in douban_movie["directors"]:
                            if item["id"] is None:
                                director = DIRECTORS.objects.filter(name=item["name"])
                                if director:
                                    if film.directors.filter(film__directors__name=director[0].name) is None:
                                        film.directors.add(director)
                                else:
                                    direct = DIRECTORS()
                                    direct.douban_id = item["id"]
                                    direct.alt = item["alt"]
                                    direct.name = item["name"]
                                    if item["avatars"]:
                                        direct.small_douban_image = item["avatars"]["small"]
                                        direct.middle_douban_image = item["avatars"]["medium"]
                                        direct.big_douban_image = item["avatars"]["large"]
                                    direct.save()
                                    film.directors.add(direct)

                            else:
                                director = DIRECTORS.objects.filter(douban_id=item["id"])
                                if director:
                                    if film.directors.filter(film__directors__douban_id=director[0].douban_id) is None:
                                        film.directors.add(director)
                                else:
                                    direct = DIRECTORS()
                                    direct.douban_id = item["id"]
                                    direct.alt = item["alt"]
                                    direct.name = item["name"]
                                    if item["avatars"]:
                                        direct.small_douban_image = item["avatars"]["small"]
                                        direct.middle_douban_image = item["avatars"]["medium"]
                                        direct.big_douban_image = item["avatars"]["large"]
                                    direct.save()
                                    film.directors.add(direct)
                    film.save()
                    logging.warning('id为：' + str(start_id) + "的电影获取成功")
                    start_id += 1
                else:
                    continue
        except Exception as e:
            logging.warning(e)

    def check_error_movie(self):
        '''
        检查出错的电影 看是否能够拯救
        :return:
        '''

        try:
            movie = FILM.objects.filter(stars__isnull=True, if_useapi=1)

            for i in movie:
                try:
                    film = FILM.objects.get(id=i.id)
                except Exception as e:
                    continue
                if film:
                    time.sleep(37)
                    db = doubanclass()
                    douban_movie = db.get_film_douban_id(film.film_name, film.film_pub_year)
                    if douban_movie == "error" or douban_movie == "":
                        logging.warning('id为：' + str(i.id) + "的电影从豆瓣导出失败！")
                        film.if_useapi = "1"
                        film.save()
                        continue

                    film.stars = douban_movie["rating"]["average"]

                    film.collect_count = douban_movie["collect_count"]
                    film.origin_title = douban_movie["original_title"]
                    film.alt = douban_movie["alt"]
                    film.if_useapi = "1"
                    film.douban_id = douban_movie["id"]
                    film.douban_title = douban_movie["title"]
                    film.film_pub_year = douban_movie["year"]
                    if douban_movie["images"]:
                        film.small_douban_image = douban_movie["images"]["small"]
                        film.middle_douban_image = douban_movie["images"]["medium"]
                        film.big_douban_image = douban_movie["images"]["large"]

                    if douban_movie["casts"]:
                        for item in douban_movie["casts"]:
                            if item["id"] is None:
                                actor = ACTORS.objects.filter(name=item["name"])
                                if actor:
                                    if film.actors.filter(film__actors__name=actor[0].name) is None:
                                        film.actors.add(actor)
                                else:
                                    act = ACTORS()
                                    act.douban_id = item["id"]
                                    act.alt = item["alt"]
                                    act.name = item["name"]
                                    if item["avatars"]:
                                        act.small_douban_image = item["avatars"]["small"]
                                        act.middle_douban_image = item["avatars"]["medium"]
                                        act.big_douban_image = item["avatars"]["large"]
                                    act.save()
                                    film.actors.add(act)
                            else:
                                actor = ACTORS.objects.filter(douban_id=item["id"])
                                if actor:
                                    if film.actors.filter(film__actors__douban_id=actor[0].douban_id) is None:
                                        film.actors.add(actor)
                                else:
                                    act = ACTORS()
                                    act.douban_id = item["id"]
                                    act.alt = item["alt"]
                                    act.name = item["name"]
                                    if item["avatars"]:
                                        act.small_douban_image = item["avatars"]["small"]
                                        act.middle_douban_image = item["avatars"]["medium"]
                                        act.big_douban_image = item["avatars"]["large"]
                                    act.save()
                                    film.actors.add(act)
                    if douban_movie["directors"]:
                        for item in douban_movie["directors"]:
                            if item["id"] is None:
                                director = DIRECTORS.objects.filter(name=item["name"])
                                if director:
                                    if film.directors.filter(film__directors__name=director[0].name) is None:
                                        film.directors.add(director)
                                else:
                                    direct = DIRECTORS()
                                    direct.douban_id = item["id"]
                                    direct.alt = item["alt"]
                                    direct.name = item["name"]
                                    if item["avatars"]:
                                        direct.small_douban_image = item["avatars"]["small"]
                                        direct.middle_douban_image = item["avatars"]["medium"]
                                        direct.big_douban_image = item["avatars"]["large"]
                                    direct.save()
                                    film.directors.add(direct)

                            else:
                                director = DIRECTORS.objects.filter(douban_id=item["id"])
                                if director:
                                    if film.directors.filter(film__directors__douban_id=director[0].douban_id) is None:
                                        film.directors.add(director)
                                else:
                                    direct = DIRECTORS()
                                    direct.douban_id = item["id"]
                                    direct.alt = item["alt"]
                                    direct.name = item["name"]
                                    if item["avatars"]:
                                        direct.small_douban_image = item["avatars"]["small"]
                                        direct.middle_douban_image = item["avatars"]["medium"]
                                        direct.big_douban_image = item["avatars"]["large"]
                                    direct.save()
                                    film.directors.add(direct)
                    film.save()
                    logging.warning('id为：' + str(i.id) + "的电影获取成功")
                else:
                    continue
        except Exception as e:
            logging.warning(e)

    def get_movie_detail(self):
        '''
        获取电影详情
        :return:
        '''
        try:
            try:
                start_id = FILM.objects.filter(comments_count__isnull=False).order_by('-id')[0].id+1
            except Exception as e:
                start_id = FILM.objects.all().order_by('id')[0].id
            end = FILM.objects.all().order_by('-id')[0].id

            while start_id < end:
                try:
                    film = FILM.objects.get(id=start_id)
                except Exception as e:
                    start_id += 1
                    logging.warning("不存在id为" + str(start_id) + "的电影")
                    continue
                if film.douban_id:
                    db = doubanclass()
                    douban_movie = db.get_film_detail(film.douban_id)
                    if douban_movie is None:
                        start_id += 1
                        continue
                    film.film_name = douban_movie["title"]
                    film.ratings_count = douban_movie["ratings_count"]
                    film.reviews_count = douban_movie["reviews_count"]
                    film.comments_count = douban_movie["comments_count"]
                    film.wish_count = douban_movie["wish_count"]
                    film.film_intro = douban_movie["summary"]
                    film.film_pub_year = douban_movie["year"]
                    film.subtype = douban_movie["subtype"]
                    if douban_movie["countries"]:
                        for item in douban_movie["countries"]:
                            country = Countries.objects.filter(name=item)
                            if country:
                                if film.douban_country.filter(film__douban_country__name=item) is None:
                                    film.douban_country.add(country)
                            else:
                                coun = Countries()
                                coun.name = item
                                coun.save()
                                film.douban_country.add(coun)

                    if douban_movie["genres"]:
                        for item in douban_movie["genres"]:
                            genre = Film_genres.objects.filter(name=item)
                            if genre:
                                if film.douban_country.filter(film__douban_genres__name=item) is None:
                                    film.douban_country.add(genre)
                            else:
                                gen = Film_genres()
                                gen.name = item
                                gen.save()
                                film.douban_genres.add(gen)

                    if douban_movie["aka"]:
                        for item in douban_movie["aka"]:
                            akas = AKA.objects.filter(name=item)
                            if akas:
                                if film.douban_country.filter(film__aka__name=item) is None:
                                    film.douban_country.add(akas)
                            else:
                                a = AKA()
                                a.name = item
                                a.save()
                                film.aka.add(a)

                    film.save()
                    start_id += 1
                    logging.warning(str(start_id)+"详情更新成功！")

        except Exception as e:
            logging.warning(e)


def main(argv):
    inp = ""
    try:
        opts, args = getopt.getopt(argv, "hi:", ["input="])
    except getopt.GetoptError:
        print("you need to input the function index that you want to run:  ")
        print("1.get_movie_base_information")
        print("2.check_error_movie")
        print("3.get_movie_detail")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("you need to input the function index that you want to run:  ")
            print("1.get_movie_base_information")
            print("2.check_error_movie")
            print("3.get_movie_detail")
        elif opt in ["-i", "--input"]:
            opt = arg
            if opt == "1":
                di = DoubanInformation()
                logging.warning(" get_movie_base_information is ready to start.")
                di.get_movie_base_information()
                logging.warning("Mission clear")
            if opt == "2":
                di = DoubanInformation()
                logging.warning(" check_error_movie is ready to start.")
                di.check_error_movie()
                logging.warning("Mission clear")
            if opt == "3":
                di = DoubanInformation()
                logging.warning(" get_movie_detail is ready to start.")
                di.get_movie_detail()
                logging.warning("Mission clear")

if __name__ == '__main__':
    main(sys.argv[1:])
