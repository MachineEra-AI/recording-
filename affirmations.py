import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100 #sample rate
seconds =  15 # Duration of recording

myrecording = sd.rec(int(seconds * fs),samplerate = fs ,channels = 2)
print('waiting for your recording')
sd.wait() #wait until recording is finished
write('output.wav',fs,myrecording) # save as wav file

