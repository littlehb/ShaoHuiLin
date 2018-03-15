# 人脸识别
from aip import AipFace
import cv2

# 定义常量
APP_ID = '10908241'
API_KEY = 'MnKKwD8kCghkmjuNet48V3uc'
SECRET_KEY = 'IYY8zVYIG5lIbW1nPjmOOkfHSNWzbtEZ'

# 初始化AipFace对象
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "./Images/zhaowei_1.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 定义参数变量
options = {
    'max_face_num': 1,
    'face_fields': "age,beauty,expression,faceshape",
}
# 调用人脸属性检测接口
result = aipFace.detect(get_file_content(filePath), options)

# 解析位置信息
location = result['result'][0]['location']
left_top = (location['left'], location['top'])
right_bottom = (left_top[0] + location['width'], left_top[1] + location['height'])

img = cv2.imread(filePath)
cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 2)

print("美丑打分：", result["result"][0]["beauty"])
print("年龄：", result["result"][0]["age"])

cv2.imshow('w', img)
cv2.waitKey(0)
