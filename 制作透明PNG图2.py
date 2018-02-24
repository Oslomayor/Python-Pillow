# 制作透明PNG图
from PIL import Image

def transPNG(srcImageName,dstImageName):
    img = Image.open(srcImageName).convert("RGBA")
    datas = img.getdata()
    newData = list()
    # 把接近白色的像素点的alpha通道值改为0
    for data in datas:
        if data[0] > 250 and data[1] > 250 and data[2] > 250 :
            newData.append([255,255,255,0])
        else:
            newData.append(data)
    # SystemError: new style getargs format but argument is not a tuple
    # 要用tuple ??
    # 上次用list没问题呀
    # 加了下面两行转换 list 中的元素为 tuple 可以工作了
    for index, item in enumerate(newData):
        newData[index] = tuple(item)
    img.putdata(newData)
    img.save(dstImageName,"PNG")

def main():
    content = "E:\MyCareer-我的职业生涯\个人简历\素材\\"
    transPNG(content+"杭州电子科技大学校徽.PNG",content+"杭州电子科技大学校徽2.PNG")

if __name__ == '__main__':
    main()
