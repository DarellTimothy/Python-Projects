# Program dapat melakukan iterasi untuk menentukan jumlah bilangan-bilangan yang diinput merupakan ganjil atau genap , untuk membatalkannya cukup mengingkari syarat dengan menginput (-)

b = int(input("Masukkan :"))
genap, ganjil = 0, 0
while b >= 0:
    if b%2 == 0:
        genap += 1
    else :
        ganjil += 1
    b = int(input("Masukkan Bilangan : "))
print("Genap = ", genap )
print("Ganjil = ", ganjil )