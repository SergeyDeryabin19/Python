# 1. многопольз калькулятор БМИ(словарь)
# 2. Храним рост, вес, пол,
# 3. Меню:CRUD(L)
#     1. Вывести список польз(ключ - login)(L)
#     2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ) (R)
#     3. Изменить данные о пользователе (выбираем соот во ключу) (U)
#     4. Удалить выбранного пользователя (D)
#     5. Добавить пользователя(C)
#     6. Выход


import os
all_dict = {}


def screen_clear():
    os.system("CLS")


def read_certain_person():
    print_people_list()
    certain_person = str(input("Выберите кого почитать : "))
    print(all_dict[certain_person])
    read_and_pass_the_screen()


def edit_person():
    screen_clear()
    print_people_list()
    certain_person = str(input("Выберите кого изменить : "))
    screen_clear()
    print(all_dict[certain_person])
    input_height = float(input("Введите рост тела, см: "))
    input_veight = float(input("Введите вес тела, кг: "))
    input_sex = input("Введите ваш пол, m/f: ")
    input_age = float(input("Введите ваш возраст, лет: "))
    bmi_value = round(input_veight/((input_height*0.01)**2))
    all_dict[certain_person]={"height": input_height, "weight": input_veight,"sex": input_sex, "age": input_age, "bmi": bmi_value}
    print(all_dict[certain_person])
    read_and_pass_the_screen()
    
    


def exit_from_programm():
    exit()


def read_and_pass_the_screen():
    input("Нажмите любую клавишу для продолжения: ")

def print_people_list():
    for item in all_dict:
        print(item)
        
def list_of_all_values():
    screen_clear()
    print_people_list()
    read_and_pass_the_screen()


def delete_person():
    screen_clear()
    print_people_list()
    chosen_weak_man = str(input("Введите удаляемого челика: "))
    del all_dict[chosen_weak_man]
    print(f"{chosen_weak_man} удален")
    read_and_pass_the_screen()


def print_menu_and_make_a_decision():
    screen_clear()
    print("""    1. Вывести список польз(ключ - login)(l)
    2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ) (r)
    3. Изменить данные о пользователе (выбираем соот во ключу) (u)
    4. Удалить выбранного пользователя (d)
    5. Добавить пользователя(c)
    6. Выход(e)""")
    option = input("Введите индентификатор требуемой операции ")
    return option


def create_new_person():
    screen_clear()
    global all_dict
    input_height = float(input("Введите рост тела, см: "))
    input_veight = float(input("Введите вес тела, кг: "))
    name_of_person = input("Введите имя пользователя: ")
    input_sex = input("Введите ваш пол, m/f: ")
    input_age = float(input("Введите ваш возраст, лет: "))
    bmi_value = round(input_veight/((input_height*0.01)**2))
    print("Ваш имт составляет ", bmi_value, " едениц")
    all_dict.update({name_of_person: {"height": input_height, "weight": input_veight,
                    "sex": input_sex, "age": input_age, "bmi": bmi_value}})
    screen_clear()


def make_a_decision(option):
    if option == "l":
        list_of_all_values()
    elif option == "r":
        read_certain_person()
    elif option == "u":
        edit_person()
    elif option == "d":
        delete_person()
    elif option == "c":
        create_new_person()
    elif option == "e":
        exit_from_programm()


def main():
    option = print_menu_and_make_a_decision()
    make_a_decision(option)


while True:
    main()
