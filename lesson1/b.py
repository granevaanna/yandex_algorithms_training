# Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами. Если это возможно, выведите строку YES, иначе выведите строку NO.\
# Треугольник — это три точки, не лежащие на одной прямой.
#
# Формат ввода
# Вводятся три натуральных числа.
#
# Формат вывода
# Выведите ответ на задачу ('YES' или 'NO').

def isTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 'YES'
    else:
        return 'NO'

assert isTriangle(3, 4, 5) == 'YES'
assert isTriangle(3, 5, 4) == 'YES'
assert isTriangle(4, 5, 3) == 'YES'
assert isTriangle(2, 3, 5) == 'NO'

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(isTriangle(a, b, c))

main()