# python百度ai的身份证识别代码
from aip import AipOcr
import os
# 定义常量
APP_ID = '10908207'
API_KEY = 'x4kTCeUjDOM0SNnB106WkGGv'
SECRET_KEY = 'DHSAwwDrj5VuukhHbT1znjxPfGI8jef6'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content(os.getcwd()+'/Images/IdentityCard.jpg')  # 将左侧括号内1.jpg替换为待识别的图片路径
idCardSide = "front"
""" 调用身份证识别 """
result = client.idcard(image, idCardSide)
print("姓名：", result["words_result"]["姓名"]["words"])
print("性别：", result["words_result"]["性别"]["words"])
print("民族：", result["words_result"]["民族"]["words"])
print("生日：", result["words_result"]["出生"]["words"])
print("身份证号：", result["words_result"]["公民身份号码"]["words"])
print("住址：", result["words_result"]["住址"]["words"])
