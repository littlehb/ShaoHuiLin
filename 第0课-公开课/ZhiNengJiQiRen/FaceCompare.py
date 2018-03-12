# 人脸比对
# 导入百度ai和opencv
import os

from aip import AipFace

# 定义常量
APP_ID = '10908241'
API_KEY = 'MnKKwD8kCghkmjuNet48V3uc'
SECRET_KEY = 'IYY8zVYIG5lIbW1nPjmOOkfHSNWzbtEZ'

# 初始化AipFace对象
client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


images = [
    get_file_content(os.getcwd()+'/Images/zhaowei_1.jpg'),
    get_file_content(os.getcwd()+'/Images/zhaowei_2.jpg'),
    get_file_content(os.getcwd()+'/Images/zhaowei_3.jpg'),
]

""" 调用人脸比对 """
result = client.match(images)

# 输出比对结果
for k in range(3):
    print("图片%s和图片%s相似度：" % (result["result"][k]["index_i"], result["result"][k]["index_j"]))
    print(result["result"][k]["score"])
