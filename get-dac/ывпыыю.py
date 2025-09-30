import RPi.GPIO as GPIO
import time

# Настройка пинов DAC
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)

dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        return 0
    
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    # Преобразуем число в список битов (0/1)
    binary = bin(number)[2:].zfill(8)
    bits = [int(bit) for bit in binary]
    print(f"Число: {number}, Бинарный код: {binary}, Биты: {bits}")
    return bits

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах (0-3.3): "))
            number = voltage_to_number(voltage)
            bits = number_to_dac(number)
            
            # Устанавливаем состояние пинов
            for i in range(8):
                GPIO.output(dac_bits[i], bits[i])
                print(f"Пин {dac_bits[i]} установлен в {bits[i]}")
            
            actual_voltage = (number / 255) * dynamic_range
            print(f"Запрошено: {voltage:.2f} В, Установлено: {actual_voltage:.2f} В")
            print("-" * 50)
            
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз \n")
        except KeyboardInterrupt:
            print("\nВыход из программы")
            break

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    print("Очистка...")
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()