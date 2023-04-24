# -*- coding: utf-8 -*-
import pyaudio
import viVoicecloud as vv
from sjtu.audio import findDevice

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


def asr():
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


while True:
    try:
        words = asr()
        if words == "退出。":
            break
        elif words == "点歌。":
            print("请说歌名")
            words = asr()

            from music import play_qq_music

            while True:
                try:
                    play_qq_music.play_music(words)
                except:
                    break
        elif words == "对话。":
            print("请说话")
            
            import viVoicecloud as vv
            from sjtu import analyze

            vv.Login()
            t = vv.tts()
            while 1:
                try:
                    question = input("I:")
                    json_data = vv.aiui(question)
                    print(json_data)
                    print(type(json_data))

                    answer = analyze.aiui_answer(json_data)
                    print("R:" + answer)

                    t.say(answer, voice="nannan")

                except Exception as e:
                    print(e)
                    vv.Logout()
                    break

            vv.Logout()


            import conversation
            while True:
                try:
                    words = asr()
                    conversation.conversation(words)
                except:
                    break

    except KeyboardInterrupt:
        break

vv.Logout()  # 注销
stream.close()
p.terminate()
