import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000) # Створюємо масив значень
x[0] = 1e-6  
y = x ** np.cos(x)
plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label=r'$y = x^{\cos(x)}$') # Побудова графіка
plt.title('Графік функції y = x^cos(x)', fontsize=14)

# Позначення осей
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend() # Легенда
plt.grid(True) # Відображення сітки
plt.show() #Відображення графіка