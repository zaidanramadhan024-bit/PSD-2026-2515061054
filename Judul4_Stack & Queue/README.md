### Judul Program

Implementasi Struktur Data Stack Array pada Riwayat Login User

### Deskripsi Singkat

Program ini dibuat untuk mengelola data riwayat login user menggunakan konsep Stack Array. Pengguna dapat menambahkan user yang login, menghapus user terakhir yang login (logout), melihat user terakhir yang login, dan menampilkan seluruh riwayat login yang tersimpan.

Konsep yang digunakan pada program ini adalah Stack (LIFO / Last In First Out), yaitu data yang terakhir masuk akan menjadi data pertama yang keluar. Konsep ini sesuai digunakan pada sistem login karena user terakhir yang login dapat logout terlebih dahulu.

Struktur data yang digunakan adalah Array 1 Dimensi, karena seluruh data username disimpan dalam satu list dengan kapasitas tertentu.

### Source Code dan Penjelasan


### 1. Class StackArray
```python
class StackArray:
```
Class digunakan untuk membuat struktur stack pada program.
```python
def __init__(self, max_size=100):
```
Constructor digunakan untuk mengatur data awal stack.
```python
self.MAX = max_size
```
Menentukan kapasitas maksimum stack.
```python
self.st = [None] * self.MAX
```
Membuat list kosong untuk menyimpan data user login.
```python
self.top_idx = -1
```
Menandakan bahwa stack masih kosong.

### 2. Fungsi is_empty()
```python
def is_empty(self):
```
Fungsi digunakan untuk mengecek apakah stack kosong.
```python
return self.top_idx == -1
```
Jika nilai top_idx sama dengan -1, berarti belum ada data pada stack.

### 3. Fungsi is_full()
```python
def is_full(self):
```
Fungsi digunakan untuk mengecek apakah stack sudah penuh.
```python
return self.top_idx == self.MAX - 1
```
Jika posisi indeks terakhir sama dengan kapasitas maksimum dikurangi satu, maka stack penuh.

### 4. Fungsi push()
```python
def push(self, x):
```
Fungsi digunakan untuk menambahkan user login ke dalam stack.
```python
if self.is_full():
```
Mengecek apakah stack penuh.
```python
print("Riwayat login penuh")
```
Menampilkan pesan jika stack tidak dapat ditambah lagi.
```python
self.top_idx += 1
```
Menambah posisi indeks teratas.
```python
self.st[self.top_idx] = x
```
Menyimpan username ke dalam stack.
```python
print(f"User {x} berhasil login")
```
Menampilkan pesan bahwa user berhasil login.

### 5. Fungsi pop()
```python
def pop(self):
```
Fungsi digunakan untuk menghapus user terakhir dari stack.
```python
if self.is_empty():
```
Mengecek apakah stack kosong.
```python
print("Tidak ada riwayat login")
```
Menampilkan pesan jika stack kosong.
```python
print(f"User {self.st[self.top_idx]} berhasil logout")
```
Menampilkan user yang logout.
```python
self.top_idx -= 1
```
Mengurangi posisi indeks teratas sehingga data dianggap terhapus.

### 6. Fungsi peek()
```python
def peek(self):
```
Fungsi digunakan untuk melihat user terakhir yang login.
```python
if self.is_empty():
```
Mengecek apakah stack kosong.
```python
print(f"User terakhir yang login: {self.st[self.top_idx]}")
```
Menampilkan user yang berada di posisi paling atas stack.

### 7. Fungsi display()
```python
def display(self):
```
Fungsi digunakan untuk menampilkan seluruh riwayat login user.
```python
for i in range(self.top_idx, -1, -1):
```
Perulangan digunakan untuk menampilkan data dari atas ke bawah.
```python
print(self.st[i], end=" ")
```
Menampilkan seluruh data user login.

### 8. Fungsi Main
```python
def main():
```
Fungsi utama program.
```python
login = StackArray()
```
Membuat objek stack baru.
```python
pilih = 0
```
Variabel untuk menyimpan pilihan menu.
```python
while pilih != 5:
```
Perulangan program selama pengguna belum memilih keluar.
```python
pilih = int(input("Pilih: "))
```
Input pilihan menu dari pengguna.
```python
username = input("Masukkan username: ")
```
Input username yang ingin login.
```python
login.push(username)
```
Menambahkan user login ke stack.
```python
login.pop()
```
Menghapus user terakhir dari stack.
```python
login.peek()
```
Melihat user terakhir yang login.
```python
login.display()
```
Menampilkan seluruh riwayat login.

### Source Code Lengkap
```python
class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Riwayat login penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"User {x} berhasil login")

    def pop(self):
        if self.is_empty():
            print("Tidak ada riwayat login")
            return
        print(f"User {self.st[self.top_idx]} berhasil logout")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Tidak ada user yang login")
            return
        print(f"User terakhir yang login: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Riwayat login kosong")
            return
        print("Riwayat Login User (terbaru ke terlama): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()


def main():
    login = StackArray()
    pilih = 0

    while pilih != 5:
        print("\n=== Riwayat Login User ===")
        print("1. Login User")
        print("2. Logout User")
        print("3. User Terakhir Login")
        print("4. Lihat Semua Riwayat Login")
        print("5. Keluar Program")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            username = input("Masukkan username: ")
            login.push(username)

        elif pilih == 2:
            login.pop()

        elif pilih == 3:
            login.peek()

        elif pilih == 4:
            login.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
```
### Output Program

<img width="2130" height="1394" alt="Screenshot 2026-05-11 214940" src="https://github.com/user-attachments/assets/8d3fdb04-44f7-4e33-b060-b5d5f5caeec6" />

<img width="2134" height="668" alt="Screenshot 2026-05-11 215003" src="https://github.com/user-attachments/assets/7e905310-df8a-492e-9570-998a41f33e57" />



Saat program dijalankan, pengguna akan melihat menu utama yang berisi beberapa pilihan. Pengguna dapat menambahkan user login, logout user terakhir, melihat user terakhir yang login, dan menampilkan seluruh riwayat login.

Ketika user login, data username akan dimasukkan ke dalam stack menggunakan metode push(). Jika user logout, maka user terakhir yang login akan keluar terlebih dahulu menggunakan metode pop(). Hal ini menunjukkan bahwa struktur data stack bekerja dengan konsep LIFO (Last In First Out), yaitu data terakhir masuk akan menjadi data pertama yang keluar.
