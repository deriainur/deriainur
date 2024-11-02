print("Nama : Deri Ainur Ridho")
print("NIM  : 352310702")

max = 0 # Menentukan bilangan terbesar
while True :
        a = int(input("Masukkan bilangan = "))
        if max < a:
            max = a
        if a== 0:
            break # Mengakhiri perulangan

print ("Bilangan terbesar adalah: ",max)
