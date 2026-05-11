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