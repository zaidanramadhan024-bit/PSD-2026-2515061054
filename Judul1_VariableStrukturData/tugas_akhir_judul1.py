def menu():
    print("1. Tampilkan semua transaksi")
    print("2. Tambah pemasukan")
    print("3. Tambah pengeluaran")
    print("4. Hitung total & saldo")
    print("5. Keluar")


def main():
    pemasukan = [0] * 5
    pengeluaran = [0] * 5

    jumlah_masuk = 0
    jumlah_keluar = 0

    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("DATA TRANSAKSI")

            print("Pemasukan:")
            if jumlah_masuk == 0:
                print("Belum ada data.")
            else:
                for i in range(jumlah_masuk):
                    print(f"{i+1}. Rp{pemasukan[i]}")
                

            print("Pengeluaran:")
            if jumlah_keluar == 0:
                print("Belum ada data.")
            else:
                for i in range(jumlah_keluar):
                    print(f"{i+1}. Rp{pengeluaran[i]}")

        elif choice == 2:
            if jumlah_masuk < 5:
                try:
                    uang = int(input("Masukkan pemasukan: "))
                    pemasukan[jumlah_masuk] = uang
                    jumlah_masuk += 1
                    print("Pemasukan berhasil ditambahkan!")
                except ValueError:
                    print("Masukkan angka!")
            else:
                print("Data pemasukan penuh!")

        elif choice == 3:
            if jumlah_keluar < 5:
                try:
                    uang = int(input("Masukkan pengeluaran: "))
                    pengeluaran[jumlah_keluar] = uang
                    jumlah_keluar += 1
                    print("Pengeluaran berhasil ditambahkan!")
                except ValueError:
                    print("Masukkan angka!")
            else:
                print("Data pengeluaran penuh!")

        elif choice == 4:
            total_masuk = 0
            total_keluar = 0

            for i in range(jumlah_masuk):
                total_masuk += pemasukan[i]

            for i in range(jumlah_keluar):
                total_keluar += pengeluaran[i]

            saldo = total_masuk - total_keluar

            print(f"Total pemasukan : Rp{total_masuk}")
            print(f"Total pengeluaran: Rp{total_keluar}")
            print(f"Saldo sekarang  : Rp{saldo}")

        elif choice == 5:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()