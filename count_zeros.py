def count_zeros(number):
    return str(number).count('0')


print('Input number to count zeros')
x = input(int())

y = count_zeros(x)
print(y)