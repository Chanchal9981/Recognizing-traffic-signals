from django.shortcuts import render

# Create your views here.



from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os
from PIL import Image
import  numpy as np
model=load_model("color_classification.h5")
def image_classification(color):
    img=load_img(color,target_size=(150,150))
    img=img_to_array(img)/255
    img=np.expand_dims(img,axis=0)
    img=model.predict(img).round(3)
    print(img)
    img=np.argmax(img)
    if img == 0:
        return 'Black'
    elif img == 1:
        return 'Blue'
    elif img == 2:
        return 'Brown'
    elif img ==3:
        return 'green'
    elif img ==4:
        return 'violet'
    elif img ==5:
        return 'white'
    elif img ==6:
        return 'mix_black'
    elif img ==7:
        return 'mix_blue'
    elif img ==8:
        return 'mix_brown'
    elif img ==9:
        return 'mix_green'
    elif img ==10:
        return 'mix_orange'
    elif img ==11:
        return 'mix_red'
    elif img ==12:
        return 'mix_color'
    elif img ==13:
        return 'mix_violet'
    elif img ==14:
        return 'mix_white'
    elif img ==15:
        return 'mix_yellow'
    elif img ==16:
        return 'orange'
    elif img ==17:
        return 'red'
    elif img ==18:
        return 'mixing two or more color'
    else:
        return 'yellow'









def home(request):
    return render(request,'home.html')
def result(request):
    if request.method=="POST":
        image=request.FILES["image"]
        fs=FileSystemStorage()
        imgg=fs.save(image.name,image)
        imgg=fs.url(imgg)
        test_img='.'+imgg
        pred=image_classification(color=test_img)
        return render(request,'result.html',{"pred":pred,"user_img":imgg})

    return render(request,'result.html')