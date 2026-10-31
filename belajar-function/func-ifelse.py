def cek_kelulusan(nilai):
    if nilai >=70:
        return "lulus"
    else:
        return "tidak lulus"

print(cek_kelulusan(75))
print(cek_kelulusan(65))