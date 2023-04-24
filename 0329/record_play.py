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
#p.terminate()           #终止任务

#
# #写入wav文件
# import wave          #导入wave,用于读写wav文件
#
# file_name = "output.wav" #wav文件输出路径
#
# wf = wave.open(file_name, 'wb')
# wf.setnchannels(Sample_channels)
# wf.setsampwidth(Sample_width)
# wf.setframerate(Sample_rate)
# wf.writeframes(frames)
# wf.close()

###############################################################################################################3

# -*- coding: utf-8 -*-

#读取wav文件
# import wave
#
# file_name = "output.wav"
#
# wf = wave.open(file_name, 'rb')
#
# Sample_channels = wf.getnchannels() #通道数
# Sample_rate = wf.getframerate()     #采样率
# Sample_width = wf.getsampwidth()    #样本宽度
Output_index = 3                    #播放设备索引
#
# nframes = wf.getnframes()           #样本总数
# frames = wf.readframes(nframes)
#
# wf.close()

#import pyaudio

#p = pyaudio.PyAudio()#实例化

#播放初始化
stream = p.open(
            rate=Sample_rate,
            format=p.get_format_from_width(Sample_width),
            channels=Sample_channels,
            output=True,
            output_device_index=Output_index,
            start=True)

stream.write(frames)  #向缓存中写入frames

stream.stop_stream()    #停止播放
stream.close()          #关闭stream
p.terminate()           #终止任务



