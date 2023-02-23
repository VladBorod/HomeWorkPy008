# Удаление данных.

def delete_base():
    edit_data = input('Введите Имя или Фамилию для удаления записи из справочника: ').upper()
    with open('base.txt') as f:
        list_temp = []
        for line in f:
            if edit_data in line.split():
                print(f'{line} удалена ')
                continue
            else:
                list_temp.append(line)
    with open('base.txt', 'w') as f:
        f.writelines(list_temp)