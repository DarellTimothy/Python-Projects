a = int(input("Masukkan besar batas awal integral: "))
b = int(input("Masukkan besar batas akhir integral: "))
n = int(input("Masukkan jumlah pembatas/partisi: "))

dx = (b-a)/n
L_up = a*a + 2 
L_down = b*b + 2
L = 0
batas_awal = a

for i in range (batas_awal , n-1):
    y = (a+dx)**2+2
    L = L + y*dx
    a = a + dx

L_t = ((dx*(L_up + L_down))/2) + L
print ("Luas dibawah kurva adalah" , L_t)