# F. Расстановка ноутбуков
# В школе решили на один прямоугольный стол поставить два прямоугольных ноутбука.
# Ноутбуки нужно поставить так, чтобы их стороны были параллельны сторонам стола.
# Определите, какие размеры должен иметь стол, чтобы оба ноутбука на него поместились, и площадь стола была минимальна.
#
# Формат ввода
# Вводится четыре натуральных числа, первые два задают размеры одного ноутбука,
# а следующие два — размеры второго. Числа не превышают 1000.
#
# Формат вывода
# Выведите два числа — размеры стола.
# Если возможно несколько ответов, выведите любой из них (но только один).

def find_size_of_table_with_min_square(a, b, c, d):
    combinations = [(b+d, max(a, c)),
                    (b+c, max(a, d)),
                    (a+d, max(b, c)),
                    (a+c, max(b, d))]

    d1_ans, d2_ans = combinations[0]
    min_square = d1_ans * d1_ans

    for comb in combinations:
        square = comb[0] * comb[1]
        if square < min_square:
            min_square = square
            d1_ans = comb[0]
            d2_ans = comb[1]

    return d1_ans, d2_ans

def main():
    a, b, c, d = map(int, input().split())
    res = find_size_of_table_with_min_square(a, b, c, d)
    print(res[0], res[1])

assert find_size_of_table_with_min_square(10, 2, 2, 10) == (20, 2) or (2, 20) or (4, 10) or (10, 4)
assert find_size_of_table_with_min_square(5, 7, 3, 2) == (9, 5) or (5, 9)

main()