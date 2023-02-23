# Файл контроллер.
# Импорт функций.

from input import input_base as ib
from read import read_base as rb
from search import search_base as sb
from edit import edit_base as eb
from delete import delete_base as db

# Функция основоного запуска.

while True:
    get_choice = (int(input(
        '''\n Введите 1 - для добавления записи.
         2 - Для вывода всего справочника. 
         3 - Для поиска. 
         4 - Для изменения данных.
         5 - Для удаления данных.         
         6 - Для завершения работы: ''')))
    match get_choice:
        case 1:
            ib()
        case 2:
            rb()
        case 3:
            sb()
        case 4:
            eb()
        case 5:
            db()
        case _:
            break