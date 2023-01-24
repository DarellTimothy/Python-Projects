# Mengubah matriks menjadi triangular keatas dengan Eliminasi Gauss

#KAMUS
#c = int
#c1 = int
#c2 = int
#a = list

import numpy as np

a = [[0 for j in range(3)] for i in range(3)]

#melakukan perulangan bertingkat untuk keadaan dimana i in range 3 : for j in range 3

for i in range(3):

    for j in range(3):
        a[i][j] = int(input(f"Masukkan bilangan baris ke {i+1} dan kolom ke {j+1} : "))

#asumsikan suatu konstanta (c)

c = a[1][0]/a[0][0]

#melakukan perulangan tiap kejadian dengan m saat kejadian tertentu

for m in range(3):
    a[1][m] = c*a[0][m] - a[1][m]

c1 = a[2][0]/a[0][0]

for m in range(3):

    a[2][m] = c1*a[0][m] - a[2][m]

c2 = a[2][1]/a[1][1]