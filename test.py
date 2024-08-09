import sounddevice as sd
 
# 设定要录制的秒数
duration = 5  # 录制时间为5秒
 
# 打开麦克风，采样率为44.1kHz，16位深度，单声道
with sd.InputStream(samplerate=44100, channels=1, dtype='int16') as stream:
    print("开始录制...")
    # 从麦克风读取数据，时长为duration秒
    my_recording = stream.read(duration * stream.samplerate)
 
# 如果需要，可以将录制的数据保存为文件
# sd.play(my_recording, samplerate=44100, channels=1)
# sd.wait()  # Wait until file is done playing
 
# 如果需要进一步处理音频数据，可以对my_recording进行操作
