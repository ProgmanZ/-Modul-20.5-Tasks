# Задача 2. Контакты 2

def enter_user_string():
    while True:
        user_string = input('\nВведите Фамилию, Имя и телефон через пробел: ').strip().split(' ')
        if len(user_string) != 3:
            print('Ошибка. Количество элементов в строке не равно трем.')
        elif user_string[0].isdigit() or user_string[1].isdigit():
            print('Ошибка. Имя и Фамилия не должны содержать цифры.')
        elif not user_string[-1].isdigit():
            print('Ошибка в номере. Допускаются только цифры')
        else:
            return tuple(user_string[:2]), user_string[-1]


def check_range(entered_range):
    while True:
        if not entered_range.isdigit():
            print('Ошибка. Неверно указано количество.')
        else:
            return int(entered_range)


def check_choice(entered_symbol):
    if entered_symbol.lower() == 'y':
        return True
    else:
        return False


def print_phone_book(phone_book):
    print('\nСодержимое телефонной книги сейчас:')
    for user_data, number_data in phone_book.items():
        print(' '.join(user_data), ':', number_data)


data_phonebook = dict()

for i in range(check_range(input('Введите количество добавляемых контактов: '))):
    choice = str()
    key_tuple, number = enter_user_string()
    if key_tuple in data_phonebook.keys():
        print(key_tuple[0], key_tuple[1], 'уже есть в телефонной книге.')

        if check_choice(input('Что бы заменить текущий номер у {0} {1} введите \'Y\' и нажмите \'Enter\': '.format(
                key_tuple[0], key_tuple[1]))):
            print_phone_book(data_phonebook)
            continue
    data_phonebook[key_tuple] = number
    print_phone_book(data_phonebook)
