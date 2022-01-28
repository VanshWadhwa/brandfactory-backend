from PIL import Image, ImageDraw, ImageFont
import textwrap
import pathlib

# from numpy import product, select

from .text_handler import importantWords
import pyqrcode

import logging
from configparser import ConfigParser


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

config = ConfigParser()
config.read('../../config.ini')


# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class ImageHandler:

    def __init__(self, imagePath):

        logger.info("ImageHandler Instance Created")

        # self.path = "../assets/images/"
        self.path = pathlib.Path('.').cwd()

        self.fileName = imagePath



        if type(imagePath) == str:
            self.imageObj = Image.open(str(self.path) +  '\\assets\\images\\'+ imagePath)

        else:
            self.imageObj = Image.open(imagePath);

            self.fileName = imagePath.name
        # self.primaryColor = config['DESIGN']['primaryColor']
        # self.secondaryColor = config['DESIGN']['secondaryColor']

        # self.primaryColor = (212, 212, 35)
        self.primaryColor = (255,255,255)

        # self.secondaryColor = (123, 221, 0)
        self.secondaryColor = (27,157,240)



    def overLayImage(self, otherImagePath, atX=0, atY=0, RGBA=1):
        """Enter the path of the image and it will add it to the other image
            Image is not saved
        """

        otherImagePath = str(self.path) + "\\" + otherImagePath

        otherImageObj = Image.open(otherImagePath)
        if RGBA == 1:
            otherImageObj = otherImageObj.convert('RGBA')
            self.imageObj.paste(otherImageObj, (atX, atY), mask=otherImageObj)
            # self.imageObj.alpha_composite(self.imageObj,otherImageObj)
        elif RGBA == 0:
            otherImageObj = otherImageObj.convert('RGB')
            self.imageObj.paste(otherImageObj, (atX, atY), mask=otherImageObj)

    def createQRcode(self, text, filenameToBeSavedAs):
        qr = pyqrcode.create(text)
        qr.png(filenameToBeSavedAs, scale=5)
        print("saved qr code at : ", filenameToBeSavedAs)

    def resizeImage(self, x=1080, y=1080, type="corner"):
        """Resizes Image according to X and Y"""

        # UPdate 
        # fromCorner -> corner
        # fromCenter -> center
        
        # alpha = alpha_gradient.resize(input_im.size)
        if type == "corner":
            self.imageObj = self.imageObj.resize((x, y))
        elif type == "centre":
            # im = Image.open(<your image>)
            width, height = self.imageObj.size   # Get dimensions

            left = (width - x)/2
            top = (height - y)/2
            right = (width + x)/2
            bottom = (height + y)/2

            # Crop the center of the image
            self.imageObj = self.imageObj.crop((left, top, right, bottom))

        # print(self.imageObj.width)

    # def resizeOtherImage(self , filePath):
    #     """This function resize another image not the self one"""

    def addText(self, text, atX=0, atY=None, fontSize=4, marginX=0, marginY=0, fontPath="../../assets/fonts/Merriweather-Regular.ttf", containsImportantWords=False, alignment="justified", returnImportantWords=False, containsRawText=False):
        """Add Text works with multiline , center Aligned text    
        use negative for atY to keep in mind the bottom margin
        """
        
        text = text.replace(u'\xa0', u' ')
        # text = text.replace(u"\'", u"'")

        # if containsRawText == False:
        #     text = repr(text)


# This is IMPORTANT
        # font = ImageFont.truetype(font=fontPath, size=int(
        #     self.imageObj.height*fontSize)//100)

        # font = ImageFont.load_default()
        # font = ImageFont.truetype("arial.ttf", 18)

        font = ImageFont.truetype(font='arial.ttf', size=int(
            self.imageObj.height*fontSize)//100)

        draw = ImageDraw.Draw(self.imageObj)

        # widthOfChar , heightOfChar = font.font.getsize("A")[0] ,font.font.getsize("A")[1]
        ascent, descent = font.getmetrics()
        # print("ascent, descent" ,ascent, descent)
        (width, baseline), (offset_x, offset_y) = font.font.getsize(text)
        # print("(width, baseline), (offset_x, offset_y)" ,(width, baseline), (offset_x, offset_y))

        widthOfChar, heightOfChar = font.getsize("a")

        # for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        #     print(i ," ",font.getsize(i) )

        # print("widthOfChar , heightOfChar " , widthOfChar , heightOfChar )

        # (widthOfChar, baselineOfChar), (offset_xOfChar, offset_yOfChar) = font.font.getsize("A")

        # print("-"*25)
        # print(widthOfChar , heightOfChar)
        # font.font.getsize(char)[0][0]
        # widthPerLine = (self.imageObj.width ) / widthOfChar
        widthPerLine = (self.imageObj.width - 2*marginX) // widthOfChar
        # print("widthPerLine = (self.imageObj.width ) / widthOfChar : " ,widthPerLine  , self.imageObj.width  , widthOfChar)
        # print()
        # widthPerLine = ( ) / widthOfChar
        if alignment == "justified":
            lines = textwrap.wrap(text, width=widthPerLine)
            # print("TEXT = " , text)
            # print("Lines = " , lines)

        elif alignment == "center":
            lines = text.split("\n")
        elif alignment == "leftAlign":
            # lines = text.split("\n")
            lines = text #last moment edit is buggy definately
            # pass
        heightOfTextBox = 0
        heightOfTextBox = heightOfChar * len(lines)
        #               DISCLAIMER :
        # For further processing heightOfTextBox is buggy
        #  kindly change the logic to use it for further utilisation
        # This is importhant....the above statement
        if atY == None:
            """Making the Y location of TEXT CAn be in center"""
            # If none then it will make it fall in center
            atY = ((self.imageObj.height/2) - (heightOfTextBox/2))
        elif atY < 0:
            # This will add margin at the bottom
            atY = self.imageObj.height - heightOfTextBox + atY

        atY += marginY
        # Margin can be used when needed
        # margin = self.imageObj.width*0.03

        def isGuilty():
            """Hahah this checks if the char at this index is to be changed in color or not"""

            guiltyIndexes = set()

            # Creates the set of guilty indexes
            x = 1
            for i in range(len(tuple(dictOfImportantText.values()))):
                if tuple(dictOfImportantText.values())[i][0] < 1:
                    x = 0
                guiltyIndexesShort = {j for j in range(tuple(dictOfImportantText.values())[
                                                       i][0],  tuple(dictOfImportantText.values())[i][1])}
                guiltyIndexes = guiltyIndexes.union(guiltyIndexesShort)

            x = indexOfChar in guiltyIndexes
            return x  # result if the current index is guilty of not

        indexOfChar = 0

        # Imp down
        # print(dictOfImportantText)
        for line in lines:

            # line_width, line_height = font.getsize(line)
            currentX = 0
            xyz = font.getmask(line).getbbox()
            # print("XYZ : " , xyz)
            try:
                line_width, line_height = xyz[2], xyz[3]
                line_height += descent
            except:
                line_width, line_height = 0, 0
            # print("line_width, line_height" ,line_width, line_height)

            if containsImportantWords == True:
                dictOfImportantText = importantWords(text)

            for char in line:
                if containsImportantWords == True:

                    if isGuilty():
                        color = self.secondaryColor
                    else:
                        color = self.primaryColor
                else:
                    color = self.primaryColor

                draw.text((((self.imageObj.width/2) - (line_width/2)) + currentX, atY),
                          char, font=font, fill=color)
                currentX += font.font.getsize(char)[0][0]
                indexOfChar += 1

            indexOfChar += 1
            # atY += line_height+offset_y+descent
            atY += line_height+descent
            # atY += line_height

        logger.debug("Text Added to Image , TEXT : " + text)

        if returnImportantWords == True:
            return dictOfImportantText

    def saveImage(self, fileName="", path="../output/"):
        """SAves the image"""
        # os.chdir('../..')
        # print(path , self.fileName)
        if fileName == "":
            fileName = self.fileName

        # otherImagePath = str(self.path) + "\\" + otherImagePath
        pathnow = self.path.cwd() 
        # finalPath = str(pathnow) + "\\output\\" + fileName
        finalPath = pathnow / 'output' / fileName

        print("FInal Path : " , finalPath)

        self.imageObj.save(finalPath)
        # print("File saved at : " , finalPath)
        # logger.debug("Image saved at " + finalPath)
        return finalPath

    def addRectangle(self, x1, y1, x2, y2, color=None):
        if color == None:
            color = self.secondaryColor
        shape = [(x1, y1), (x2, y2)]
        draw = ImageDraw.Draw(self.imageObj)
        draw.rectangle(shape, fill=color)


# # IH = ImageHandler("almonds.jpg")

# IH = ImageHandler("testImage1.png")
# IH.resizeImage()
# IH.overLayImage("basicGradient.png")
# IH.overLayImage("temp2.png")

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
# text = "Alibaba loses $60 bn m-cap after China starts anti-monopoly investigation"
# text = "US faces government shutdown as Trump threatens not to sign spending bill"
# text = "Aurobindo Pharma to make COVAXX's COVID-19 vaccine for India, UNICEF"
# text = r"Elon Reeve Musk FRS is a business magnate, industrial designer and engineer. He is the founder, CEO, CTO and chief designer of SpaceX; early investor, CEO and product architect of Tesla, Inc.; founder of The Boring Company; co-founder of Neuralink; and co-founder and initial co-chairman of OpenAI."
# text = "Narendra Chanchal is an Indian singer who specializes in religious songs and hymns."
# text = "Vansh Wadhwa is a great genius programmer , He is specialised in Python."


# IH.addText(text , atY = -170)
# IH.saveImage()
# # print(IH.fileName)


# IH.imageObj.show()
