# 2 menentukan bilangan tebesar dari 3 bilangan
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >=a and b >= c:
        return b
    else:
        return c


max_number = max_of_three(3, 4, 10)
print("bilangan terbesar adalah:", max_number)


# rekrusif
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)


print("faktorial dari 5 adalah:", factorial(5))