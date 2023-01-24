num = int(input("Masukkan nilai :"))

if num > 1:
    
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number Sir")
            break
        else:
            print(num,"is a prime number Sir")

else:
    print("Please enter number larger than 1")     