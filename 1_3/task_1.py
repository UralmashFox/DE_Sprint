import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
sess = req.Session()
sess.headers.update({
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/105.0.0.0 Safari/537.36'
})

data = {
    "data": []
}

def get_data(sess, url_obj):
    resp_object = sess.get(url_obj)
    soup_object = BeautifulSoup(resp_object.text, "lxml")
    tag_title = soup_object.find(attrs={"class": "vacancy-title"}).find("h1").text
    tag_we = soup_object.find(attrs={"data-qa": "vacancy-experience"}).text
    tag_salaray = soup_object.find(attrs={"class": "vacancy-title"}).find(attrs={"data-qa": "vacancy-salary"}).text
    tag_region = soup_object.find(attrs={"data-qa": "vacancy-serp__vacancy-address"}).text
    return tag_title, tag_we, tag_salaray, tag_region


for n in tqdm.tqdm(range(40)):
    url = f"https://hh.ru/search/vacancy?text=python++%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&area=1&page=0&hhtmFrom=vacancy_search_list"
    resp = sess.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"class": "serp-item__title"})
    for iter in tags:
        url_obj = iter.attrs['href'].split('?')[0]
        try:
            tag_title, tag_we, tag_salaray, tag_region = get_data(sess, url_obj)
            data['data'].append({
                "title": tag_title,
                "work experience": tag_we,
                "salary": tag_salaray,
                "region": tag_region,
            })
            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii=False)
        except:
            continue
