import r2r_adc1 as r2r
import time
import adc_plot as plot


dynamic_range = 3.183 
duration = 3.0     

adc = r2r.R2R_ADC(dynamic_range=dynamic_range, verbose=False)

voltage_values = []  
time_values = []      

try:
   
    start_time = time.time()

    while (time.time() - start_time) < duration:
        
        voltage = adc.get_sc_voltage()
        voltage_values.append(voltage)
        
        
        current_time = time.time() - start_time
        time_values.append(current_time)
        
        print(f"Время: {current_time:.1f}с, Напряжение: {voltage:.3f}В", end='\r')
        time.sleep(0.01)
   
 
    plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)

finally:
    adc.deinit()
