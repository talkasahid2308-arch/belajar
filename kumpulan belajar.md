#iterasi lompat 2 angka (deret ganjil)
for i in range(1, 10, 2):
    print(i)
#output:1, 3, 5, 7, 9

#hitung mundur (countdown)
for i in range(10, 0, -1):
    print(i)
#output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

#iterasi langsung declarative
daftar_buah = ["apel", "pisang", "jeruk"]
for item in daftar_buah:
    print(item)

#iterasi pasangan indeks dan nilai
for i, item in enumerate(daftar_buah):
    print(f"indeks {i}: {item}")
# output: indeks 0: apel, dst

#sample dictionary data
mhs = {"nama": "aria", "nim": "12345"}
#iterasi kunci dan nilai bersama
for key, value in mhs.items():
    print(f"{key}: {value}")
