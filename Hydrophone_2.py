import serial
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

    #reads each sample data into an array
    while True:
        if arduino.in_waiting:
            try:
                val = float(arduino.readline().decode('utf-8').strip())
                dataArray.append(val)
                if len(dataArray) > 10000:
                    print("done")
                    break
            except ValueError:
                print("value error")
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
    s_rate = 2000 #unsure what the sampling rate is here... i've been trying to maximize the sampling rate to no avail.
    out_f = '/users/paulkullmann/Desktop/'+str(datetime.datetime.now())+'.wav'
    wavf.write(out_f,s_rate,samples.astype(np.float32))

wave()