# 融合两张图片
# RGBA模式下，一张图片映射一个列表，列表的元素是四元组(R,G,B,A)
# R = Red, G = Green, B = Blue, A = Alpha(anti-transparence)
from PIL import Image

def mergeAB(srcA,srcB,dstAB):
    imgA = Image.open(srcA).convert("RGBA")
    imgB = Image.open(srcB).convert("RGBA")
    datasA = imgA.getdata()
    datasB = imgB.getdata()
    newData = list()
    # 建立一个缓存列表
    temp = list([0,0,0,0])
    for dataA,dataB in zip(datasA,datasB):
        # 每个像素点的4通道融合
        for i in range(0,4):
            # 调节权重
            temp[i] = int(dataA[i]*0.1 + dataB[i]*0.8)
        # 图片列表的元素是四元组
        newData.append(tuple(temp))
    imgA.putdata(newData)
    #imgA.show()
    imgA.save(dstAB)

content = "D:\Python\Python36\pictures\\"
mergeAB(content+"A.jpg",content+"B.jpg",content+"AB.png")
        
