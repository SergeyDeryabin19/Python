    # написать программу которая:
    # 1. запрашивает у пользователя логин
    # 2. Есть **функция** котороя выводит сумму на счете
    # 3. Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе,
    # то выводит сумму счета (выполняет функ из п 2) bla bla
    # 4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен
    
    
# while True:
#     def chek_login():
#         input_login = input("Введите логин  :")
#         if input_login == "admin":
#             key = True
#         else:
#             key = False
#         return key
    

#     def all_your_money(key):
#         if key == True:
#             print(" Ваша сумма на счете много денег ")
#         else:
#             print(" Доступ запрещен ")


#     chek_login = all_your_money(chek_login())
#     #конец
# def decorator(func):
#     def wrapper_decorator(*args, **kwargs):
#         value = f"сумма  счёта: {func(*args, **kwargs)}"
#         return value
#     return wrapper_decorator

# @decorator
# def adds():
#     return 2

# login_person = input('логин: ')
# if (login_person == 'admin'):
#       print(adds())  
# else:
#     print('Доступ запрещен')



input_login=input("Введите логин :")
def decorator(func):
    # new_func/func - висит в замыкании
    def wrapper_decorator(*args, **kwargs):
        if input_login=="admin":
            value = func(*args, **kwargs)
            return value
        else: print("Ты не админ, доступа нет") 
    return wrapper_decorator

@decorator
def chek_balance():
    print("Сумма на счете много денег")
    

chek_balance()
    
    
    
    
    
    
    
    
    
    