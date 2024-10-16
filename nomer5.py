n = int(input("angkanya = "))#kode ini untuk menginput value untuk n
for i in range(1 ,n+1):#Fungsi range(1, n+1) menghasilkan urutan angka mulai dari 1 hingga n, sehingga variabel i akan mengambil nilai setiap angka dalam rentang tersebut pada setiap iterasi.

    for k in range(i):#loop ini Untuk setiap nilai i, loop ini berjalan i. jadi dalam satu baris akan menampilkan i sebanyak i dalam satu baris
        print(i, end=" ")#Baris ini mencetak nilai i tanpa pindah baris
    print()#Baris ini digunakan untuk mencetak baris kosong (newline) setelah loop bersarang selesai