
import logging

import os
from .image_handler import ImageHandler
from .news_handler import NewsHandler
from .image_downloader import ImageDownloader
from .telegram_hander import TelegramHandler

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info("----GAME STARTED----")

ID = ImageDownloader()


def createTemp1(text, url):
    """Mainly made for 1 liner news """
    # url = str(url)
    # print("URL :::::::::", url)
    # +url.split('/')[-1].split('.')[1]
    filename = url.split('/')[-1].split('.')[0] + ".png"
    # print('filename : ', filename)
    ID.downloadImage(filename, url)
    IH = ImageHandler(filename)
    # IH.secondaryColor = (49, 188, 238)
    # IH.resizeImage(type = "fromCentre")
    IH.resizeImage()
    IH.overLayImage("\\assets\\images\\basicGradient.png")
    IH.overLayImage("\\assets\\images\\temp1.png")
    importantWords = IH.addText(
        text, fontSize=5, atY=-170, containsImportantWords=True, returnImportantWords=True)
    IH.saveImage()
    del IH
    return filename, text, importantWords

def createTemp2(text, url):
    """Mainly made for 1 liner news """
    # url = str(url)
    # print("URL :::::::::", url)
    # +url.split('/')[-1].split('.')[1]

    # print("HEck filename : " , url.split('/')[-1].split('.')[0] , " " , url.split('/')[-1].split('.')[1])
    filename = url.split('/')[-1].split('.')[0] + "." + url.split('/')[-1].split('.')[1]
    print("filename : " , filename)
    # filename = url.split('/')[-1].split('.')[0] + "."

    # print('filename : ', filename)
    # ID.downloadImage(filename, url)

    # pathOfImage 
    # filename = url

    filepath =  filename
    # filepath = "\\media\\post_images\\" + filename




    print('Filename : ' , filename)
    IH = ImageHandler(filename)
    # IH.secondaryColor = (49, 188, 238)
    # IH.resizeImage(type = "fromCentre")
    IH.resizeImage()
    IH.overLayImage("\\assets\\images\\basicGradient.png")
    IH.overLayImage("\\assets\\images\\temp1.png")
    importantWords = IH.addText(
        text, fontSize=5, atY=-170, containsImportantWords=True, returnImportantWords=True)
    IH.saveImage()
    del IH
    location = '/output/' + filename
    return filename, text, importantWords , location 


def createDescriptiveNews(header, description, filename, url):
    """Mainly made for 1 liner news """
    try:
        ID.downloadImage(filename, url)
        filePath = "../assets/images/" + filename
        IH = ImageHandler("BG.png")
        IH.resizeImage(x=1080, y=1080)
        IH2 = ImageHandler(filename)
        IH2.resizeImage(x=1020, y=600, type="fromCentre")
        IH2.saveImage(filename, path="../assets/images/")
        del IH2

        IH.overLayImage(filePath, atX=30, atY=30)
        IH.primaryColor = (255, 255, 255)
        IH.overLayImage("../assets/images/logo(130x130).png", atX=475, atY=550)
        importantWords = IH.addText(header, fontSize=4, fontPath="assets/fonts/Merriweather-Bold.ttf",
                                    atY=-240, containsImportantWords=True, returnImportantWords=True)

        IH.addText(description, fontSize=2,
                   fontPath="assets/fonts/Merriweather-Regular.ttf",  atY=-100)
        try:
            os.remove("../assets/images/"+filename)

        except Exception as e:
            logger.debug("Not deleted Due to : ", e)
        IH.saveImage(filename)

        return importantWords

    except:
        logger.exception("Error in creating Descripting News")


# NH = NewsHandler()

# # createTemp1(    'Report on $42-billion deal to buy Alzheimers drug maker Biogen untrue: Samsung', "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2021/12_dec/30_thu/img_1640855093097_710.jpg")

# x = NH.getDescriptiveNews(2)

# for i in x:

#     i[0] = NH.clearExtra(i[0])
# # print(i[1])
#     i[1] = NH.clearExtra(i[1], symbol=".") + "."

#     print(i)

#     createDescriptiveNews(
#         i[0], i[1], i[2], i[3])
