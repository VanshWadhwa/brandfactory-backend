from distutils.command.upload import upload
import profile
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from users.models import Profile
import pathlib


import os
import base64

from modules.image_handler import ImageHandler
from modules.image_downloader import ImageDownloader

from modules.main import createTemp1 , createTemp2
# Create your views here.

ID = ImageDownloader()



class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
     
        requestDataDict = request.data.dict()
        id = request.user.id
        username = request.user.username

        if id is not None:
            prof = Profile.objects.get(id = id)
        else:
            print("id is none  id : " , id)


        posts_serializer = PostSerializer(data=request.data)


        imageFrom= requestDataDict['imageFrom'],
        title=requestDataDict['title'],
        content= requestDataDict['content'],
        print("1")

        try:
            imageLocation= requestDataDict['image'],
        except:
            imageLocation= ''

        imageURL=requestDataDict['imageURL'],
        cropType= requestDataDict['cropType'],
        temp= requestDataDict['temp'],#template type
        isAddGradient= requestDataDict['isAddGradient'] == 'true',
        isAddBranding= requestDataDict['isAddBranding'] == 'true',
        isAddTitleText= requestDataDict['isAddTitleText'],
        titleTextPosition=requestDataDict['titleTextPosition'],
        titleTextAlignment=requestDataDict['titleTextAlignment'] ,
        isContainImportantWords= bool(requestDataDict['isContainImportantWords'] == 'true'),
        imgType = type(imageLocation)
        savedFilename = ''
        print("2")

        # if (imageFrom[0] == "upload"):
        #     savedFilename = imageLocation[0].name
        #     IH = ImageHandler(imageLocation[0] , primaryColor=prof.primaryColor , secondaryColor= prof.secondaryColor)

        # elif(imageFrom[0] == "url"):
        #     filename = imageURL[0].split('/')[-1].split('.')[0] + ".png"

        #     savedFilename = filename

        #     ID.downloadImage(filename, imageURL[0])
        
        #     IH = ImageHandler( str(filename))

        # else:
        #     print('Invalid image upload type')

        print("3")



        if temp[0] == "temp1":
            # template 1 selected
            if (imageFrom[0] == "upload"):
                savedFilename = imageLocation[0].name
                IH = ImageHandler(imageLocation[0] , primaryColor=prof.primaryColor , secondaryColor= prof.secondaryColor)

            elif(imageFrom[0] == "url"):
                filename = imageURL[0].split('/')[-1].split('.')[0] + ".png"
    
                savedFilename = filename

                ID.downloadImage(filename, imageURL[0])
        
                IH = ImageHandler( str(filename))

            else:
                print('Invalid image upload type')

            IH.resizeImage(type = cropType[0])



            if isAddGradient[0] :
                IH.overLayImage("\\assets\\images\\basicGradient.png")
            if isAddBranding[0] :
                IH.overLayImage("\\assets\\images\\"+username+"\\tempImage1.png")

            importantWords = IH.addText(
                title[0], fontSize=5, atY=-170, containsImportantWords=isContainImportantWords[0] ,  returnImportantWords=[0], alignment=titleTextAlignment[0])
            finalPath = IH.saveImage()

            del IH
            location = '/output/' + savedFilename
            print("4")

            short_report = open(finalPath, 'rb')
            report_encoded = base64.b64encode(short_report.read())

            res =     {'status':'200' ,"msg" : "Post created", 'importantWords' : importantWords , 'imgLocation' : location , 'report': report_encoded , 'savedFileName' : savedFilename }
            
            short_report.close()
            
            os.remove(finalPath)

            print("5")

            try:
                if (imageFrom[0] == "url"):
                    os.remove(str(pathlib.Path('.').cwd()) + "\\assets\\images\\" + savedFilename)
                    print("removed")
            except Exception as e :
                print(e)

            print("6")
            return Response(res, status=status.HTTP_200_OK ,  content_type="image/jpeg")
            print("7")
        elif temp[0] == "temp2":
            # template 2 selected
            IH = ImageHandler("BG.png")
            IH.resizeImage(x=1080, y=1080)

            if (imageFrom[0] == "upload"):
                savedFilename = imageLocation[0].name
                filename = imageLocation[0].name
                IH2 = ImageHandler(imageLocation[0] , primaryColor=prof.primaryColor , secondaryColor= prof.secondaryColor)

            elif(imageFrom[0] == "url"):
                filename = imageURL[0].split('/')[-1].split('.')[0] + ".png"
    
                savedFilename = filename

                ID.downloadImage(filename, imageURL[0])
        
                IH2 = ImageHandler( str(filename))

            else:
                print('Invalid image upload type')


            IH2.resizeImage(x=1020, y=600, type="centre")
            IH2.saveImage(filename, path="\\assets\\images\\")
            del IH2

            IH.overLayImage("\\output\\"+filename, atX=30, atY=30)
            IH.primaryColor = (255, 255, 255)
            IH.overLayImage("assets\\images\\"+username+"\\defaultLogo.png", atX=475, atY=550)
            importantWords = IH.addText(title[0], fontSize=4, fontPath="assets/fonts/Merriweather-Bold.ttf",
                                        atY=-240, containsImportantWords=True, returnImportantWords=True)

            importatWords = IH.addText(content[0], fontSize=2,
                    fontPath="assets/fonts/Merriweather-Regular.ttf",  atY=-100)
            finalPath = IH.saveImage(filename)

            del IH
            location = '/output/' + savedFilename
            print("4")

            short_report = open(finalPath, 'rb')
            report_encoded = base64.b64encode(short_report.read())

            res =     {'status':'200' ,"msg" : "Post created", 'importantWords' : importantWords , 'imgLocation' : location , 'report': report_encoded , 'savedFileName' : savedFilename }
            
            short_report.close()
            
            os.remove(finalPath)

            print("5")

            try:
                if (imageFrom[0] == "url"):
                    os.remove(str(pathlib.Path('.').cwd()) + "\\assets\\images\\" + savedFilename)
                    print("removed")
            except Exception as e :
                print(e)

            print("6")
            return Response(res, status=status.HTTP_200_OK ,  content_type="image/jpeg")
        elif temp == "temp3":
            pass

        return Response( {"status":"400" , "msg" : "bad request served"}, status=status.HTTP_400_BAD_REQUEST ,  content_type="image/jpeg")
