import time
import pwm_dac as pwm
import signal_generator as sg

amplitude = 5
sig_freq = 4.5
sampl_freq = 1000

try:
    dc = pwm.PWM_DAC(12, 1000, 3.29, True)

    while True:
        try:

            fx=sg.get_triangle_wave_amplitude(sig_freq, time.time())
            dc.set_voltage(fx*amplitude)
            sg.wait_for_sampling_period(sampl_freq)
        except ValueError:
                print("Это шутка что ли?! Введите нормальное число\n") 

finally:
    dc.deinit()