import serial
import struct
import time
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
import numpy.fft as fft
import sounddevice as sd
import scipy.io.wavfile as wavf

def ardInit():
    connectedPort='/dev/cu.usbmodem101'
    return(serial.Serial(port=connectedPort, baudrate=115000))

def read():
    arduino=ardInit()
    dataArray = []

    while True:
        val = arduino.read(2)
        upkdval = struct.unpack('<h',val)[0]
        dataArray.append(upkdval)
        if len(dataArray) > 10000: #determines length of recording based on data points recorded
            break

    return(dataArray)

def wave():
    data = read()

    # converts the data to be between (-1,1)
    if max(data) > abs(min(data)):
        maxval = max(data)
    else:
        maxval = abs(min(data))
    for i in range(len(data)):
        data[i] = data[i]/maxval

    # shows a graph of the output as read by the arduino
    plt.plot(data)
    plt.show()

    samples = np.array(data)
    s_rate = 2500 #unsure what the exact sampling rate is here
    out_f = '/users/paulkullmann/Desktop/'+str(datetime.datetime.now())+'.wav'
    wavf.write(out_f,s_rate,samples.astype(np.float32))

wave()