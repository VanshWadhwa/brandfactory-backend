import requests
from bs4 import BeautifulSoup
import string
import random
from .image_downloader import ImageDownloader

import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class NewsHandler:
    def __init__(self):
        logger.info("NewsHandler Inctance created")
        self.url = "https://inshorts.com/en/read/business"
        # self.url = "https://inshorts.com/en/read/"
        # r = requests.get(self.url).content
        # soup = BeautifulSoup(r, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

    def getOneLiner(self, amount):
        # URL = "https://www.geeksforgeeks.org/data-structures/"
        r = requests.get(self.url).content
        # If this line causes an error, run 'pip install html5lib' or install html5lib
        soup = BeautifulSoup(r, 'html5lib')

        # print(r.content)
        # print(soup.prettify())
        # /html/body/div[4]/div/div[3]/div[1]/div/div[2]/a/span
        # <span itemprop="headline">CRED members to get gifts worth ₹16 crore for paying credit card bills</span>
        # body > div.container > div > div.card-stack > div:nth-child(1) > div > div.news-card-title.news-right-box > a > span
        # instructions = recipeSoup.find("div", itemprop="name")
        # allNews = soup.body
        # allNews = soup.body.find_all("div" , class_="news-card z-depth-1")
        # allNews = soup.body.find_all("div" , class_="container")
        # allNews = soup.body.find_all("div" , class_="row")
        # allNews = soup.body.find_all("div" , class_="row")
        # allNews = soup.body.find_all("div" , class_="news-card z-depth-1")
        allNewsText = soup.body.find_all(
            "div", class_="news-card-title news-right-box")
        allNewsImageURL = soup.body.find_all("div", class_="news-card-image")
        # allNews = soup.body.find_all("div.div.div.div.div.spam" , itemprop="headline")
        # allNews = soup.body.find_all("div.div.div.div.div.spam" , itemprop="headline")
        # allNews = soup.body.find_all("spam" , itemprop="headline")
        # allNews = soup.body.div.div.div.div.div
        # print(allNews)
        newsList = []
        # print(type(allNewsText))
        for i in range(amount):
            # print(allNewsText[i].a.text)
            # print(allNewsImageURL[i]['style'].split("url('")[1][:-3])
            # print("allNewsImageURl" , allNewsImageURL[i])
            # print("allNewsImageURl" , allNewsImageURL[i]['style'].split("url('")[1][:-3])
            newsList.append((" ".join(allNewsText[i].a.text.split(
            )), allNewsImageURL[i]['style'].split("url('")[1][:-3]))

        # print("newsList" , newsList)

        # print(newsList)
        return newsList

    def getDescriptiveShorts(self, amount):
        URL = "https://inshorts.com/en/read/business"
        r = requests.get(self.url).content
        # If this line causes an error, run 'pip install html5lib' or install html5lib
        soup = BeautifulSoup(r, 'html5lib')

        # print(r.content)
        allNewsText = soup.body.find_all(
            "div", class_="news-card-title news-right-box")
        allNewsImageURL = soup.body.find_all("div", class_="news-card-image")
        # allNewsDescription = soup.body.find_all("div" , class_="news-card-content news-right-box")
        allNewsDescription = soup.body.find_all("div", itemprop="articleBody")
        allNewsSourceLink = soup.body.find_all(
            "div", class_="news-card-footer news-right-box")
        # print(allNewsDescription)
        # allNews = soup.body.find_all("div.div.div.div.div.spam" , itemprop="headline")
        newsList = []
        # print(type(allNewsText))

        for i in range(amount):
            # print(allNewsText[i].a.text)
            res = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=7))

            filenameToBeSavedAs = res + ".png"
            newsList.append((" ".join(allNewsText[i].a.text.split()), " ".join(allNewsDescription[i].text.split(
            )),  allNewsImageURL[i]['style'].split("url('")[1][:-3], filenameToBeSavedAs, " ".join(allNewsSourceLink[i].a["href"].split())))

        # print(newsList)
        return newsList

    def getOneLinerFlip(self, amount):
        self.url = "https://flipitnews.com/flips"
        r = requests.get(self.url).content
        soup = BeautifulSoup(r, 'html5lib')  # If this line caus

        allNewsText = soup.body.find_all(
            "div", class_="p-sm-4 pl-sm-5 pr-sm-5")
        allNewsImageURL = soup.body.find_all(
            "div", class_="d-flex flex-column flex-lg-row no-gutters border rounded bg-white o-hidden")

        # for i in allNewsText:
        #     print(i.a.h1.text)

        # for i in allNewsImageURL:
        #     print(i.a.img["src"])

        newsList = []
        # print(type(allNewsText))
        for i in range(amount):
            # print(allNewsText[i].a.text)
            # print(allNewsImageURL[i]['style'].split("url('")[1][:-3])
            newsList.append(
                (allNewsText[i].a.h1.text, allNewsImageURL[i].a.img["src"]))

        # print(newsList)
        return newsList

    def getDescriptiveNews(self, amount=5):
        """this get news from the newsapi with description"""
        # URL = ('https://newsapi.org/v2/top-headlines?'
        #     'country=in&'
        #     'apiKey=beec77fb9b4b4eeba97926a8ad867bc3'
        #     )
        URL = ('https://newsapi.org/v2/top-headlines?'
               'country=in&'
               'category=business&'
               'apiKey=beec77fb9b4b4eeba97926a8ad867bc3'
               )

        # URL = ('https://newsapi.org/v2/everything?'
        #     'q=elon Musk&'
        #     # 'category=business&'
        #     'apiKey=beec77fb9b4b4eeba97926a8ad867bc3'
        #     )
        # headers_dict={'User-Agent': 'Mozilla/5.0'}
        # response = requests.get(URL , headers=headers_dict)
        response = requests.get(URL)
        # print(response.json())
        # print(response.json()["articles"][1]["title"])
        # print(response.json()["articles"][0]["author"])
        newsList = []
        # ID = ImageDownloader()
        # print(response.json())
        for i in range(amount):
            # print("---" , i , "---")
            title = response.json()["articles"][i]["title"]
            description = response.json()["articles"][i]["description"]
            urlToImage = response.json()["articles"][i]["urlToImage"]
            # content = response.json()["articles"][i]["content"]
            N = 7
            res = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=N))

            filenameToBeSavedAs = res + ".png"
            # print(filenameToBeSavedAs)

            # try:
            #     ID.downloadImage(filenameToBeSavedAs , urlToImage  )
            #     print("Image Downloaded")
            # except Exception as e:
            #     print(e)

            # print("Title : " , title)
            # print("Description : " , description)
            # print("urlToImage : " , urlToImage)
            # print("filenameToBeSavedAs : " , filenameToBeSavedAs)

            newsList.append(
                [title, description, filenameToBeSavedAs, urlToImage])
        # print(newsList)
        return newsList

    def getIndexes(self):
        """GEt senex and nifty at real time"""
        self.url = "https://ticker.finology.in/"
        r = requests.get(self.url).content
        soup = BeautifulSoup(r, 'html5lib')  # If this line caus

        indexes = soup.body.find_all("div", class_="col-12 col-md-3 item")
        finalData = ""
        j = 0
        for i in indexes:
            # print(i , j)
            textLine = i.text.split()
            # print(i.text)
            # for j in range(len(indexes)):
            # if j == 0 :
            #     # print("ENTEREEDDDDD")
            #     pass
            # continue
            if j != 0:
                textLine[0] = textLine[0] + textLine[1]
                del textLine[1]
                # textLine.pop(1)
                # pass

            j = j + 1
            # print(textLine[0],textLine[1],textLine[2],textLine[3])
            finalData += str('{:<12s}{:>12s}{:>12s}{:>12s}\n'.format(
                textLine[0], textLine[1], textLine[2], textLine[3]))
            # print("+="*15)

            # print(textLine)

        return finalData

    def clearExtra(self, text, symbol="-", index=-1):
        """This functions removes the unneccacry text from news like text which is not continued"""
        # print("TEXT : " , text)
        textList = text.split(symbol)
        # print("TEXT : " , text)
        # print("textList : " , textList)

        # print("len(textList) : " , len(textList))
        if len(textList) > 1:
            # print("len(textList) > 0")
            # print("text : " ,text)
            text = symbol.join(textList[0:index])
            # print("text : " ,text)

        # print("text : " ,text)

        return text

        # print(finalData)


# <h1>PE investment in real estate to drop 31% at $4.6 billion in 2020</h1>
# <h1>PE investment in real estate to drop 31% at $4.6 billion in 2020</h1>
# /html/body/section[1]/div/div[1]/div/div[1]/div/div/div/a[1]/h1
# body > section.bg-light > div > div.row.mt-3.mt-sm-0 > div > div:nth-child(1) > div > div > div > a:nth-child(2) > h1

        # newsList = []
        # for i in range(amount):
        #     print(allNewsText[i].text)
        #     # print(allNewsImageURL[i]['style'].split("url('")[1][:-3])
        #     # newsList.append((" ".join(allNewsText[i].a.text.split()) , allNewsImageURL[i]['style'].split("url('")[1][:-3]))

        # print(newsList)
        # return newsList

#
# NH = NewsHandler()
# text = "Hi i am vansh wadhwa - vansh - wadhwa - kj n kn - jb - kjbkjb"
# text = "Hi i am vansh wadhwa. Vansh wadhwa  is a great man . He is .."
# text = "Congress leader Rahul Gandhi, in an online interaction former US ambassador Nicolas Burns, has questioned the apparent silence of US on what he claims to be the 'destructive' happenings in India with regards to democracy. The statement is being seen by some a…"
# text = "Huawei Band 6 has launched in the Malaysian market. The fitness band will go on sale on April 4. It comes in Amber Sunrise, Forest Green, and Graphite Black colour options. The wearable comes with SpO2, heart rate, and sleep monitoring, along with 96 workout …"
# text = " Delhi Capitals all-rounder Axar Patel has tested positive for coronavirus, the franchise confirmed on Saturday."


# print(NH.clearExtra(text , symbol = "."))
# NH = NewsHandler()
# x = NH.getDescriptiveShorts(10)
# print(x)
# for i in x:
    # print(i[1])
# x = NH.getDescriptiveNews()
# print(x)
# # NH.getIndexes()
# # print(NH.getOneLinerFlip(5))
# print(NH.getOneLiner(1))
# # NH.getOneLinerImagesURL()
