import os
import uuid
import wave, base64
import pyaudio, json, urllib
from aip import AipSpeech

# 注册的baidu帐号
APP_ID = '10892266'
API_KEY = '1qVkEPMsjr7G0lswIqqDegHT'
SECRET_KEY = 'fa292bdfcc5c634d15f079618451ed42'
client = None

asr_server = 'http://vop.baidu.com/server_api'
baidu_oauth_url = 'https://openapi.baidu.com/oauth/2.0/token/'
mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]


def get_token():
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_KEY + "&client_secret=" + SECRET_KEY;
    res = urllib.request.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']


access_token = get_token()


# 转化mp3为wav,防止版权问题
def ConvertMp3ToWav(source, target):
    cmd = os.getcwd() + r'\ffmpeg\ffmpeg.exe  -y -i  ' + source + ' ' + target
    os.system(cmd)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


class BaiduAiUtil:

    @staticmethod
    def PlaySoundByText(speakString):
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        # 调用百度进行生成语音
        result = client.synthesis(speakString, 'zh', 1, {
            'vol': 5,
        })
        # 保存文件
        file = 'weather.mp3'
        if not isinstance(result, dict):
            with open(file, 'wb') as f:
                f.write(result)
            # 转成wave
            ConvertMp3ToWav(os.getcwd() + '\\' + file, os.getcwd() + '\\' + file.replace('.mp3', '.wav'))

            # 定义数据流块
            chunk = 1024
            # 只读方式打开wav文件
            f = wave.open(os.getcwd() + '\\' + file.replace('.mp3', '.wav'), "rb")
            p = pyaudio.PyAudio()
            # 打开数据流
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)
            # 读取数据
            data = f.readframes(chunk)
            # 播放
            while len(data)>0:
                stream.write(data)
                data = f.readframes(chunk)

            # 停止数据流
            stream.stop_stream()
            stream.close()

    @staticmethod
    def GetTextFromSound(speech_file):
        with open(speech_file, 'rb') as f:
            speech_data = f.read()
        speech_base64 = base64.b64encode(speech_data).decode('utf-8')
        speech_length = len(speech_data)
        data_dict = {'format': 'wav', 'rate': 8000, 'channel': 1, 'cuid': mac_address, 'token': access_token,
                     'lan': 'zh',
                     'speech': speech_base64, 'len': speech_length}
        json_data = json.dumps(data_dict).encode('utf-8')
        json_length = len(json_data)

        request = urllib.request.Request(url=asr_server)
        request.add_header("Content-Type", "application/json")
        request.add_header("Content-Length", json_length)
        fs = urllib.request.urlopen(url=request, data=json_data)

        result_str = fs.read().decode('utf-8')
        json_resp = json.loads(result_str)
        return json_resp
