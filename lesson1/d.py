# Решите в целых числах уравнение:
# sqrt(a*x+b) = c
# a, b, c – данные целые числа. Найдите все решения или сообщите, что решений в целых числах нет.
#
# Формат ввода
# Вводятся три числа a, b и c по одному в строке.
#
# Формат вывода
# Программа должна вывести все решения уравнения в порядке возрастания,
# либо NO SOLUTION (заглавными буквами), если решений нет.
# Если решений бесконечно много, вывести MANY SOLUTIONS.

def solve_equation(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    if a == 0:
        if b == c**2:
            return 'MANY SOLUTIONS'
        return 'NO SOLUTION'
    x = (c**2 - b) / a
    if x.is_integer():
        return int(x)
    return 'NO SOLUTION'

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve_equation(a, b, c))

assert solve_equation(1, 0, 0) == 0
assert solve_equation(1, 2, 3) == 7
assert solve_equation(1, 2, -3) == 'NO SOLUTION'

assert solve_equation(0, 4, 2) == 'MANY SOLUTIONS'
assert solve_equation(0, 5, 5) == 'NO SOLUTION'
assert solve_equation(5, 4, 4) == 'NO SOLUTION'

main()