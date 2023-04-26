import datetime
import os
import time



dict_num=\
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
    tochki=dict_num["tochki"]
    tochki_sp=tochki.splitlines()
    ne_tochki=dict_num["netochki"]
    ne_tochki_sp=ne_tochki.splitlines()
    if datetime.datetime.now().second % 2 == 0:
        for i in range(len(lines1)):
            print("{} {} {} {} {} {} {} {}".format(lines1[i], lines2[i],\
                ne_tochki_sp[i], lines3[i], lines4[i], ne_tochki_sp[i],\
                    lines5[i], lines6[i]))
    elif datetime.datetime.now().second % 2 != 0:
        for i in range(len(lines1)):
            print("{} {} {} {} {} {} {} {}".format(lines1[i], lines2[i],\
                tochki_sp[i], lines3[i], lines4[i], tochki_sp[i], lines5[i],\
                    lines6[i]))
    

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


def all_in_one(input_number):
    splited_number = [int(a) for a in str(input_number)]
    new_num=chek_zero(splited_number)
    new_num_1, new_num_2=dict_num[new_num[0]],dict_num[new_num[1]]
    return new_num_1, new_num_2
        

def main():
    screen_clear()
    current_time_number = current_time()
    continue_hour_1, continue_hour_2=all_in_one(current_time_number.hour)
    continue_minute_1, continue_minute_2=all_in_one(current_time_number.minute)
    continue_second_1, continue_second_2=all_in_one(current_time_number.second)
    print_result(continue_hour_1, continue_hour_2, continue_minute_1,\
        continue_minute_2, continue_second_1, continue_second_2)
    time.sleep(1)
    
     
    

    #something
       
while True:
    main()