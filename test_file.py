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
    ■■■■■"""
}

def split_number(number):
    list = []
    for line in number.split("\n"):
        if not line.strip():
            continue
        list.append(line.lstrip())
    n_0, n_1, n_2, n_3, n_4 = list[0], list[1], list[2], list[3], list[4]
    return n_0, n_1, n_2, n_3, n_4 

def split_number_return_list(number):
    list = []
    for line in number.split("\n"):
        if not line.strip():
            continue
        list.append(line.lstrip())
    
    return list


def list_print(income_list):
    print(income_list[0])
    print(income_list[1])
    print(income_list[2])
    print(income_list[3])
    print(income_list[4])
    


def print_spline_number(string_0, string_1, string_2, string_3, string_4):
    print(string_0)
    print(string_1)
    print(string_2)
    print(string_3)
    print(string_4)
    
    

# n_0, n_1, n_2, n_3, n_4 = split_number(dict_nombers[8])
# print_spline_number(n_0, n_1, n_2, n_3, n_4) 



def print_spline_number(string_0, string_1, string_2, string_3, string_4, string_5, string_6, string_7, string_8, string_9): 
    lines_0 = string_0.splitlines()
    lines_1 = string_1.splitlines()
    lines_2 = string_2.splitlines()
    lines_3 = string_3.splitlines()
    lines_4 = string_4.splitlines()
    lines_5 = string_5.splitlines()
    lines_6 = string_6.splitlines()
    lines_7 = string_7.splitlines()
    lines_8 = string_8.splitlines()
    lines_9 = string_9.splitlines()

    for i in range(len(lines_2)):
        print(lines_0[i] + "   " + lines_1[i]\
            + "   " + lines_2[i]+ "   " + lines_3[i]\
                + "   " + lines_4[i]+ "   " + lines_5[i]\
                    + "   " + lines_6[i]+ "   " + lines_7[i]\
                        + "   " + lines_8[i]+ "   " + lines_9[i])


string_0, string_1, string_2, string_3, string_4,\
    string_5, string_6, string_7, string_8, string_9=\
        dict_nombers[0],dict_nombers[1],dict_nombers[2],dict_nombers[3],dict_nombers[4],\
            dict_nombers[5],dict_nombers[6],dict_nombers[7],dict_nombers[8],dict_nombers[9]
            
print_spline_number(string_0, string_1, string_2, string_3, string_4,\
    string_5, string_6, string_7, string_8, string_9)

 



# a=dict_nombers[2].split(" ")
# print(a[0])
# b=","
# print(b.join(a))

# print(b.join(a),b.join(a))
# print(dict_nombers[2].split("-"))
import time
import os
while True:
    current_time = time.localtime()
    hours = str(current_time.tm_hour).zfill(2)
    minutes = str(current_time.tm_min).zfill(2)
    seconds = str(current_time.tm_sec).zfill(2)
 
    if int(hours) < 24 and int(minutes) < 60 and int(seconds) < 60:
        colon = current_time.tm_sec % 2 == 0  # проверка на четность секунд
        display_time(hours, minutes, seconds, colon)

    time.sleep(1)