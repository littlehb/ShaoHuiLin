from aip import AipOcr
import os

# 初始化AipFace对象
APP_ID = '10908207'
API_KEY = 'x4kTCeUjDOM0SNnB106WkGGv'
SECRET_KEY = 'DHSAwwDrj5VuukhHbT1znjxPfGI8jef6'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content(os.getcwd() + '/Images/RankCard.jpg')  # 将左侧括号内3.jpg替换为待识别的图片路径
# 调用银行卡识别
result_bank = client.bankcard(image)
print("银行卡号：", result_bank["result"]["bank_card_number"])
print("发卡银行：", result_bank["result"]["bank_name"])
