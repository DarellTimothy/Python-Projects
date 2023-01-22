# PROGRAM MENENTUKAN LUAS DIBAWAH KURVA DENGAN INTEGRAL PERSEGI

a = int(input("Masukkan batas awal integral: "))
b = int(input("Masukkan batas akhir integral: "))
n = int(input("Masukkan jumlah pembatas/partisi: "))

dx = (b-a)/n
L = 0
#referensi dari rumus luas integral D.sqrtD/6a^2
batas_awal = a
for i in range (batas_awal, n):
    p = a*a+2
    L = L + p*dx
    a = a + dx
print ("Luas dibawah kurva adalah" , L)