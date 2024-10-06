def get_pass(num):
    password = []
    for i in range(1, num):
        for j in range(2, num):
            if j <= i:
                continue
            if num % (i + j) == 0:
                password.append(f'{i} + {j}')
    return password


num = int(input('Введите число от 3 до 20: '))

result = get_pass(num)
print('Пароль:', result)