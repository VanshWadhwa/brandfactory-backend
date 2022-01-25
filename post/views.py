from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

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
        print('request.data : ', request.data)
        print('request.data type: ', type(request.data))
        requestDataDict = request.data.dict()
        print('requestDataDict  type: ', type(requestDataDict))


        posts_serializer = PostSerializer(data=request.data)

        # if posts_serializer.is_valid():

        print("hey ----->")
        # print(posts_serializer)
        # createTemp1()

        # posts_serializer.save()

        # title = requestDataDict['title']
        # imageLocation = requestDataDict['image']

        imageFrom= requestDataDict['imageFrom'],
        title=requestDataDict['title'],
        content= requestDataDict['content'],
        imageLocation= requestDataDict['image'],
        print('imageLocation : ' , imageLocation)
        imageURL=requestDataDict['imageURL'],
        cropType= requestDataDict['cropType'],
        isAddGradient= requestDataDict['isAddGradient'] == 'true',
        isAddBranding= requestDataDict['isAddBranding'] == 'true',
        isAddTitleText= requestDataDict['isAddTitleText'],
        titleTextPosition=requestDataDict['titleTextPosition'],
        titleTextAlignment=requestDataDict['titleTextAlignment'] ,
        isContainImportantWords= bool(requestDataDict['isContainImportantWords'] == 'true'),
        # savedFilename=requestDataDict['savedFilename'],
        imgType = type(imageLocation)

        

        print("type : " , type(isAddGradient))

        # a , b  , importantWords , location = createTemp2(title,imageLocation)
        # filename = imageLocation[0].split('/')[-1].split('.')[0] + "." + imageLocation[0].split('/')[-1].split('.')[1]
        # print("filename : " , )
        # filename = url.split('/')[-1].split('.')[0] + "."

        # print('filename : ', filename)
        # ID.downloadImage(filename, url)

        # pathOfImage 
        # filename = url

        # filepath =  filename
        # filepath = "\\media\\post_images\\" + filename




        # print('Filename : ' , filename)

        IH = ImageHandler(imageLocation[0])


        # IH.secondaryColor = (49, 188, 238)
        IH.resizeImage(type = cropType[0])
        # IH.resizeImage()
        print("IDK WHAT 0: " , bool(isAddGradient[0]))
        print("IDK WHAT 1: " , bool(isAddGradient))
        print("IDK WHAT 2: " , isAddGradient[0])
        print("IDK WHAT 2: " , type(isAddGradient[0]))


        print("IDK WHAT 3: " , isAddGradient)


        if isAddGradient[0] :

            print("adding gradient")
            IH.overLayImage("\\assets\\images\\basicGradient.png")
        if isAddBranding[0] :
            IH.overLayImage("\\assets\\images\\temp1.png")

        # titleTextX , titleTextY 

        print("isContainImportantWords : " , isContainImportantWords[0])
        print("isContainImportantWords type : " , type(isContainImportantWords[0]))

        importantWords = IH.addText(
            title[0], fontSize=5, atY=-170, containsImportantWords=isContainImportantWords[0] ,  returnImportantWords=[0], alignment=titleTextAlignment[0])
        finalPath = IH.saveImage()

        del IH
        savedFilename = imageLocation[0].name
        location = '/output/' + savedFilename
        
        print("savedFilename :::::>> " , savedFilename)

        


        print("created post")
        # posts_serializer.save()

        # return Response(request.data, status=status.HTTP_201_CREATED)
        print('request.data : ', request.data)

        short_report = open(finalPath, 'rb')
        report_encoded = base64.b64encode(short_report.read())
        # return Response({'detail': 'this works',
        # 'report': report_encoded})
        

        res =     {'status':'200' , 'importantWords' : importantWords , 'imgLocation' : location , 'report': report_encoded , 'savedFileName' : savedFilename }
        
        short_report.close()
        
        os.remove(finalPath)

        return Response( res, status=status.HTTP_201_CREATED ,  content_type="image/jpeg")

        # else:
        #     print('error', posts_serializer.errors)
        #     return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
