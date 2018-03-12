import requests
import time

from Util.BaiduAiUtil import *
from Util.RecordUtil import *

while True:
    try:
        # 录制
        r = RecordUtil()
        r.recoder()
        WorkingWave = os.getcwd() + r'\weather.wav'
        r.savewav(WorkingWave)

        # 百度识别
        question = BaiduAiUtil.GetTextFromSound(WorkingWave)['result'][0]
        print(question)

        # 传给机器人
        url = 'http://api.chatbot.cn/cloud/robot/5aa28b810d00008b2baa8545/answer?channel=app&userId=5aa28b810d00008b2baa8545' \
              '&sessionId=0&question= '
        r = requests.get(url + question)
        returnStr = str(r.json()['answers'][0]['respond']).replace('<p>', '').replace('</p>', '')
        print(returnStr)

        # 上传到百度语音合成并输出
        BaiduAiUtil.PlaySoundByText(returnStr)
        # 小林有点笨
        print('休息3秒后再说！')
        time.sleep(3)
    except Exception as err:
        print('发生了错误：' + str(err))
        continue
