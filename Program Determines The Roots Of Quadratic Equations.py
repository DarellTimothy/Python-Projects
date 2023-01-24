#Menentukan akar akar persamaan kuadrat
#Darell Timothy Tarigan - 16022344 FMIPA-IPA
#Solusi dari persamaan kuadratik dalam bentuk akar akarnya (x1 dan x2 bilangan Real dan Imajiner)
import math

a = float(input("masukkan besar/nilai dari a bukan 0"))
b = float(input("masukkan besar/nilai dari b"))
c = float(input("masukkan besar/nilai dari c"))

det = b * b - 4 * a * c

if (det<0) :
    dar = math.sqrt(-det) / (2*a)
    rel = -b / (2*a)

    print("akar imajiner x1= ", rel, " + i", dar)
    print("akar imajiner x2= ", rel, " - i", dar)
else :
    x1 = (b + math.sqrt(det))/(2*a)
    x2 = (b - math.sqrt(det))/(2*a)
    print("x1 =", x1)
    print("x2 =", x2)
