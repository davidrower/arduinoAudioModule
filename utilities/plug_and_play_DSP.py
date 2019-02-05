#!/usr/bin/python3

"""
Purpose: Provide a simple plug-and-play environment to test and debug DSP
         algorithms.

Author: David Rower
Date: Febuary 4, 2019
"""
print(__doc__ + "="*80)

import numpy as np
import matplotlib.pyplot as plt

def input_signal(t):
    frequency = 440 # Hz
    w = frequency * 2. * np.pi # angular frequency, rad/s
    A = 5 # Volts, similar to a Eurorack audio signal.
    return A * np.sin(w*t)

def output_signal(t, history):
    #return history[0] # a simple follower
    return history[0] - history[1] # difference

def main():

    # Sampling Parameters and Input Signal
    total_sample_time = 0.01 # s
    sample_rate_khz   = 38.5 # kHz
    sample_dt         = 1./(1000*sample_rate_khz) # seconds
    sample_times      = np.linspace(0,total_sample_time, total_sample_time/sample_dt)
    input_samples     = input_signal(sample_times)
    output_samples    = np.zeros_like(input_samples)

    print("Will be sampling for %fms" % (total_sample_time*1000))
    print("Sample Rate: %fkHz" % sample_rate_khz)
    print("Corresponding dt: %fms" % (sample_dt*1000))
    print("Sampled %d points." % len(input_samples))

    # Keep buffer of most recent input samples, ignore starting effects
    n_history = 4 # keep track of the last 4 samples
    buff = np.zeros(n_history) # [s(t), s(t-1), s(t-2), s(t-3)]

    # Let's get jiggy wit it
    for index, input_signal_sample in enumerate(input_samples):
        # most recent samples in buffer
        buff = np.roll(buff, 1); buff[0] = input_signal_sample

        # DSP algorithms loose a lot of cool properties when they depend on t
        t = sample_times[index] # current time
        output_samples[index] = output_signal(t, buff)

    # Plot our samples
    fig = plt.figure()
    plt.xlim([sample_times[0],sample_times[-1]])
    plt.ylim([-6,6]) # Eurorack goes between -5 and 5 V
    plt.plot(sample_times, input_samples, label="Input")
    plt.plot(sample_times, output_samples, label="Output")
    plt.xlabel("Time (s)")
    plt.ylabel("Signal Level (V)")
    plt.title("Input and Output Signals, Sample Rate: %.1fkHz" % sample_rate_khz)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
