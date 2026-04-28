def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j + 1] > arr[j]:
                tukar(arr, j, j + 1)


def main():
    try:
        banyak_orang = int(input("Masukkan jumlah orang: "))
    except ValueError:
        print("Input tidak valid!")
        return

    umur = []
    print("Masukkan umur setiap orang:")

    for i in range(banyak_orang):
        while True:
            try:
                u = int(input(f"Umur orang ke-{i+1}: "))
                umur.append(u)
                break
            except ValueError:
                print("Harus angka ya!")

    print("Umur sebelum diurutkan:", umur)

    bubble_sort(umur, banyak_orang)

    print("Umur setelah diurutkan:", end=" ")
    for i in range(banyak_orang):
        print(umur[i], end=" ")
    print()


if __name__ == "__main__":
    main()