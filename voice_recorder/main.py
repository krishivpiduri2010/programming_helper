from tkinter.simpledialog import askinteger
from tkinter import *
import pyaudio
import wave

win = Tk()
file_name = Entry(win)
Label(win, text='file name').pack()
file_name.pack()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


def record_voice(seconds):
    WAVE_OUTPUT_FILENAME = file_name.get() + '.wav'
    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


seconds = askinteger('Input', 'How long do you want your recording to last (Seconds)')
Button(win, text='Record', command=lambda :record_voice(seconds)).pack()
mainloop()
