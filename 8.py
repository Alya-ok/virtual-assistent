import random
import datetime
import math
print('Для того чтобы пользоваться Гошой - виртуальным помощником войдите в систему')
login = str('gosha12')
password = str('1234')
userlog = input('Введите логин: ')
userpas = input('Введите пароль: ')
while userlog != login or userpas != password:
    print('Неверный логин или пароль')
    userlog = input('Введите логин: ')
    userpas = input('Введите пароль: ')
else:
    print('Успешный вход')
name = str.title(input('Привет, я Гоша - виртуальный помощник, как мне к тебе обращаться?: '))
list1 = ['Какое сегодня число?',
         'Какое сейчас время?','Игра к-н-б',
         'Игра угадай число',
         'Игра орел или решка',
         'Калькулятор',
         'Калькулятор квадратных уравнений',
         'Магический шар',
         'Интересные факты о лягушках',
         'Таблица умножения',
         'Выйти из системы']
date_time = datetime.datetime.now()
user_help = int(input(f'{name}! Вот мой список возможностей:\n1 - {list1[0]}\n2 - {list1[1]}\n3 - {list1[2]}'
                      f'\n4 - {list1[3]}\n5 - {list1[4]}\n6 - {list1[5]}\n7 - {list1[6]}\n8 - {list1[7]}'
                      f'\n9 - {list1[8]}\n10 - {list1[9]}\n0 - {list1[10]}\nЧем могу помочь?: '))
while user_help != 0:
    if user_help == 1:
        print(f'Текущая дата: {date_time.date()}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 2:
        print(f'Текущее время: {date_time.time()}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 3:
        knb = ['1 - камень ', '2 - ножницы ', '3 - бумага ']
        print('Добро пожаловать в игру камень-ножницы-бумага')
        print(f'нужно выбрать 1 из вариантов:{knb}')
        v = int(input('Что вы выбираете?: '))
        while v < 1 or v > 3:
            v = int(input('Ошибка вы ввели не правильное число, попробуйте еще раз: '))
        else:
            if v == 1:
                print(f'Ваш выбор: {knb[0]}')
            if v == 2:
                print(f'Ваш выбор: {knb[1]}')
            if v == 3:
                print(f'Ваш выбор: {knb[2]}')
            bot = random.randint(0, len(knb) - 1)
            print(f'Выбор компьютера: {knb[bot]}')
            if v == bot + 1:
                print('Ничья')
            elif (v == 1 and bot == 1) or (v == 2 and bot == 2) or (v == 3 and bot == 0):
                print('Победа')
            else:
                print('Проигрыш')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 4:
        life = 7
        num = random.randint(1, 100)
        user = int(input(f'У тебя {life} жизней, угадай число от 1 до 100: '))
        while life > 1:
            while user < 1 or user > 100:
                user = int(input('Вы ввели число меньше 1 или больше 100 попробуйте еще раз: '))
            else:
                if user < num:
                    print('Число слишком маленькое')
                    life -= 1
                    user = int(input(f'У тебя {life} жизней, попробуй еще раз: '))
                elif user > num:
                    print('Число слишком большое')
                    life -= 1
                    user = int(input(f'У тебя {life} жизней, попробуй еще раз: '))
                else:
                    print(f'Ты угадал! это {num}')
                    break
        else:
            print(f'У тебя закончились жизни :( , число было {num}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 5:
        coin = ['Орел', 'Решка']
        useror = int(input(f'Привет, это игра Орел или Решка!\n1 - {coin[0]} '
                           f'\n2 - {coin[1]} '
                           f'\nЧто ты выберешь?: '))
        rand = random.randint(0, len(coin) - 1)
        while useror < 1 or useror > 2:
            useror = int(input('Ошибка, выберите 1 - Орел или 2 - Решка: '))
        else:
            if useror == rand + 1:
                print(f'Повезло! {coin[rand]}')
            else:
                print(f'Не повезло! {coin[rand]}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 6:
        a = float(input('введите первое число '))
        b = float(input('введите второе число '))
        print(f'Сумма: {a + b}'
              f'\n'f'Разность: {a - b}'
              f'\nПроизведение: {a * b}'
              f'\nДеление: {a / b}'
              f'\nЦелочисленное деление: {a // b}'
              f'\nОстаток деления: {a % b}'
              f'\nВозведение в степень: {a ** b}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 7:
        print('квадратное уравнение имеет вид: ax^2+bx+c=0')
        x = int(input('введи a: '))
        y = int(input('введи b: '))
        z = int(input('введи c: '))
        d = ((y ** 2) - 4 * x * z)
        if d < 0:
            print('нет корней')
        elif d == 0:
            x1 = ((-y + (math.sqrt(d))) / 2)
            print(f'корень уравнения: {x1}')
        else:
            x1 = ((-y + (math.sqrt(d))) / 2)
            x2 = ((-y - (math.sqrt(d))) / 2)
            print(f'корни уравнения: {x1, x2}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 8:
        otvet = ['Да', 'Нет', 'Может быть', 'Скорее да чем нет', 'Скорее нет чем да', '50 на 50']
        magic_ball = random.randint(0, len(otvet) - 1)
        quetion = input('Задай шару вопрос на который можно ответить Да или Нет: ')
        print(f'Шар думает что ответ.. {otvet[magic_ball]}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 9:
        facts = ['Лягушки живут по всему миру, на всех континентах, кроме Антарктиды, их насчитывается более 6 000 видов',
                 'Не все лягушки умеют прыгать',
                 'Большинство длинноногих видов лягушек могут прыгать на расстояние, превышающее длину их тела в 20 раз',
                 'Древесная лягушка, обитающая в Северной Америке, зимой замерзает, а весной оживает',
                 'Коренные народы на западе Колумбии сотни лет использовали кожу золотых ядовитых лягушек для наконечников дротиков для духовой трубки',
                 'Одна из самых необычных лягушек в мире это стеклянная лягушка']
        fact = random.randint(0,len(facts) - 1)
        print(f'Вот один рандомный факт о лягушках: {facts[fact]}')
        user_help = int(input('Чем еще могу помочь?: '))
    elif user_help == 10:
        for num1 in range(1, 10):
            for num2 in range(1, 10):
                print(f'{num1} * {num2} = {num1 * num2}')
            print('~~~~~~~~~~')
        user_help = int(input('Чем еще могу помочь?: '))
    else:
        user_help = int(input(f'Цифры {user_help} нет в списке моих возможностей, введите другое число: '))
else:
    print('Выход из системы')