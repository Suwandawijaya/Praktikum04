# Praktikum04
# Pertemuan9-praktikum4

Repositiry ini dibuat untuk memenuhi tugas Pertemuan 9 - Bahasa Pemrograman (Module Praktikum 4)<br><br>
Nama : Suwanda wijaya <br>
NIM : 312210028<br>
Dosen : Agung Nugroho, M.Kom<br>
Matkul : Bahasa Pemrograman<br>
Kelas : TI.22.B.1<br>

Pada halaman ini (Tugas Pertemuan-9-Module Praktikum 4) Dosen memberi tugas sebagai berikut : <br>
Ada dua bahan praktik dimodule 4 kali ini yaitu :<br>

* Soal Latihan yang ada pada module praktikum 4
![tugas](img/soallist.png)<br>

* Berikut ini saya menulis syntax sekaligus menuliskan langkah-langkahnya sebagai berikut 

```python
# create list
print("Buat sebuah list sebanyak 5 elemen dengan nilai bebas")
listA = ["buku", 30, 21, "mangga", 34]
print(list)

# mengakses list
print("Menampilkan elemen ke 3")
print(listA[2])

print("ambil nilai elemen 2 sampai ke 4")
print(listA[1:4])

print("ambil elemen terakhir")
print(listA[4])

# mengubah elemen list
print("ubah elemen 4 dengan nilai lainnya")
listA[3]=10
print(listA[3])

print("ubah elemen 4 sampai dengan elemen terakhir")
listA[4:5]=["apel", 11]
print(listA)

# Tambah elemen list
print("Ambil 2 bagian dari list pertama(A) dan jadikan list ke 2(B)")
listB=listA[0:2]
print(listB)

print("tambah list B dengan nilai string")
listB.append("Melon")
print(listB)

print("Tambah list B dengan 3 nilai")
listB.extend(["jeruk", 99, 80])
print(listB)

print("Menggabungkan list B dengan list A")
listGabungan=listB+listA
print(listGabungan)

```
* Berikut hasil run syntax untuk memenuhi latihan module 4 diatas :<br><br>
![hasil running](img/list.png)<br>

* Soal Tugas praktikum module 4
![soal praktik module4](img/soal-praktikum4.png)<br>

* Pada soal tugas ini saya akan menulis dan menjelaskan syntax yang saya buat sebagai berikut<br>

```python

print("===================================================================")
print("Tugas Praktikum module 4")

# Buat program sederhana untuk menambahkan data kedalam sebuah list dengan rincian sebagai berikut: • Progam meminta
# memasukkan data sebanyak-banyaknya (gunakan perulangan) • Tampilkan pertanyaan untuk menambah data (y/t?),
# apabila jawaban t (Tidak), maka program akan menampilkan daftar datanya. • Nilai Akhir diambil dari perhitungan 3
# komponen nilai (tugas: 30%, uts: 35%, uas: 35%) • Buat flowchart dan penjelasan programnya pada README.md. • Commit
# dan push repository ke github.

from prettytable import PrettyTable

baris = []
stop = False

# masukan nilai
while (not stop):
    nama = input("Masukan Nama : ")
    nim = input("Masukan NIM : ")
    tugas = input("Masukan Nilai Tugas : ")
    uts = input("Masukan Nilai UTS : ")
    uas = input("Masukan Nilai UAS : ")
    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
    baris.append([nama, nim, tugas, uts, uas, nilai_akhir])

    tanya = input("Tambah data? (y/t) : ")
    if (tanya == "t"):
        stop = True

# cetak nilai
print("===================================================================")

x = PrettyTable()
no = 0

for isi in baris:
    no += 1
    x.field_names = ["No", "Nama", "Nim", "Tugas", "UTS", "UAS", "Nilai Akhir"]
    x.add_row([no, isi[0], isi[1], isi[2], isi[3], isi[4], isi[5]])
print(x)
```
* Berikut hasil run syntax yang saya buat untuk memenuhi praktikum module 4 :<br><br>
![hasil running](img/praktikum4.png)<br>
* Flowchart program diatas adalah sebagai berikut <br>
![flowchar](img/flowchart-module.png)<br
> Penjelasan singkat tentang fungsi While untuk mengatur kondisi seperti while not stop dan jika tidak berhenti maka system akan terus menampilkan perintah user untuk meninputkan data . Untuk perhitungan nilai akhir sesuai ketentuan yang dosen inginkan. Sedangkan untuk menampilkan hasil dari inputan user tersebut menggunakan fungsi/module yang ada pada PrettyTable bisa mengakses link berikut ini untuk panduan installation : <br>
> [How to install PIP](https://phoenixnap.com/kb/install-pip-windows)<br>
>[How to install PrettyTable](https://pypi.org/project/prettytable/)<br>

### Demikian tugas untuk pertemuan 9 module 4 yang bisa saya sampaikan, Terima kasih...