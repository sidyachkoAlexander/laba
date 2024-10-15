import numpy as np


x,y,z = float(input('Введите x: ')), float(input('Введите y: ')), float(input('Введите z: '))

s = np.round(((y+(x-1)**(1/3))**(1/4))/(np.abs(x-y)*(np.sin(z)**2 + np.tan(z))), 2)

print(f'При введенных входных данных s = {s}')
