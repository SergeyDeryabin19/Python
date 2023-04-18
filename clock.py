import datetime
import os
import time



dict_nombers={0: "zero",
              1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              }


def screen_clear():
    os.system("CLS")
    

def print_result(continue_hour, continue_minute, continue_second):
    print(f"{continue_hour} {continue_minute} {continue_second}")
    

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
    new_current_hour=f"{dict_nombers[new_current_splited_hour[0]]} {dict_nombers[new_current_splited_hour[1]]}"
    return new_current_hour
    

def new_vew_minute(current_time_number):
    current_minute = current_time_number.minute
    splited_minute = [int(a) for a in str(current_minute)]
    new_current_splited_minute=chek_zero(splited_minute)
    new_current_minute=f"{dict_nombers[new_current_splited_minute[0]]} {dict_nombers[new_current_splited_minute[1]]}"
    return new_current_minute
    

def new_vew_second(current_time_number):
    current_second = current_time_number.second
    splited_second = [int(a) for a in str(current_second)]
    new_current_splited_second=chek_zero(splited_second)
    new_current_second=f"{dict_nombers[new_current_splited_second[0]]} {dict_nombers[new_current_splited_second[1]]}"
    return new_current_second
    

def main():
    screen_clear()
    current_time_number = current_time()
    continue_hour=new_vew_hour(current_time_number)
    continue_minute=new_vew_minute(current_time_number)
    continue_second=new_vew_second(current_time_number)
    print_result(continue_hour, continue_minute, continue_second)
    time.sleep(0.5)
    
    
    
       
while True:
    main()










# new_current_hour=dict_nombers[current_hour]
# print(new_current_hour)



# if d.hour == 14:
#     print("""14
#           """)
