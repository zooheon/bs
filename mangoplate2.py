from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import time

itaewon_food = {}

def mangoplate_search(url_search, dic):
    url_main = "http://www.mangoplate.com"


    for k in range(1, 3):
        try:
            time.sleep(1)
            url_search = url_search + str(k)
            html = urlopen(url_search).read()
            soup = BeautifulSoup(html, "html.parser")

            name = None
            restaurant_data = None
            phone_num = None
            restaurant_href = None
            data3 = None

            for link in soup.findAll('a', {'class': 'only-desktop_not'}):
                href = link.get('href')
                url = url_main + href
                html_restaurant = urlopen(url).read()
                soup_restaurant = BeautifulSoup(html_restaurant, "html.parser")

                name = soup_restaurant.select('.restaurant_name')[0].text

                restaurant_data = soup_restaurant.select('table > tbody > tr')
                data3 = []
                tel_checker = re.compile(r"(\d{2,3})-(\d{3,4})-(\d{4,5})")
                for data in restaurant_data:
                    data1 = data.text
                    data2 = data1.split('\n')
                    data3 = data3 + data2
                for dataaa in data3:
                    phone_num = tel_checker.match(dataaa)
                    if phone_num != None:
                        phone_num = phone_num.group(0)
                        break
                    else:
                        phone_num = "None"

                url_list = []
                for page_url in soup_restaurant.findAll('a', {'class': "under_line"}):
                    restaurant_href = page_url.get('href')
                    url_list.append(str(restaurant_href))
                    if url_list[0] != "mailto://cs@mangoplate.com":
                        restaurant_url = url_list[0]
                    else:
                        restaurant_url = "None"

                dic[name] = (phone_num, restaurant_url)

        except:
            break

    print(dic)

mangoplate_search("https://www.mangoplate.com/search/%EC%9D%B4%ED%83%9C%EC%9B%90?keyword=%EC%9D%B4%ED%83%9C%EC%9B%90&page=", itaewon_food)