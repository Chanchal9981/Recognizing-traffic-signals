from django.shortcuts import render

# Create your views here.





from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os
from PIL import Image
import  numpy as np
model=load_model("Recog_trafic.h5")
def image_classification(trafic):
    img=load_img(hollywood,target_size=(150,150))
    img=img_to_array(img)/255
    img=np.expand_dims(img,axis=0)
    img=model.predict(img).round(3)
    print(img)
    img=np.argmax(img)
    if img == 0:
        return 'Height_limit'
    elif img == 1:
        return 'No_entry'
    elif img == 2:
        return 'No_entry_or_one_way'
    elif img == 3:
        return 'Symbolic_data'
    elif img == 4:
        return 'cross_road_warning'
    elif img == 5:
        return 'dont horn'
    elif img == 6:
        return "don't parking"
    elif img == 7:
        return "don't_take_left"
    elif img == 8:
        return "don't_take_right"
    elif img == 9:
        return 'four_wheelar'
    elif img == 10:
        return 'green_light_signle'
    elif img == 11:
        return 'hospital'
    elif img == 12:
        return 'left_curve'
    elif img == 13:
        return 'lenght_limite'
    elif img == 14:
        return 'no_entry_for_cycle_&_bus'
    elif img == 15:
        return 'no_overtaking'
    elif img == 16:
        return 'one_way'
    elif img == 17:
        return 'railway_gate'
    elif img == 18:
        return 'red_light'
    elif img == 19:
        return  'right_curve'
    elif img == 20:
        return 'road_workers'
    elif img == 21:
        return 'school_gate'
    elif img == 22:
        return 'speed_limite'
    elif img == 23:
        return  'stop_sign'
    elif img == 24:
        return 'trafig_signals'
    else:
        return 'yellow_light'






def home(request):
    return render(request,'home.html')
def result(request):
    if request.method=="POST":
        image=request.FILES["image"]
        fs=FileSystemStorage()
        imgg=fs.save(image.name,image)
        imgg=fs.url(imgg)
        test_img='.'+imgg
        pred=image_classification(trafic=test_img)
        return render(request,'result.html',{"pred":pred,"user_img":imgg})
    return render(request,'result.html')
