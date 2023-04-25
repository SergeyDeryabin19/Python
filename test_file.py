from colorama import init, Fore, Back, Style

# Инициализация colorama
init()

# Примеры использования цветов
print(Fore.RED + "Красный текст" + Fore.RESET)
print(Back.GREEN + "Зеленый фон с черным текстом" + Back.RESET)
print(Style.DIM + "Тусклый текст" + Style.RESET_ALL)
import datetime
import os
import time



dict_nombers=\
{0:\
    """
    ■■■■■
    ■   ■
    ■   ■
    ■   ■
    ■■■■■""",
1:\
    """
      ■  
     ■■  
    ■ ■  
      ■  
    ■■■■■""",
2:\
    """
    ■■■■■
    ■   ■
      ■  
    ■    
    ■■■■■""",
3:\
    """
    ■■■■ 
        ■
      ■  
        ■
    ■■■■ """,
4:\
    """
    ■   ■
    ■   ■
    ■ ■ ■
        ■
        ■""",
5:\
    """
    ■■■■■
    ■    
    ■ ■ ■
        ■
    ■■■■■""",
6:\
    """
    ■■■■■
    ■    
    ■ ■ ■
    ■   ■
    ■■■■■""",
7:\
    """
    ■■■■■
        ■
      ■  
      ■  
      ■  """,
8:\
    """
    ■■■■■
    ■   ■
    ■■■■■
    ■   ■
    ■■■■■""",
9:\
    """
    ■■■■■
    ■   ■
    ■ ■ ■
        ■
    ■■■■■""",
"tochki":\
    """
         
      ■  
         
      ■  
         """,
"netochki":\
    """
         
         
         
         
         """

    
}



def screen_clear():
    os.system("CLS")
    

def print_result(continue_hour_1, continue_hour_2, continue_minute_1,\
    continue_minute_2, continue_second_1, continue_second_2):
    lines1 = continue_hour_1.splitlines()
    lines2 = continue_hour_2.splitlines()
    lines3 = continue_minute_1.splitlines()
    lines4 = continue_minute_2.splitlines()
    lines5 = continue_second_1.splitlines()
    lines6 = continue_second_2.splitlines()
    tochki=dict_nombers["tochki"]
    tochki_sp=tochki.splitlines()
    ne_tochki=dict_nombers["netochki"]
    ne_tochki_sp=ne_tochki.splitlines()
    color=[Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    if datetime.datetime.now().second % 2 == 1:
        for i in range(len(lines1)):
                print(color[i] + "{} {} {} {} {} {} {} {}".format(lines1[i], lines2[i],\
                ne_tochki_sp[i], lines3[i], lines4[i], ne_tochki_sp[i],\
                lines5[i], lines6[i] + Fore.RESET))
    elif datetime.datetime.now().second % 2 != 1:
        for i in range(len(lines1)):
                print(color[i] + "{} {} {} {} {} {} {} {}".format(lines1[i], lines2[i],\
                tochki_sp[i], lines3[i], lines4[i], tochki_sp[i], lines5[i],\
                lines6[i] + Fore.RESET))
        
                            
    

def chek_zero(our_number):
    chek_len = len(str(our_number))
    if chek_len==3:
        firs_number = 0
        second_number = our_number[0]
        our_number=[firs_number, second_number]
    return our_number


def current_time():
    current_time = datetime.datetime.now()
    return current_time

def new_vew_hour(current_time_number):
    current_hour = str(current_time_number.hour)
    splited_hour = [int(a) for a in str(current_hour)]
    new_current_splited_hour=chek_zero(splited_hour)
    new_current_splited_hour_1=dict_nombers[new_current_splited_hour[0]]
    new_current_splited_hour_2=dict_nombers[new_current_splited_hour[1]]
    return new_current_splited_hour_1, new_current_splited_hour_2
    

def new_vew_minute(current_time_number):
    current_minute = current_time_number.minute
    splited_minute = [int(a) for a in str(current_minute)]
    new_current_splited_minute=chek_zero(splited_minute)
    new_current_splited_minute_1=dict_nombers[new_current_splited_minute[0]]
    new_current_splited_minute_2=dict_nombers[new_current_splited_minute[1]]
    return new_current_splited_minute_1, new_current_splited_minute_2
    

def new_vew_second(current_time_number):
    current_second = current_time_number.second
    splited_second = [int(a) for a in str(current_second)]
    new_current_splited_second=chek_zero(splited_second)
    new_current_splited_second_1=dict_nombers[new_current_splited_second[0]]
    new_current_splited_second_2=dict_nombers[new_current_splited_second[1]]
    return new_current_splited_second_1, new_current_splited_second_2
    

def main():
    screen_clear()
    current_time_number = current_time()
    continue_hour_1, continue_hour_2=new_vew_hour(current_time_number)
    continue_minute_1, continue_minute_2=new_vew_minute(current_time_number)
    continue_second_1, continue_second_2=new_vew_second(current_time_number)
    print_result(continue_hour_1, continue_hour_2, continue_minute_1,\
        continue_minute_2, continue_second_1, continue_second_2)
    time.sleep(1)
    
    
    
    
       
while True:
    main()