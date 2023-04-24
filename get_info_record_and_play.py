import pyaudio              #导入模块
p = pyaudio.PyAudio()       #实例化

def findDevice0 (name, d):
    if d == "input":
        flag = 1
    else:
        flag = 0
    num = p.get_device_count()  #获取声音设备总数
    for i in range(0, num):     #遍历声音设备 
        device = p.get_device_info_by_index(i) #获取索引号为i的设备信息
        if device.get('name') == name and device.get('maxInputChannels') == flag: #如果第i个设备是录音设备，即最大输入通道数大于0
            return device.get('index')
        else:
            continue
    return None


def findDevice(name,mode):
    if mode=="input" or mode=="i":
        check = 'maxInputChannels'       
    elif mode=="output" or mode=="o":
        check = 'maxOutputChannels'
    else:
        print ("Wrong mode! Please give a string like 'input' or 'i', 'output' or 'o'")
        return None   

    p = pyaudio.PyAudio()       
    num = p.get_device_count()     

    for i in range(0, num):          
        device = p.get_device_info_by_index(i)
        if device.get(check) >0 and name in device.get('name'):
            p.terminate()
            return i
    p.terminate()



Sample_channels = 1  #通道数
Sample_rate = 16000  #采样率
Sample_width = 2     #样本宽度
Device_index = 6     #设备索引
time_seconds = 5     #采样时间

#录音初始化
stream = p.open(
            rate=Sample_rate,
            format=p.get_format_from_width(Sample_width),
            channels=Sample_channels,
            input=True,
            input_device_index=findDevice('ac108','input'))

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

file_name = "output.wav" 

wf = wave.open(file_name, 'rb')

Sample_channels = wf.getnchannels() #通道数
Sample_rate = wf.getframerate()     #采样率
Sample_width = wf.getsampwidth()    #样本宽度
Output_index = 3                    #播放设备索引

nframes = wf.getnframes()           #样本总数
frames = wf.readframes(nframes)

wf.close()

#播放初始化
stream = p.open(
            rate=Sample_rate,
            format=p.get_format_from_width(Sample_width),
            channels=Sample_channels,
            output=True,
            output_device_index=findDevice('sysdefault','output'),
            start=True)

stream.write(frames)  #向缓存中写入frames

stream.stop_stream()    #停止播放
stream.close()          #关闭stream
p.terminate()           #终止任务