from celery import Celery
from celery.utils.log import get_task_logger
from .models import News
import requests
from bs4 import BeautifulSoup
from time import sleep


logger = get_task_logger(__name__)


app = Celery()


def urlScraper():
    domain = 'https://news.un.org/en/news/region/africa'
    page = requests.get(domain)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all("h1", {"class" : "story-title"})
    links = []
    titles = []
    for link in data:
        if "https://news.un.org" in link.a["href"]:
            links.append(link.a["href"])
        else:
            links.append("https://news.un.org"+link.a["href"])
        titles.append(link.text)            
    body = soup.find_all("div", {"class" : "news-body"})
    texts = []
    for te in body:
        texts.append(te.p.text)
    
    dict_of_data = {}
    i = 0
    for lnk, title, text in zip(links, titles, texts):
        dict_of_data["data"+str(i)] = {
            "title" : title,
            "link" : lnk,
            "text" : text
        }
        i += 1
    
    return dict_of_data




@app.task
def save_data():
    data = urlScraper()
    for value in data:
        if News.objects.filter(link=data[value]["link"]).exists():
            logger.info("News already scrapped....")
        else:
            News.objects.create(
            title=data[value]["title"],
            link=data[value]["link"],
            text=data[value]["text"]
            )
            logger.info("Database created succefully...")

            #Send latest news to users:
            url = "http://email:8000/api/v1/send-mail/"
            news = {
            "title" : data[value]["title"],
            "text" : data[value]["text"],
            "link" : data[value]["link"]
            }
            req = requests.post(url, data=news)
            logger.info(req.text)
            sleep(5)

@app.on_after_configure.connect
def save_data_task(sender, **kwargs):
    sender.add_periodic_task(10.0, save_data(), name='add every 10')
