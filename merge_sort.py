import random


def merge_sort(a, lb=0, ub=-1):
    def merge(a, lb, split, ub):
        # Слияние упорядоченных частей массива в буфер temp
        # с дальнейшим переносом содержимого temp в a[lb]...a[ub]

        # текущая позиция чтения из первой последовательности a[lb]...a[split]
        pos1 = lb

        # текущая позиция чтения из второй последовательности a[split+1]...a[ub]
        pos2 = split + 1

        # текущая позиция записи в temp
        pos3 = 0

        temp = [i for i in range(ub - lb + 1)]

        # идет слияние, пока есть хоть один элемент в каждой последовательности
        while pos1 <= split and pos2 <= ub:
            if a[pos1] < a[pos2]:
                temp[pos3] = a[pos1]
                pos1 += 1
                pos3 += 1
            else:
                temp[pos3] = a[pos2]
                pos2 += 1
                pos3 += 1

        # одна последовательность закончилась -
        # копировать остаток другой в конец буфера
        while pos2 <= ub:  # пока вторая последовательность непуста
            temp[pos3] = a[pos2]
            pos3 += 1
            pos2 += 1
        while pos1 <= split:  # пока первая последовательность непуста
            temp[pos3] = a[pos1]
            pos3 += 1
            pos1 += 1

        # скопировать буфер temp в a[lb]...a[ub]
        a[lb:ub + 1] = temp

        del(temp)

    if lb < ub:  # если есть более 1 элемента
        split = (lb + ub) // 2  # индекс, по которому делим массив
        merge_sort(a, lb, split)  # сортировать левую половину
        merge_sort(a, split + 1, ub)  ##сортировать правую половину
        merge(a, lb, split, ub)  # слить результаты в общий массив


n = 500000
a = [0] * n
for i in range(n):
    a[i] = random.randint(0, 100000)


merge_sort(a, 0, len(a)-1)

for i in range(n):
    print(a[i])
