import urllib.request
from Util.BaiduAiUtil import *


# 获取天气
def getWeather():
    ApiUrl = "http://www.weather.com.cn/data/sk/101060101.html"
    html = urllib.request.urlopen(ApiUrl)
    # 读取并解码
    data = html.read().decode("utf-8")
    # 将JSON编码的字符串转换回Python数据结构
    ss = json.loads(data)
    info = ss['weatherinfo']
    return info


if __name__ == '__main__':
    # 获取天气信息
    info = getWeather()
    speakString = '现在播报天气：城市,%s' % info['city']
    speakString = speakString + (' ,温度：%s度' % info['temp'])
    speakString = speakString + (',风速：%s' % info['WD'])
    speakString = speakString + info['WS']
    speakString = speakString + (',湿度：%s' % info['SD'])
    speakString = speakString + (',天气播报完毕！')
    print(speakString)
    BaiduAiUtil.PlaySoundByText(speakString)
