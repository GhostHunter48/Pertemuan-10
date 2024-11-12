# Nama: 
# NIM: 
# Kelas: 1A
import numpy as np

nilai_ujian = np.array([78, 85, 92, 70, 65, 88, 77, 95, 82, 69, 
                        74, 91, 67, 89, 94, 58, 76, 87, 79, 80, 
                        90, 84, 73, 72, 68, 93, 86, 81, 66, 75])

nilai_urut = np.sort(nilai_ujian)[::-1]

print("Nilai ujian dari terbesar hingga terkecil:", nilai_urut)

print("5 nilai terbesar:", nilai_urut[:5])
