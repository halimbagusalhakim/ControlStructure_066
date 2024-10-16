n = int(input("Masukkan jumlah elemen Fibonacci: "))  # Input jumlah elemen
a, b = 0, 1  # Inisialisasi dua elemen pertama Fibonacci

print("Deret Fibonacci:")
for i in range(n):#Melakukan iterasi sebanyak n kali. Setiap iterasi menghasilkan satu elemen Fibonacci baru
    print(a, end=" ")  # Cetak elemen Fibonacci
    a, b = b, a + b  # Update nilai a dan b untuk iterasi berikutnya
