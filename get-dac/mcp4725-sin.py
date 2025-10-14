import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(dynamic_range=5.0, address=0x61, verbose=True)
    start_time = time.time()

    while True:
        current_time = time.time() - start_time
        signal_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = signal_amplitude * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()