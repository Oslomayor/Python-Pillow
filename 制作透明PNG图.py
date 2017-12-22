# 制作透明PNG图
from PIL import Image

def transPNG(srcImageName,dstImageName):
    img = Image.open(srcImageName).convert("RGBA")
    datas = img.getdata()
    newData = list()
    # 把接近黑色的像素点的alpha通道值改为0
    for data in datas:
        if data[0] < 10 and data[1] < 10 and data[2] < 10 :
            newData.append((255,255,255,0))
        else:
            newData.append(data)
    img.putdata(newData)
    img.save(dstImageName,"PNG")

content = "D:\Python\Python36\pictures\\"
transPNG(content+"灰度Logo.jpg",content+"HDUwaLogo灰度.png")

