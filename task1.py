# Найдите сумму цифр трехзначного числа.

num = int(input())
num_sum = 0
while num > 0:
    num_sum += (num % 10)
    num //= 10
print(num_sum)