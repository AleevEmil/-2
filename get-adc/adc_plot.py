from matplotlib import pyplot

def plot_voltage_vs_time(time, voltage, max_voltage):
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(time, voltage, 'b-', linewidth=2, label='Измеренное напряжение')
    
    pyplot.title('Зависимость напряжения от времени', fontsize=14, fontweight='bold')
    pyplot.xlabel('Время, с', fontsize=12)
    pyplot.ylabel('Напряжение, В', fontsize=12)
    
    pyplot.xlim(0, max(time))
    pyplot.ylim(0, max_voltage * 1.1)  
    
    pyplot.grid(True, alpha=0.3)
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.show()