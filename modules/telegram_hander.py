import requests
import logging
from urllib.parse import quote

        # ' ' => '%20',    '!' => '%21',    '"' => '%22',
        # '#' => '%23',    '$' => '%24',    '%' => '%25',
        # '&' => '%26',    '\'' => '%27',   '(' => '%28',
        # ')' => '%29',    '*' => '%2A',    '+' => '%2B',
        # ',' => '%2C',    '-' => '%2D',    '.' => '%2E',
        # '/' => '%2F',    ':' => '%3A',    ';' => '%3B',
        # '<' => '%3C',    '=' => '%3D',    '>' => '%3E',
        # '?' => '%3F',    '@' => '%40',    '[' => '%5B',
        # '\\' => '%5C',   ']' => '%5D',    '^' => '%5E',
        # '_' => '%5F',    '`' => '%60',    '{' => '%7B',
        # '|' => '%7C',    '}' => '%7D',    '~' => '%7E',
    

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')



file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class TelegramHandler:
# almonds.jpg
# "chat_id":"-426705193"
    # botToken = "1485711665:AAFrs9EGdknjUiVDFWkM36ZkSZcSlt5gDHY"
    # chat_id  = "-426705193"
    
    def __init__(self ,botToken , chat_id):
        self.chat_id = chat_id
        self.botToken = botToken
        logger.info("TelegramHandler Instance Created")

    def optimiseForTelegram(self , text):
        """Optimise the text for caption for https response"""
        # return quote(text , safe='')
        # return text
        text = text.replace("%", "%25")
        text = text.replace("#", "%23")
        text = text.replace("$", "%24")
        text = text.replace("&" , "%26")
        #  # '&' => '%26',
        return text
        
    def sendMessage(self , text):
        """Sends a text message"""
        try:
            url = "https://api.telegram.org/bot"+ self.botToken+"/sendMessage"
            # text = self.optimiseForTelegram(text)
            payload = {"chat_id": self.chat_id , "text" : text}
            r = requests.get(url  , params = payload)
            
            logger.info("Message Sent")         
            logger.debug("Text : " + text)         
        except:
            logger.exception("Error While Sending Message")




    def sendPhoto(self , photo , caption = ""):
        """Send the Photo the telegram can work with caption"""
        try:
            photo  = {'photo':open(photo , "rb")}
            url = 'https://api.telegram.org/bot' + self.botToken + '/sendPhoto?chat_id=' + self.chat_id
            
            if caption != "":
                caption = self.optimiseForTelegram(caption)

                url = url + "&caption="+caption
    
            r = requests.post(url , files = photo)
            logger.info("Image Sent")    
            logger.debug("Text : " + caption)         

        except:
            logger.exception("Error While Sending Image")

# th = TelegramHandler("1485711665:AAFrs9EGdknjUiVDFWkM36ZkSZcSlt5gDHY" ,"-426705193" )
# th.sendMessage("hi")
# th.sendPhoto("./almonds.jpg")



# def test(text):
#     # removeSpecialChars = z.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}
#     # print(quote("hello%h"))
#     # print(quote_plus(text))
#     pass

# test("Bank of Maharashtra Q3 net climbs by 13.9% at Rs 154 crore")

# TH = TelegramHandler("1485711665:AAFrs9EGdknjUiVDFWkM36ZkSZcSlt5gDHY" , "-426705193")
# TH = TelegramHandler("1560307455:AAFzL08q4m3MkxVDRHWe99PWCCczUBb_VQU" , "-1001432550139") # channel ID pass word for 
# TH = TelegramHandler("1560307455:AAFzL08q4m3MkxVDRHWe99PWCCczUBb_VQU" , "-1001488732517") # channel ID pass word for 
# # # 
# TH.sendMessage("Bank of Maharashtra Q3 % net climbs by 13.9 # at Rs 154 crore")
# TH.sendMessage("Hi")
# TH.sendPhoto("basicGradient.png" , """66% of small businesses w#ill outsource services to other small businesses.

#  For More Updates Follow : 
#   t.me/Inclined_Entrepreneur 

# #Inclined_Entrepreneur #Inclined_Entrepreneur_Fact""")

# # test("http://google.com/")
