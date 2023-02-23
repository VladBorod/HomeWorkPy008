# Редактирование данных.

def edit_base():
    edit_data = input("Введите Имя или Фамилию для редактирования записи из справочника : ").upper()
    list1 = []
    with open("base.txt") as f:
        for line in f:
            if edit_data not in line.split():
                list1.append(line)
            else:
                list1.append(input('Введите новые данные: ').upper())
    with open("base.txt", "w") as f:
        f.writelines(list1)

