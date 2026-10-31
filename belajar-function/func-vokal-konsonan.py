def hitung_vokal_konsonan(kata):
    vokal = 0
    konsonan = 0

    for huruf in kata.lower():
        if huruf in "aiueo":
            vokal += 1
        elif huruf in "bcdfghijklmnopqrstuvwxyz":
            konsonan += 1

    return vokal, konsonan


hilang = input("masukkan sebuah kata atau kalimat: ")
jumlah_vokal, jumlah_konsonan = hitung_vokal_konsonan(hilang)
print(f"jumlah huruf vokal: {jumlah_vokal}")
print(f"jumlah huruf kosonan: {jumlah_konsonan}")