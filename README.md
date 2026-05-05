# Judul Program
Implementasi Algoritma Sequential Search pada Pencarian Data Buah

## Deskripsi Singkat
Program ini dibuat untuk mencari jumlah kemunculan suatu buah dalam sebuah daftar menggunakan algoritma **Sequential Search**. Pengguna diminta memasukkan nama buah yang ingin dicari, kemudian program akan menghitung berapa kali buah tersebut muncul di dalam data.

Dengan adanya program ini, pengguna dapat mengetahui jumlah kemunculan suatu data secara sederhana. Metode yang digunakan adalah **Sequential Search**, yaitu metode pencarian yang dilakukan dengan cara memeriksa data satu per satu dari awal hingga akhir.

Struktur data yang digunakan adalah **List (Array 1 Dimensi)** karena data buah disimpan dalam satu kumpulan data yang sama.

---

## Source Code dan Penjelasan

### 1. Fungsi Sequential Search

```python
def sequential_search(data, n, target):
```

Fungsi ini digunakan untuk mencari dan menghitung jumlah kemunculan data yang dicari.

```python
i = 0
counter = 0
```

Variabel i sebagai indeks untuk menelusuri data, sedangkan counter untuk menghitung jumlah kemunculan.

```python
while i < n:
```

Perulangan untuk memeriksa seluruh elemen dalam list.

```python
if data[i] == target:
```

Mengecek apakah data saat ini sama dengan data yang dicari.

```python
counter += 1
```

Jika sama, maka jumlah kemunculan ditambah.

```python
i += 1
```

Melanjutkan ke data berikutnya.

```python
return counter
```

Mengembalikan hasil jumlah kemunculan.

### 2. Fungsi Main

```python
def main():
```

Fungsi utama program.

```python
data = ["apel", "durian", "mangga", "apel", "mangga", "jeruk", "apel", "anggur", "jambu"]
```

List data buah yang sudah diperbaiki (setiap buah menjadi elemen terpisah).

```python
n = len(data)
```

Menghitung jumlah data.

```python
print("Daftar buah:", data)
```

Menampilkan data buah.

```python
target = input("Masukkan nama buah yang ingin dicari: ")
```

Input nama buah dari pengguna.

```python
hasil = sequential_search(data, n, target)
```

Memanggil fungsi pencarian.

```python
if hasil > 0:
```

Mengecek apakah buah ditemukan.

```python
print(f"Buah {target} ditemukan sebanyak {hasil} kali.")
```

Menampilkan hasil jika ditemukan.

```python
else:
    print(f"Buah {target} tidak ditemukan.")
```

Menampilkan pesan jika tidak ditemukan.

### 3. Menjalankan Program

```python
if __name__ == "__main__":
    main()
```

Digunakan untuk menjalankan program utama.
