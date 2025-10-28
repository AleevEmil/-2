import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False, show_leds=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.show_leds = show_leds
        
       
        self.bits_gpio = [16, 20, 19, 16, 13, 12, 25, 11] 
        self.comp_gpio = 21
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        binary_number = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, binary_number)
        
        if self.verbose:
            print(f"Подано число на ЦАП: {number} -> {binary_number}")

    def sequential_counting_adc(self):
        print("Начало преобразования АЦП...")
        
        for number in range(256):
            self.number_to_dac(number)

        print("Достигнуто максимальное значение 255")
        return 255

    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()
        voltage = (digital_value / 255.0) * self.dynamic_range
        if not self.show_leds:
            self.number_to_dac(0)
        
        return voltage


if __name__ == "__main__":
    try:
        
        show_leds = True
        compare_time = 0.3
        adc = R2R_ADC(dynamic_range=3.183, compare_time=compare_time, verbose=True,show_leds=show_leds)
        measurement_count = 0
        while True:
            measurement_count += 1
            print(f"\n📊 Измерение #{measurement_count}")
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            
            # В быстром режиме - пауза между измерениями
            if not show_leds:
                time.sleep(1)


    finally:
        # Вызываем деструктор
        adc.deinit()