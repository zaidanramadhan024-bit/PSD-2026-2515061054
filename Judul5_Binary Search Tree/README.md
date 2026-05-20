### Judul Program

Implementasi Binary Search Tree (BST) pada Data Umur Penduduk

### Deskripsi Singkat

Program ini dibuat untuk mengelola data umur penduduk menggunakan struktur data Binary Search Tree (BST). Pengguna dapat menambahkan data umur, mencari umur terdekat yang lebih besar (successor), mencari umur terdekat yang lebih kecil (predecessor), serta menghapus data umur tertentu.

Konsep yang digunakan pada program ini adalah Binary Search Tree, yaitu struktur data pohon biner yang memiliki aturan bahwa nilai di sebelah kiri lebih kecil dari root dan nilai di sebelah kanan lebih besar dari root. Dengan metode ini, proses pencarian dan pengelolaan data menjadi lebih cepat dan terstruktur.

Struktur data BST sangat cocok digunakan untuk pengolahan data umur penduduk karena data dapat tersusun otomatis berdasarkan urutan umur.

### Source Code dan Penjelasan
### 1. Class Node
```python
class Node:
```
Class digunakan untuk membuat node pada BST.
```python
def __init__(self, key):
```
Constructor digunakan untuk mengisi data node.
```python
self.key = key
```
Menyimpan nilai umur pada node.
```python
self.left = None
self.right = None
```
Digunakan untuk menyimpan child kiri dan child kanan.

### 2. Class BSTLanjut
```python
class BSTLanjut:
```
Class digunakan untuk membuat Binary Search Tree.
```python
self.root = None
```
Root awal BST masih kosong.

### 3. Fungsi insert_node()
```python
def insert_node(self, root, key):
```
Fungsi digunakan untuk menambahkan node baru ke BST.
```python
if root is None:
```
Mengecek apakah posisi node kosong.
```python
return Node(key)
```
Membuat node baru jika posisi kosong.
```python
if key < root.key:
```
Jika umur lebih kecil dari root maka data masuk ke subtree kiri.
```python
root.left = self.insert_node(root.left, key)
```
Memasukkan data ke subtree kiri secara rekursif.
```python
elif key > root.key:
```
Jika umur lebih besar dari root maka data masuk ke subtree kanan.
```python
root.right = self.insert_node(root.right, key)
```
Memasukkan data ke subtree kanan secara rekursif.

### 4. Fungsi insert()
```python
def insert(self, key):
```
Digunakan untuk memanggil fungsi insert_node().
```python
self.root = self.insert_node(self.root, key)
```
Menambahkan data umur baru ke BST.

### 5. Fungsi find_min_node()
```python
def find_min_node(self, root):
```
Fungsi digunakan untuk mencari nilai umur terkecil pada subtree.
```python
while current is not None and current.left is not None:
```
Perulangan dilakukan sampai node paling kiri ditemukan.
```python
current = current.left
```
Berpindah ke child kiri.

### 6. Fungsi delete_node()
```python
def delete_node(self, root, key):
```
Fungsi digunakan untuk menghapus node dari BST.
```python
if root is None:
```
Mengecek apakah node kosong.
```python
if key < root.key:
```
Jika umur lebih kecil maka pencarian dilakukan ke subtree kiri.
```python
elif key > root.key:
```
Jika umur lebih besar maka pencarian dilakukan ke subtree kanan.
```python
if root.left is None and root.right is None:
```
Jika node tidak memiliki child maka node langsung dihapus.
```python
successor = self.find_min_node(root.right)
```
Mencari successor untuk mengganti node yang dihapus.

### 7. Fungsi level_order()
```python
def level_order(self, root):
```
Fungsi digunakan untuk menampilkan BST secara level order.
```python
queue = []
```
Membuat queue sementara.
```python
queue.append(root)
```
Menambahkan root ke queue.
```python
current = queue.pop(0)
```
Mengambil data paling depan dari queue.
```python
print(current.key, end=" ")
```
Menampilkan nilai node.

### 8. Fungsi find_successor()
```python
def find_successor(self, root, key):
```
Fungsi digunakan untuk mencari umur terdekat yang lebih besar.
```python
successor = current
```
Menyimpan kandidat successor.

### 9. Fungsi find_predecessor()
```python
def find_predecessor(self, root, key):
```
Fungsi digunakan untuk mencari umur terdekat yang lebih kecil.
```python
predecessor = current
```
Menyimpan kandidat predecessor.

### 10. Fungsi Main
```python
def main():
```
Fungsi utama program.
```python
bst = BSTLanjut()
```
Membuat objek BST.
```python
while pilih != 5:
```
Perulangan program sampai pengguna memilih keluar.
```python
bst.insert(x)
```
Menambahkan umur penduduk ke BST.
```python
bst.find_successor(bst.root, x)
```
Mencari umur terdekat yang lebih besar.
```python
bst.find_predecessor(bst.root, x)
```
Mencari umur terdekat yang lebih kecil.
```python
bst.delete(x)
```
Menghapus data umur penduduk.

### Source Code Lengkap
```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTLanjut:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert_node(root.left, key)

        elif key > root.key:
            root.right = self.insert_node(root.right, key)

        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def find_min_node(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    def delete_node(self, root, key):
        if root is None:
            return None

        if key < root.key:
            root.left = self.delete_node(root.left, key)

        elif key > root.key:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.right = self.delete_node(root.right, successor.key)

        return root

    def level_order(self, root):
        if root is None:
            print("(kosong)")
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            current = queue.pop(0)

            print(current.key, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def find_successor(self, root, key):
        current = root
        successor = None

        while current is not None:
            if key < current.key:
                successor = current
                current = current.left

            elif key > current.key:
                current = current.right

            else:
                break

        if current is None:
            return None, False

        if current.right is not None:
            successor = self.find_min_node(current.right)

        if successor is None:
            return None, False

        return successor.key, True

    def find_predecessor(self, root, key):
        current = root
        predecessor = None

        while current is not None:
            if key > current.key:
                predecessor = current
                current = current.right

            elif key < current.key:
                current = current.left

            else:
                break

        if current is None:
            return None, False

        if current.left is not None:
            temp = current.left

            while temp.right is not None:
                temp = temp.right

            predecessor = temp

        if predecessor is None:
            return None, False

        return predecessor.key, True


def main():
    bst = BSTLanjut()
    pilih = 0

    while pilih != 5:
        print("\n=== Data Umur Penduduk ===")
        print("1. Masukkan Umur Penduduk")
        print("2. Menampilkan umur terdekat yang lebih besar")
        print("3. Menampilkan umur terdekat yang lebih kecil")
        print("4. Hapus Data Umur")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                x = int(input("Masukkan umur penduduk: "))
                bst.insert(x)

                print(f"Umur {x} berhasil dimasukkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                x = int(input("Cari umur terdekat yang lebih besar dari: "))

                ans, found = bst.find_successor(bst.root, x)

                if found:
                    print(f"Umur terdekat yang lebih besar dari {x}: {ans}")

                else:
                    print(f"Tidak ada umur yang lebih besar dari {x}")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            try:
                x = int(input("Cari umur terdekat yang lebih kecil dari: "))

                ans, found = bst.find_predecessor(bst.root, x)

                if found:
                    print(f"Umur terdekat yang lebih kecil dari {x}: {ans}")

                else:
                    print(f"Tidak ada umur yang lebih kecil dari {x}")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 4:
            try:
                x = int(input("Masukkan umur yang ingin dihapus: "))

                bst.delete(x)

                print(f"Umur {x} berhasil dihapus")

                print("Data umur terbaru: ", end="")
                bst.level_order(bst.root)
                print()

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
```
### Output Program

<img width="2880" height="1342" alt="Screenshot 2026-05-20 200514" src="https://github.com/user-attachments/assets/cbaff3ae-db79-4ec9-978b-0520801780d1" />
<img width="2880" height="1552" alt="Screenshot 2026-05-20 200525" src="https://github.com/user-attachments/assets/8012f8bc-5bfe-46a2-b1ee-0e4634e393a0" />
<img width="2880" height="404" alt="Screenshot 2026-05-20 200533" src="https://github.com/user-attachments/assets/f406fa97-ad94-464a-9c9d-1406a7a5480b" />


### Penjelasan Output Program

Saat program dijalankan, pengguna akan melihat menu pengolahan data umur penduduk yang berisi beberapa pilihan seperti menambahkan umur, mencari umur terdekat yang lebih besar atau lebih kecil, menghapus data umur, dan keluar dari program.

Ketika pengguna menambahkan data, umur penduduk akan disimpan ke dalam Binary Search Tree sesuai aturan BST. Jika pengguna mencari successor, program akan menampilkan umur terdekat yang lebih besar dari nilai yang dicari. Sedangkan predecessor digunakan untuk mencari umur terdekat yang lebih kecil.

Program ini menunjukkan bahwa struktur data Binary Search Tree dapat digunakan untuk mengelola data umur penduduk secara terurut sehingga proses pencarian dan penghapusan data menjadi lebih efisien.

Link Youtube : https://youtu.be/qsqep7LMino
