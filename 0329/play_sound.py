# -*- coding: utf-8 -*-

#读取wav文件
import wave          

file_name = "output.wav" 

wf = wave.open(file_name, 'rb')

Sample_channels = wf.getnchannels() #通道数
Sample_rate = wf.getframerate()     #采样率
Sample_width = wf.getsampwidth()    #样本宽度
Output_index = 3                    #播放设备索引

nframes = wf.getnframes()           #样本总数
frames = wf.readframes(nframes)

wf.close()

import pyaudio

p = pyaudio.PyAudio()#实例化

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



