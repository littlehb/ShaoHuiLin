#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

# 指定GPIO口的选定模式为GPIO引脚编号模式（而非主板编号模式）
RPi.GPIO.setmode(RPi.GPIO.BCM)

# 指定GPIO14（就是LED长针连接的GPIO针脚）的模式为输出模式
# 如果上面GPIO口的选定模式指定为主板模式的话，这里就应该指定8号而不是14号。
RPi.GPIO.setup(14, RPi.GPIO.OUT)

# 循环10次
for i in range(0, 10):
    # 让GPIO14输出高电平（LED灯亮）
    RPi.GPIO.output(14, True)
    # 持续一段时间
    time.sleep(0.5)
    # 让GPIO14输出低电平（LED灯灭）
    RPi.GPIO.output(14, False)
    # 持续一段时间
    time.sleep(0.5)

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
RPi.GPIO.cleanup()


