n = int(input("Masukkan tinggi setengah menara (2-15): "))

while n < 2 or n > 15:
    print("Tinggi tidak valid! Masukkan angka 2 sampai 15.")
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

# Bagian atas menara
for i in range(1, n + 1):
    for spasi in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

# Bagian bawah menara
for i in range(n - 1, 0, -1):
    for spasi in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()