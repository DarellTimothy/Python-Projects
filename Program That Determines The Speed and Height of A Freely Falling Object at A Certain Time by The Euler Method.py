#Deskripsi : Menentukan kecepatan dan ketinggian benda jatuh bebas pada waktu tertentu dengan metode Euler

#KAMUs
#v0 = float
#h0 = float
#g = float
#dt = float

#Masukkan nilai variabel variabel yang digunakan dalam perhitungan gerak jatuh bebas
v0 = float(input("masukkan kecepatan benda mula-mula : "))
h0 = float(input("masukkan ketinggian benda mula-mula : "))
dt = float(input("masukkan selang waktu : "))
t = 0
g = float(input("masukkan besar percepatan gravitasi : "))

#lakukan pengkondisian dimana ketika keteinggian awal (h0) lebih besar dari 0

while h0 > 0.0 :
    v0 += g*dt
    h0 -= v0*dt
    t = t + dt
    print("kecepatan benda pada saat ", t, " detik adalah ", v0) 
    print("ketinggian benda pada saat ", t, " detik adalah ", h0)