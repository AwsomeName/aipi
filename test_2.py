import pyaudio
 
p = pyaudio.PyAudio()
  
stream = p.open(
  format=pyaudio.paInt16,
  channels=0,
  rate=16000,
  input=True,
  frames_per_buffer=1024)



