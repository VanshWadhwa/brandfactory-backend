from instabot import Bot
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class InstagramHandler:
    
    def __init__(self ,username, password):
        self.username = username
        self.password = password
        logger.info("Instagram Instance Created")
        self.bot = Bot()
        self.bot.login(username = self.username ,password = self.password)  
        logger.info("Logged In as : " + self.username)

    def upload_photo(self , imagePath , caption = ""):
        """Upload image to instagram"""
        try :
            self.bot.upload_photo(imagePath , caption = caption)
            logger.info("Uploaded to Feed on Instagram")
        except:
            logger.exception("ERROR While uploading image to instagram")


IH  = InstagramHandler("holyc.rossschool" ,"Raman@123")
IH.upload_photo("basicGradient.png" , "A wonderfull Gradient")