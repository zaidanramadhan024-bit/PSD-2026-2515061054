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