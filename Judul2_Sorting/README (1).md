# Judul Program
Implementasi Algoritma Bubble Sort pada Pengurutan Umur Orang

## Deskripsi Singkat
Program ini dibuat untuk mengurutkan data umur seseorang dengan menggunakan algoritma **Bubble Sort**. Pengguna diminta memasukkan jumlah orang beserta umur masing-masing, kemudian program akan menampilkan data sebelum dan sesudah diurutkan.

Melalui program ini, data umur dapat diurutkan dari umur paling tua hingga paling muda sehingga pengguna lebih mudah melihat urutan data yang ada.

Metode yang digunakan adalah **Bubble Sort**, yaitu metode pengurutan yang dilakukan dengan membandingkan dua data yang posisinya berdekatan. Jika urutannya belum sesuai, maka kedua data tersebut akan ditukar posisinya. Proses perbandingan dilakukan berulang kali sampai seluruh data berada pada urutan yang benar.

Struktur data yang dipakai dalam program ini adalah **List (Array 1 Dimensi)** karena seluruh data umur disimpan dalam satu kumpulan data yang sama dan diproses secara berurutan.

## Source Code dan Penjelasan
<img width="2187" height="1304" alt="Screenshot 2026-04-28 125550" src="https://github.com/user-attachments/assets/cb4d773b-7306-4921-86dd-52f07400a1ef" />
<img width="2154" height="435" alt="Screenshot 2026-04-28 125617" src="https://github.com/user-attachments/assets/995e6319-7c10-4ad8-8b0a-b39dc640c17c" />

### 1. Fungsi Tukar

```python
def tukar(arr, i, j):
```

Fungsi ini digunakan untuk menukar posisi dua data pada list berdasarkan indeks yang dipilih.

```python
temp = arr[i]
```

Nilai pada indeks i disimpan terlebih dahulu ke variabel sementara.

```python
arr[i] = arr[j]
```

Nilai pada indeks j dipindahkan ke posisi indeks i.

```python
arr[j] = temp
```

Nilai sementara tadi dimasukkan ke indeks j sehingga proses pertukaran selesai dilakukan.

---

### 2. Fungsi Bubble Sort

```python
def bubble_sort(arr, n):
```

Fungsi ini berisi proses pengurutan data menggunakan metode Bubble Sort.

```python
for i in range(n - 1):
```

Perulangan pertama digunakan untuk menentukan banyaknya tahap pengurutan.

```python
for j in range(n - i - 1):
```

Perulangan kedua digunakan untuk mengecek dan membandingkan data yang letaknya bersebelahan.

```python
if arr[j + 1] > arr[j]:
```

Kondisi ini digunakan untuk mengecek apakah data sebelah kanan lebih besar dibanding data sebelah kiri.

```python
tukar(arr, j, j + 1)
```

Jika kondisi terpenuhi, maka kedua data akan ditukar posisinya.

---

### 3. Fungsi Main

```python
def main():
```

Bagian ini merupakan fungsi utama yang menjalankan seluruh program.

```python
banyak_orang = int(input("Masukkan jumlah orang: "))
```

Digunakan untuk menerima input jumlah data yang akan dimasukkan.

```python
umur = []
```

Membuat list kosong yang nantinya digunakan untuk menyimpan data umur.

```python
for i in range(banyak_orang):
```

Perulangan digunakan agar pengguna dapat memasukkan data sesuai jumlah yang ditentukan.

```python
u = int(input(f"Umur orang ke-{i+1}: "))
```
Pengguna memasukkan umur setiap orang satu per satu.

```python
umur.append(u)
```

Data umur yang sudah dimasukkan akan ditambahkan ke dalam list.

---

### 4. Menampilkan Data Awal

```python
print("Umur sebelum diurutkan:", umur)
```

Program menampilkan seluruh data umur sebelum proses sorting dilakukan.

---

### 5. Menjalankan Bubble Sort

```python
bubble_sort(umur, banyak_orang)
```

Baris ini digunakan untuk memanggil fungsi Bubble Sort agar data dapat diurutkan.

---

### 6. Menampilkan Hasil

```python
for i in range(banyak_orang):
```

Perulangan dipakai untuk menampilkan data hasil pengurutan.

```python
print(umur[i], end=" ")
```

Menampilkan setiap data umur yang sudah tersusun sesuai urutan.

---

### 7. Menjalankan Program

```python
if __name__ == "__main__":
```

Digunakan untuk memastikan bahwa file dijalankan sebagai program utama.

```python
main()
```

Menjalankan fungsi main() agar program dapat diproses.

### Output Program

### Screenshot Output
<img width="2172" height="532" alt="Screenshot 2026-04-28 131412" src="https://github.com/user-attachments/assets/b91d2a73-aaf2-4570-8be1-1ef6ae0d67d8" />


### Penjelasan Output Program

Saat program mulai dijalankan, pengguna terlebih dahulu diminta memasukkan jumlah orang yang akan diinput ke dalam program. Setelah itu, pengguna memasukkan data umur satu per satu sesuai jumlah yang telah ditentukan.

Program kemudian menampilkan data umur sebelum dilakukan proses pengurutan. Setelah itu, algoritma Bubble Sort dijalankan untuk mengurutkan data umur secara descending, yaitu dari umur terbesar menuju umur terkecil.

Sesudah proses sorting selesai, program menampilkan hasil akhir berupa daftar umur yang sudah tersusun rapi dari yang paling tua hingga yang paling muda. Hasil tersebut menunjukkan bahwa proses pengurutan menggunakan algoritma Bubble Sort berhasil dijalankan dengan baik.
