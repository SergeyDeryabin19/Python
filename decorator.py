    # написать программу которая:
    # 1. запрашивает у пользователя логин
    # 2. Есть **функция** котороя выводит сумму на счете
    # 3. Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе,
    # то выводит сумму счета (выполняет функ из п 2) bla bla
    # 4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен


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
    
    
    
    
    
    
    
    
    
    
