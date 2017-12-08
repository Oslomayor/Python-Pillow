#图片多阶嵌套
from PIL import Image
#图片路径
content = 'D:\Python\Python36\pictures'
#同一张jpg图片，命名为girl时能打开，命名为boy却打不开
img = Image.open(content+'\boy.jpg')
img.show()
imgg = img
box = (0,0,640,640)
region = imgg.crop(box)
for i in range(0,3):
    region = region.resize((640-i*200,640-i*200))
    box = (i*100,i*100)
    imgg.paste(region,box)
imgg.show()

#imgg.save(content+'\wetchat3.jpg')
