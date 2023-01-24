# Menentukan transpose matriks

#Masukkan besar variabel pada kolom dan baris
baris = int(input("Masukkan jumlah baris matriks : "))
kolom = int(input("Masukkan jumlah kolom matriks : "))

#lakukan perulangan bertingkat dengan tujuan membentuk matriks awal

M = [[0 for j in range (kolom)] for i in range (baris)]
for i in range (baris):
    for j in range (kolom):
        M [i][j] = int(input("Masukkan besar bilangan : "))

#mempersiapkan data data matriks sebelum di transpose dengan perulangan bertingkat

print ("Matriks yang akan di transpose : ")
for i in range (baris):
    for j in range (kolom):
        print (str(M[i][j])+"", end='')
    print ( )

#Proses mengubah ke transpose matriks dengan perulangan bertingkat

print ("Transpose Matriks: ")
for i in range (kolom):
    for j in range (baris):
        print (str(M[j][i])+" ", end='')
    print ( )