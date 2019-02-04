#!/usr/bin/python3

"""
Purpose: Display analog input data from Arduino using Python (matplotlib)
                 via serial port.

Author: David Rower
Date: Febuary 3, 2019
"""

import sys, serial, time
import numpy as np
import matplotlib.pyplot as plt

def main():

    # Sampling Parameters
    time_to_collect = 0.01 # seconds
    sample_rate_khz = 38.5 # kHz
    sample_dt = 1./(1000*sample_rate_khz) # seconds
    samples   = []
    print("Will be sampling for %fms" % (time_to_collect*1000))
    print("Arduino sample rate: %fkHz" % sample_rate_khz)
    print("Corresponding dt: %fms" % (sample_dt*1000))

    # Arduino Port
    strPort = '/dev/ttyACM0'
    ser = serial.Serial(strPort, 115200)

    # Collect samples within interval [0, time_to_collect)
    net_time_sampled = 0
    while net_time_sampled < time_to_collect:
        line = ser.readline()
        try:
            samples.append(float(line))
            net_time_sampled += sample_dt
        except:
            # Sometimes we are fed an empty line, ignore these
            pass

    print("Sampled %d points." % len(samples))

    # Plot our samples
    fig = plt.figure()
    ax  = plt.axes(ylim=(0, 1023))
    plt.plot(np.linspace(0,time_to_collect, len(samples)), samples)
    plt.xlabel("Time (s)")
    plt.ylabel("Analog Input")
    plt.title("Analog Input to Arduino, Sample Rate: %.1fkHz" % sample_rate_khz)
    plt.show()

    # Close serial connection
    ser.flush()
    ser.close()

if __name__ == '__main__':
    main()
