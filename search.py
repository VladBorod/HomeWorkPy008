# Поиск данных.

def search_base():
    with open("base.txt") as f:
        find_feature = input("Введите одну из характеристик для поиска(фио или телефон - ").upper()
        flag = False
        for i in f:
            list_feature = i.split()
            if find_feature in list_feature:
                print(i, end="")
                flag = True
        if not flag:
            print("Такой записи не найдено")