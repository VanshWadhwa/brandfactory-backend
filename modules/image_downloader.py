from os import path
from urllib.request import urlretrieve
import string
import random

import pathlib

# initializing size of string
# N = 7

# using random.choices()
# generating random strings

import logging

# logger = logging.getLogger(__name__)

# logging.basicConfig(filename = "logs.log" , level = logging.INFO , format="%(asctime)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
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


class ImageDownloader:

    def __init__(self):
        # pathnow = pathlib.Path().cwd()
        # print("pathnow str : ", str(pathnow))
        # print("pathnow  : ", pathnow)
        # self.path = str(pathnow) + "/assets/images/"
        # print("self.path  : ", self.path)

        self.path = pathlib.Path('.').cwd() / 'assets/images/'

        print("self.path  : ", str(self.path))

        # print("Image Downloader instance created")

    def downloadImage(self, filename, url):
        # print("-----Entered image download function")
        # for url in URL:
        # print("url : ", url)

        pathnow = self.path
        print("pathnow str : ", str(pathnow))
        print("pathnow  : ", pathnow)

        if filename == None:
            filename = url.split('/')[-1].split('.')[0]

        # imgLocation = self.path+filename + ".png"
        # N = 7
        # res = ''.join(random.choices(string.ascii_uppercase +
        #                  string.digits, k = N))

        imgLocation = str(pathnow) + "\\" + filename
        # imgLocation =
        print("imgLocation : ", imgLocation)
        # user_agents = [ 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11', 'Opera/9.25 (Windows NT 5.1; U; en)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12', 'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9']
        # user_agents = user_agents = ['Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        # user_agents = user_agents = ['Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        # user_agents = ['Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11']

        # headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

        # urlretrieve(url, imgLocation , headers={'User-Agent': 'Mozilla/5.0'})
        urlretrieve(url, imgLocation)
        # urlretrieve(url, imgLocation , headers)
        # print("Downloaded : " , filename )
        # print("Img location : " , imgLocation)
        # print("image Downloaded : " , imgLocation)
        logger.debug("Downloaded Image at : " + imgLocation)

    # def log(self):
    #     # logging.info("Hi")
    #     logger.debug("Hi")


# ID = ImageDownloader()
#
# ID.downloadImage("try2.png","https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2020/12_dec/26_sat/img_1608956833048_716.jpg")
