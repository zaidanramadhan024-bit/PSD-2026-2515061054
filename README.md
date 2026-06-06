# Judul Program
Implementasi HashMap dengan Separate Chaining pada Data Mata Kuliah

## Deskripsi Singkat

Program ini dibuat untuk menyimpan dan mencari data mata kuliah menggunakan struktur data HashMap dengan metode Separate Chaining. Setiap mata kuliah memiliki **kode mata kuliah** sebagai key dan nama mata kuliah sebagai value.

Pengguna dapat mencari nama mata kuliah berdasarkan kode yang dimasukkan melalui menu pencarian. Selain itu, pengguna juga dapat melihat seluruh data mata kuliah yang tersimpan di dalam HashMap.

Struktur data yang digunakan adalah HashMap, yaitu struktur data yang memungkinkan proses pencarian data dilakukan dengan cepat menggunakan fungsi hash. Untuk mengatasi collision (tabrakan indeks), digunakan metode Separate Chaining dengan bantuan Linked List.

---

# Source Code dan Penjelasan

### 1. Class Node

```python
class Node:
```

Class Node digunakan untuk membuat node pada Linked List yang akan digunakan dalam metode Separate Chaining.

```python
def __init__(self, key, value):
```

Constructor yang digunakan untuk menginisialisasi data node.

```python
self.key = key
```

Menyimpan kode mata kuliah sebagai key.

```python
self.value = value
```

Menyimpan nama mata kuliah sebagai value.

```python
self.next = None
```

Pointer yang digunakan untuk menghubungkan node dengan node berikutnya.

---

### 2. Class HashMapSeparateChaining

```python
class HashMapSeparateChaining:
```

Class utama yang digunakan untuk membuat HashMap.

```python
def __init__(self, size=10):
```

Constructor untuk menentukan ukuran HashMap.

```python
self.SIZE = size
```

Menyimpan ukuran tabel HashMap.

```python
self.table = [None] * self.SIZE
```

Membuat tabel HashMap yang awalnya masih kosong.

---

### 3. Fungsi Hash

```python
def hash_function(self, key):
```

Fungsi yang digunakan untuk menentukan indeks penyimpanan data.

```python
return (key % self.SIZE + self.SIZE) % self.SIZE
```

Menghasilkan indeks berdasarkan kode mata kuliah yang dimasukkan.

---

### 4. Fungsi Insert

```python
def insert(self, key, value):
```

Digunakan untuk menambahkan data mata kuliah ke HashMap.

```python
index = self.hash_function(key)
```

Menentukan posisi indeks menggunakan fungsi hash.

```python
current = self.table[index]
```

Mengambil data pada indeks tersebut.

```python
while current is not None:
```

Menelusuri Linked List jika terdapat collision.

```python
if current.key == key:
```

Mengecek apakah key yang sama sudah ada.

```python
current.value = value
```

Memperbarui value jika key ditemukan.

```python
new_node = Node(key, value)
```

Membuat node baru.

```python
new_node.next = self.table[index]
```

Menghubungkan node baru dengan node sebelumnya.

```python
self.table[index] = new_node
```

Menyimpan node baru ke HashMap.

---

### 5. Fungsi Search

```python
def search(self, key):
```

Digunakan untuk mencari data berdasarkan kode mata kuliah.

```python
index = self.hash_function(key)
```

Menentukan indeks pencarian.

```python
current = self.table[index]
```

Mengambil node pertama pada indeks tersebut.

```python
while current is not None:
```

Menelusuri seluruh node pada Linked List.

```python
if current.key == key:
```

Mengecek apakah kode mata kuliah ditemukan.

```python
return current
```

Mengembalikan node jika data ditemukan.

```python
return None
```

Mengembalikan nilai kosong jika data tidak ditemukan.

---

### 6. Fungsi Display

```python
def display(self):
```

Digunakan untuk menampilkan seluruh isi HashMap.

```python
print("\nData Mata Kuliah:")
```

Menampilkan judul data.

```python
for i in range(self.SIZE):
```

Perulangan untuk menampilkan seluruh indeks HashMap.

```python
current = self.table[i]
```

Mengambil node pertama pada indeks tersebut.

```python
while current is not None:
```

Menampilkan seluruh node yang berada pada indeks tersebut.

```python
print(f"({current.key}, {current.value}) -> ", end="")
```

Menampilkan key dan value yang tersimpan.

```python
print("NULL")
```

Menandakan akhir Linked List.

---

### 7. Fungsi Main

```python
def main():
```

Fungsi utama program.

```python
hashmap = HashMapSeparateChaining()
```

Membuat objek HashMap.

```python
hashmap.insert(101, "Algoritma dan Pemrograman")
hashmap.insert(111, "Struktur Data")
hashmap.insert(121, "Rekayasa Perangkat Lunak")
hashmap.insert(102, "Teknik Digital")
```

Menambahkan data mata kuliah ke dalam HashMap.

```python
pilih = 0
```

Variabel untuk menyimpan pilihan menu.

```python
while pilih != 3:
```

Perulangan menu yang akan terus berjalan sampai pengguna memilih keluar.

```python
print("\n=== Sistem Data Mata Kuliah ===")
```

Menampilkan menu program.

```python
pilih = int(input("Pilih menu: "))
```

Menerima input pilihan menu dari pengguna.

```python
if pilih == 1:
```

Menjalankan menu pencarian mata kuliah.

```python
key = int(input("Masukkan kode mata kuliah: "))
```

Menerima kode mata kuliah yang ingin dicari.

```python
hasil = hashmap.search(key)
```

Mencari data mata kuliah berdasarkan kode.

```python
if hasil is not None:
```

Mengecek apakah data ditemukan.

```python
print(f"Nama Mata Kuliah : {hasil.value}")
```

Menampilkan nama mata kuliah.

```python
elif pilih == 2:
```

Menjalankan menu untuk menampilkan seluruh data.

```python
hashmap.display()
```

Menampilkan seluruh isi HashMap.

```python
elif pilih == 3:
```

Menu keluar dari program.

```python
print("Program selesai.")
```

Menampilkan pesan program selesai.

---

## Source Code Lengkap

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def display(self):
        print("\nData Mata Kuliah:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()

    hashmap.insert(101, "Algoritma dan Pemrograman")
    hashmap.insert(111, "Struktur Data")
    hashmap.insert(121, "Rekayasa Perangkat Lunak")
    hashmap.insert(102, "Teknik Digital")

    pilih = 0

    while pilih != 3:
        print("\n=== Sistem Data Mata Kuliah ===")
        print("1. Cari Mata Kuliah")
        print("2. Tampilkan Semua Data")
        print("3. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilih == 1:
            try:
                key = int(input("Masukkan kode mata kuliah: "))
                hasil = hashmap.search(key)

                if hasil is not None:
                    print(f"Kode Mata Kuliah {key} ditemukan")
                    print(f"Nama Mata Kuliah : {hasil.value}")
                else:
                    print("Kode Mata Kuliah tidak ditemukan")

            except ValueError:
                print("Kode mata kuliah harus berupa angka!")

        elif pilih == 2:
            hashmap.display()

        elif pilih == 3:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
```

---

# Output Program

<img width="2400" height="1568" alt="Screenshot 2026-06-06 171628" src="https://github.com/user-attachments/assets/6491727d-a387-4ae7-9383-378ae3a8919b" />


---

# Penjelasan Output Program

Saat program dijalankan, beberapa data mata kuliah akan dimasukkan terlebih dahulu ke dalam HashMap. Setiap mata kuliah memiliki kode mata kuliah sebagai key dan nama mata kuliah sebagai value.

Pada menu Cari Mata Kuliah, pengguna diminta memasukkan kode mata kuliah. Program kemudian menggunakan fungsi hash untuk menentukan indeks penyimpanan data dan melakukan pencarian pada indeks tersebut. Jika data ditemukan, program akan menampilkan nama mata kuliah yang sesuai.

Pada menu Tampilkan Semua Data, program akan menampilkan seluruh isi HashMap beserta Linked List yang terbentuk akibat collision. Tampilan ini menunjukkan bagaimana metode Separate Chaining bekerja dalam menyimpan beberapa data pada indeks yang sama.

Program akan terus berjalan sampai pengguna memilih menu **Keluar**, sehingga pengguna dapat melakukan pencarian maupun melihat data berkali-kali tanpa perlu menjalankan ulang program.
