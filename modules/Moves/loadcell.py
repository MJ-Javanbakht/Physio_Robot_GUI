import time
import csv
import ADS1263

class loadcell():
    REF = 5.08
    ADC = ADS1263.ADS1263()
    if (ADC.ADS1263_init_ADC1('ADS1263_7200SPS') == -1):
        exit()
    ADC.ADS1263_SetMode(1)
    ADC.ADS1263_SetDiffChannal(0)


    def Force_Loadcell(self):
        while True:
            ADC_Value = self.ADC.ADS1263_GetChannalValue(0)
            if ADC_Value == "error":
                continue
            offset = 0.0577
            if(ADC_Value>>31 ==1):
                # print("ADC1 IN%d = -%lf %d" %(0, ((REF*2 - ADC_Value * REF / 0x80000000) - offset), milliseconds))  
                Force = (self.REF*2 - ADC_Value * self.REF / 0x80000000)
                
            else:
                Force = ADC_Value * self.REF / 0x7fffffff
            break
        print(Force)
        return Force
