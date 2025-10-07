import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        self.bus = smbus.SMBus(1)
        
        self.address = address
        self.wm = 0x40
        self.pds = 0x00
        
        self.verbose = verbose
        self.dynamic_range = dynamic_range
        
        # Проверка подключения устройства
        try:
            self.bus.read_byte(self.address)
            if self.verbose:
                print(f"MCP4725 найден по адресу 0x{self.address:02X}")
        except OSError:  # Исправлено: конкретное исключение вместо bare except
            print(f"Ошибка: MCP4725 не найден по адресу 0x{self.address:02X}")
            print("Проверьте подключение и выполните команды:")
            print("raspi-gpio set 2 a0")
            print("raspi-gpio set 3 a0")

    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return

        first_byte = self.wm | ((number >> 8) & 0x0F)
        second_byte = number & 0xFF
        
        try:
            self.bus.write_i2c_block_data(self.address, first_byte, [second_byte])
        except Exception as e:
            print(f"Ошибка записи: {e}")
            return

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{first_byte:02X}, 0x{second_byte:02X}]")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0..{self.dynamic_range} B)")
            voltage = 0.0
        
        number = int(voltage / self.dynamic_range * 4095)
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = MCP4725(dynamic_range=5.0, address=0x61, verbose=True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
            except KeyboardInterrupt:
                print("\nПрограмма завершена пользователем")
                break

    finally:
        dac.deinit()