import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac_bits, GPIO.OUT)
GPIO.output(dac_bits, 0)
dynamic_range = 3.3
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.number = 0
        self.voltage = 0


        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.clenup()

    def set_number(self, number):
        self.number = number
    def set_voltage(self, voltage):
        self.voltage = voltage
    def dec2bin(number):
        return [int(bit) for bit in bin(number)[2:].zfill(8)]

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        voltage = 0.0
        return 0

if __name__=="__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))

                if not (0.0 <= voltage <= dynamic_range):
                    print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
                    print("Устанавливаем 0.0 B")
                    voltage = 0
                    number = 0
                else:
                    number = int((voltage/3.183) * 255)
                
                dac.set_voltage(voltage)
                number = int((voltage/3.183) * 255)
                dac.set_number(number)
                binary_number = PWM_DAC.dec2bin(number)
                GPIO.output(dac_bits, binary_number)
                print(PWM_DAC.dec2bin(number))
    

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз \n")

    finally:
        dac.deinit()
