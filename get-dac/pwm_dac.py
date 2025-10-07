import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)  # Запускаем с 0% заполнения
        
    def deinit(self):
        self.pwm.stop()  # Останавливаем ШИМ
        GPIO.cleanup()  
    

    def set_voltage(self, voltage):
        self.voltage = voltage
        
        if voltage > self.dynamic_range or voltage < 0:
            print("HIHIHIHA")
        
        if 0.0 <= voltage <= self.dynamic_range:

            print(f"Коэффициент заполнения: {(voltage / self.dynamic_range) * 100}%")


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("HOHOHO")

    finally:
        dac.deinit()