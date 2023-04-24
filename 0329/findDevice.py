# -*- coding: utf-8 -*-
def findDevice(name,d)
    import pyaudio  # 导入模块

    p = pyaudio.PyAudio()  # 实例化

    num = p.get_device_count()  # 获取声音设备总数
    index = 0
    for i in range(0, num):  # 遍历声音设备

        device = p.get_device_info_by_index(i)  # 获取索引号为i的设备信息
        # print(device)

        if (device.get('maxInputChannels') > 0 &&& ):  # 如果第i个设备是录音设备，即最大输入通道数大于0

            print('Input index:' + str(i) + ' name:' + device.get('name') + '\n')

        if device.get('maxOutputChannels') > 0:  # 如果第i个设备是播放设备，即最大输出通道数大于0

            print('Output index:' + str(i) + ' name:' + device.get('name') + '\n')

            return index



