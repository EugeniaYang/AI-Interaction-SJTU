# -*- coding: utf-8 -*-

import pyaudio       #导入pyaudio

Sample_channels = 1  #通道数
Sample_rate = 16000  #采样率
Sample_width = 2     #样本宽度
Device_index = 6     #设备索引
time_seconds = 5     #采样时间

p = pyaudio.PyAudio()#实例化

#录音初始化
stream = p.open(
            rate=Sample_rate,
            format=p.get_format_from_width(Sample_width),
            channels=Sample_channels,
            input=True,
            input_device_index=Device_index)

stream.stop_stream()    #停止录音

print("* recording")    

stream.start_stream()   #开始录音

frames = stream.read(Sample_rate*time_seconds)  #从缓存中读取一段波形数据

print("* done recording")

stream.stop_stream()    #停止录音
stream.close()          #关闭stream
p.terminate()           #终止任务


#写入wav文件
import wave          #导入wave,用于读写wav文件

file_name = "output.wav" #wav文件输出路径

wf = wave.open(file_name, 'wb')
wf.setnchannels(Sample_channels)
wf.setsampwidth(Sample_width)
wf.setframerate(Sample_rate)
wf.writeframes(frames)
wf.close()
