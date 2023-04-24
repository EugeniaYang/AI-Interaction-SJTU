# -*- coding: utf-8 -*-

import pyaudio
import viVoicecloud as vv
from sjtu.audio import findDevice
from gpiozero import LED
from time import sleep
import wave
import pyaudio
            
led1 = LED(17)
fan1 = LED(2)
device_in = findDevice("ac108","input")
Sample_channels = 1  
Sample_rate = 16000  
Sample_width = 2         
time_seconds = 0.5
p = pyaudio.PyAudio()
stream = p.open(
            rate=Sample_rate,
            format=p.get_format_from_width(Sample_width),
            channels=Sample_channels,
            input=True,
            input_device_index=device_in,
            start=False)

vv.Login()
ASR=vv.asr()

while True:
    try:
        ASR.SessionBegin(language='Chinese')
        stream.start_stream()
        print ('***Listening...')
        status=0
        print('1')
        while status!=3:
            print('2')
            frames=stream.read(int(Sample_rate*time_seconds),exception_on_overflow = False)
            ret,status,recStatus=ASR.AudioWrite(frames)
        print('3')
        stream.stop_stream()
        print ('---GetResult...')
        words=ASR.GetResult()
        ASR.SessionEnd()
        print (words)
        fan1.off()
        #for ch in ".,?!。，:;：；‘’“”\'\"":
        #    words = words.replace(ch,"")
        if "Luminous" in words or "Rumor" in words or "Luminous" in words or "Rumor" in words or "Room" in words: 
            print("LED on")
            led1.on()
            fan1.on()
        
        if "knox" in words or "Nox" in words or "Knox" in words:
            print("LED off")
            led1.off()

        if "Fire" in words or "fire" in words:
            print('fire!')
            file_name = "PULLUP.wav" 

            wf = wave.open(file_name, 'rb')

            Sample_channels = wf.getnchannels() #通道数
            Sample_rate = wf.getframerate()     #采样率
            Sample_width = wf.getsampwidth()    #样本宽度
            Output_index = 3                    #播放设备索引

            nframes = wf.getnframes()           #样本总数
            frames = wf.readframes(nframes)

            wf.close()

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

            
    except Exception as e:
        print(e)
        print('stopped')
        vv.Logout()
        stream.close()
        p.terminate()
        break
        







