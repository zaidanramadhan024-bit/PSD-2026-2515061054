def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ["apel", "jeruk", "mangga", "apel", "pisang", "jeruk", "apel"]
    n = len(data)

    print(f"Daftar buah: {data}")

    target = input("Masukkan nama buah yang ingin dicari: ")

    hasil = sequential_search(data, n, target)

    if hasil > 0:
        print(f"Buah {target} ditemukan sebanyak {hasil} kali.")
    else:
        print(f"Buah {target} tidak ditemukan.")


if __name__ == "__main__":
    main()
