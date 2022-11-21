# membuat list
print("BUAT LIST DENGAN 5 ELEMEN")
listA = ["buku", 30, 21, "mangga", 34]
print(listA)

# mengakses list
print("MENAMPILKAN ELEMEN KE 3")
print(listA[2])

print("AMBIL NILAI ELEMEN KE 2 SAMPAI KE 4")
print(listA[1:4])

print("AMBIL ELEMEN TERKAHIR")
print(listA[4])

# mengubah elemen list
print("UBAH ELEM 4 DENGAN ELEMEN LAINNYA")
listA[3]=10
print(listA[3])

print("UBAH ELEMEN 4 SAMPAI DENGAN ELEMEN TERKAHIR")
listA[4:5]=["apel", 11]
print(listA)

# Tambah elemen list
print("AMBIL 2 BAGIAN ELEMEN DARI LIST A KE LIST B)")
listB=listA[0:2]
print(listB)

print("TAMBAH LIST B DENGAN NILAI STRING")
listB.append("Melon")
print(listB)

print("TAMBAH LIST B DENGAN 3 NILAI")
listB.extend(["jeruk", 99, 80])
print(listB)

print("MENGGABUNGKAN LIST B DAN LIST A")
listGabungan=listB+listA
print(listGabungan)