#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input('Введите число: '))
def m(n):
    if n == 1:
        return 1
    else:
       return (1+1/i)**i
list = []
for i in range(1, n+1):
    list.append(m(i))
print(f'Последовательность: {list}\nСумма: {round(sum(list))}')


