import pyaudio
import viVoicecloud as vv
from sjtu.audio import findDevice
from sjtu import analyze
#import 2021QQMusic
from sjtu.audio import findDevice
import AIUI_t
import json
from gpiozero import LED
vv.Login()
t = vv.tts()
led1 = LED(17)

device_in = findDevice("ac108", "input")
Sample_channels = 1
Sample_rate = 16000
Sample_width = 2
time_seconds = 0.5  # 录音片段的时长，建议设为0.2-0.5秒

p = pyaudio.PyAudio()  # 实例化
stream = p.open(
    rate=Sample_rate,
    format=p.get_format_from_width(Sample_width),
    channels=Sample_channels,
    input=True,
    input_device_index=device_in,
    start=False)

vv.Login()  # 登录
ASR = vv.asr()  # 实例化

def getWordbyAsr():
    while True:
        try:
            ASR.SessionBegin(language='Chinese')  # 开始语音识别
            stream.start_stream()
            print('***Listening...')

            # 录音并上传到讯飞，当判定一句话已经结束时，status返回3
            status = 0
            while status != 3:
                frames = stream.read(int(Sample_rate * time_seconds), exception_on_overflow=False)
                ret, status, recStatus = ASR.AudioWrite(frames)
            stream.stop_stream()
            print('---GetResult...')

            words = ASR.GetResult()  # 获取结果
            ASR.SessionEnd()  # 结束语音识别
            print(words)

            return words
        
        except Exception as e:
            print (e)
            break

def getWordbyAsrEng():
    while True:
        try:
            ASR.SessionBegin(language='English')  # 开始语音识别
            stream.start_stream()
            print('***Listening...')

            # 录音并上传到讯飞，当判定一句话已经结束时，status返回3
            status = 0
            while status != 3:
                frames = stream.read(int(Sample_rate * time_seconds), exception_on_overflow=False)
                ret, status, recStatus = ASR.AudioWrite(frames)

            stream.stop_stream()
            print('---GetResult...')

            words = ASR.GetResult()  # 获取结果
            ASR.SessionEnd()  # 结束语音识别
            print(words)

            return words
        
        except Exception as e:
            print (e)
            break


print ("\n------------active------------\n")

while True:
    try:
        print ("\
            \n\
            当前位置：主菜单\n\
            \n\t可以进入以下频道：\n\
            \t说\'点歌\'\t进入音乐点播\n\
            \t说\'翻译\'\t进入翻译功能\n\
            \t说\'对话\'\t进入交互问答\n\
            \t说\'咒语\'\t进入咒语模式\n\
            \t说\'退出\'\t终止程序\
            \n\
            ")
        
        words = getWordbyAsr()
        flag = words
        
        for ch in ".,?!。，:;：；‘’“”\'\"":
            flag = flag.replace(ch,"")
        if flag == "退出":
            break

        if flag == "咒语":
            print('咒语模式，说\'返回\'返回主菜单')
            while True:
                Q = getWordbyAsrEng()

                for ch in ".,?!。，:;：；‘’“”\'\"":
                    Q = Q.replace(ch,"")

                if Q == "返回":
                    break

                try:
                    if "Luminous" in Q or "Rumors" in Q or "luminous" in Q or "rumors" in Q: 
                        led1.on()

                except Exception as e:
                    print (e)
                    break

        
        if flag == "点歌":
            print('点歌频道，说\'返回\'返回主菜单')
            while True:
                Q = getWordbyAsr()

                for ch in ".,?!。，:;：；‘’“”\'\"":
                    Q = Q.replace(ch,"")

                if Q == "返回":
                    break

                try:
                    QQMusic.play_music(Q)

                except Exception as e:
                    print (e)
                    break

        if flag == "对话":
            print('对话频道，说\'返回\'返回主菜单')
            while True:
                Q = getWordbyAsr()
                flag1 = Q

                for ch in ".,?!。，:;：；‘’“”\'\"":
                    flag1 = flag1.replace(ch,"")

                if flag1 == "返回":
                    break

                try:
                    json_data = vv.aiui(Q)
                    print(json_data)
                    print(type(json_data))

                    answer = analyze.aiui_answer(json_data)
                    print("R:" + answer)

                    t.say(answer,voice="nannan")

                except Exception as e:
                    print(e)
                    vv.Logout()
                    break

        if flag == "翻译":
            print('翻译频道，说\'返回\'返回主菜单')
            while True:
                Q = getWordbyAsr()
                flag1 = Q

                for ch in ".,?!。，:;：；‘’“”\'\"":
                    flag1 = flag1.replace(ch,"")

                if flag1 == "返回":
                    break

                try:

                    tr = vv.baidu_translate()
                    result = tr.translate(Q,"zh","en")
                    print(result)
            
                    # 合成英文并播放
                    t = vv.tts()
                    t.say(text=result, voice="john")

                except Exception as e:
                    print (e)
                    break

    except Exception as e:
        print (e)
        break

vv.Logout()  # 注销
stream.close()
p.terminate()
