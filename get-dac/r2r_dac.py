import RPi.GPIO as GPIO
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        self.number = number
        binary_number = self.dec2bin(number)
        GPIO.output(self.gpio_bits, binary_number)
        
        if self.verbose:
            print(f"Установлено число: {number}")
            print(f"Двоичное представление: {binary_number}")

    def set_voltage(self, voltage):
        self.voltage = voltage
        
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
            print("Устанавливаем 0.0 B")
            voltage = 0.0
            number = 0
        else:
            number = int((voltage / self.dynamic_range) * 255)
        
        self.set_number(number)
        
        if self.verbose:
            print(f"Установлено напряжение: {voltage:.2f} В")

    def dec2bin(self, number):
        return [int(bit) for bit in bin(number)[2:].zfill(8)]


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()