def hitung_total(angka):
    total = 0

    for num in angka:
        total += num

    return total

data = [10, 20, 30, 40, 50]
hasil = hitung_total(data)
print(f"total dari {data} adalah: {hasil}")