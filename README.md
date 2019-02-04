# arduinoAudioModule

Code to go along with making a Eurorack module with an Arduino.
You'll a few useful Python utilities for plotting Arduino serial output,
prototyping digital signal processing (DSP) algorithms, and corresponding
Arduino sketches for implementing various algorithms. In due time.

## Eurorack Compatibility

To make our module compatible with the Eurorack format, we must accept input
audio signals of $\pm 5V$, and massage them to the Arduino-preferred $0-5V$ for
the analog input channels. This involved some straight-forward op-amp circuitry and
a voltage divider to bias the signal. I used these components:
* [Op-Amp](https://www.digikey.com/product-detail/en/texas-instruments/TL074BCN/296-7197-5-ND/378416){:target="_blank"},
* [8-Bit DAC](https://www.digikey.com/product-detail/en/analog-devices-inc/AD7524JNZ/AD7524JNZ-ND/819882){:target="_blank"},
* [Resistors](https://www.digikey.com/product-detail/en/stackpole-electronics-inc/RNF14FTD10K0/RNF14FTD10K0CT-ND/1975090){:target="_blank"},
* [Caps](https://www.digikey.ie/product-detail/en/tdk-corporation/FK18X5R1C225K/445-8407-ND/2815337){:target="_blank"}.

## Python Utilities

In order to test and debug DSP algorithms, I created a little plug-and-play
script in Python, found in the utilities directory. I also created some tools to
plot the serial output from the Arduino, both in real time and by sampling for
a certain time interval.

## License
[MIT](https://choosealicense.com/licenses/mit/)
