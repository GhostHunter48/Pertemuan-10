# Nama: 
# NIM: 
# Kelas: 1A
import numpy as np

suhu_celcius = np.array([30, 31, 29, 32, 30, 33, 31, 28, 30, 29]) 

suhu_fahrenheit = (suhu_celcius * 9/5) + 32

print("Suhu dalam Celcius selama 10 hari terakhir:")
print(suhu_celcius)
print("\nSuhu dalam Fahrenheit:")
print(suhu_fahrenheit)