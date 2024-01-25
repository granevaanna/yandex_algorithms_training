# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E.
# Замок Иф сложен из кирпичей, размером A × B × C.
# Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие,
# если стороны кирпича должны быть параллельны сторонам отверстия.
#
# Формат ввода
# Программа получает на вход числа A, B, C, D, E.
#
# Формат вывода
# Программа должна вывести слово YES или NO.

def is_brick_in_a_rectangle(a, b, c, d, e):
    if a>0 and b>0 and c>0 and d>0 and e>0:
        combinations = [(a,b), (b,a), (a,c), (c,a), (b,c), (c,b)]
        for combination in combinations:
            if combination[0] <= d and combination[1] <= e:
                return 'YES'
        return 'NO'

def main():
    a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
    print(is_brick_in_a_rectangle(a, b, c, d, e))

assert is_brick_in_a_rectangle(1, 1, 1, 1, 1) == 'YES'
assert is_brick_in_a_rectangle(2, 2, 2, 1, 1) == 'NO'

main()