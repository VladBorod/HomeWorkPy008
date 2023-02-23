# Внесение данных.

def input_base():
    with open('base.txt', 'a') as f:
        for i in range(int(input('Введите кол-во новых записей в справочник - '))):
            f.write(input('Введите ФИО и номер телефона: ')+'\n'.upper())
