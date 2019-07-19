import random

if __name__ == '__main__':

    ksbyn = {'КАМЕНЬ': 0, 'СПОК': 1, 'БУМАГА': 2, 'ЯЩЕРИЦА': 3, 'НОЖНИЦЫ': 4}
    ksbyn_reverse = {v: k for k, v in ksbyn.items()}

    you = 0
    comp = 0

    while True:

        while True:
            x = input('Ваш ход: ').upper()
            if x in ksbyn:
                x = ksbyn[x]
                break
            else:
                print('Варианты ввода: камень, ножницы, бумага, ящерица, Спок')

        y = random.randint(0, 4)

        if (0 < x - y <= 2) or (-4 <= x - y <= -3):
            print('Ты выиграл! Компьютер ответил', end=' ')
            you += 1
        elif x == y:
            print('Ничья, компьютер тоже выбрал', end=' ')
        else:
            print('Ты проиграл! У компьютера', end=' ')
            comp += 1
        print(ksbyn_reverse[y])

        if you == 3 or comp == 3:
            print('Ты выиграл ' + str(you) + ' раз')
            print('Компьютер выиграл ' + str(comp) + ' раз')
            break
