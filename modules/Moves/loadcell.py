# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time
import csv
# Import the ADS1x15 module.
import Adafruit_ADS1x15

class loadcell():
    def loadcell():
        # Create an ADS1115 ADC (16-bit) instance.
        adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=5)

        # Note you can change the I2C address from its default (0x48), and/or the I2C
        # bus by passing in these optional parameters:
        # adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=5)
        # Choose a gain of 1 for reading voltages from 0 to 4.09V.
        # Or pick a different gain to change the range of voltages that are read:
        #  - 2/3 = +/-6.144V
        #  -   1 = +/-4.096V
        #  -   2 = +/-2.048V
        #  -   4 = +/-1.024V
        #  -   8 = +/-0.512V
        #  -  16 = +/-0.256V
        # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
        GAIN = 1

        data = []
        try:
            while True:
                time.sleep(0.005)
                ADC_Value = (adc.read_adc(0, gain=GAIN, data_rate=860) - 19944)/6.232
                print(ADC_Value)
                return ADC_Value
                
        except IOError as e:
            print(e)
        
        except KeyboardInterrupt:
            print("ctrl + c:")
            print("Program end")
            
        with open('data.csv', 'w', newline='') as f:
            fileWriter = csv.writer(f)
            for d in data: fileWriter.writerow([d])
        print(sum(data)/len(data))
