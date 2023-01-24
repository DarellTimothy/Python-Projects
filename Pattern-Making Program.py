
rows = int(input("Masukkan angka"))

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print("\n")