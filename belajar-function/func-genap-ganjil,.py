# 3 menghitung bilangan genap dan ganjil dalam sebuah list
def count_even_odd(number):
    even_count = 0
    odd_count = 0

    for num in number:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

count_even, count_odd = count_even_odd([1, 2, 3, 4, 5, 6, 7, 10, 12])
print("jumlah bilangan genap:", count_even)
print("jumlah bilangan ganjil:", count_odd)