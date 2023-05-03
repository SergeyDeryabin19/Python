from datetime import datetime
import os
import time


output_number =\
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
"dot":\
    """
         
      ■  
         
      ■  
         """,
"nothing":\
    """
         
         
         
         
         """
    
}

def clear_screen():
  os.system('CLS')

def print_result(hour_1, hour_2, minute_1, minute_2, second_1, second_2):
  line_1 = hour_1.splitlines()
  line_2 = hour_2.splitlines()
  line_3 = minute_1.splitlines()
  line_4 = minute_2.splitlines()
  line_5 = second_1.splitlines()
  line_6 = second_2.splitlines()
  dot = output_number['dot']
  dot_new = dot.splitlines()
  nothing = output_number['nothing']
  nothing_new = nothing.splitlines()
  if datetime.now().second % 2 == 0:
    for i in range (len(line_1)):
      print(f'{line_1[i]}, {line_2[i]}, {nothing_new[i]}, {line_3[i]}, {line_4[i]}, \
            {nothing_new[i]}, {line_5[i]}, {line_6[i]}')
  elif datetime.now().second % 2 != 0:
    for i in range (len(line_1)):
      print(f'{line_1[i]}, {line_2[i]}, {dot_new[i]}, {line_3[i]}, {line_4[i]}, \
            {dot_new[i]}, {line_5[i]}, {line_6[i]}')
  
def null_check(our_number):
  check_lenght = len(str(our_number))
  if check_lenght == 3:
    first_number = 0
    second_number = our_number[0]
    our_number = [first_number, second_number]
  return our_number

def new_hour(today_time):
  split_hour = [int(a) for a in str(today_time.hour)]
  new_split_hour = null_check(split_hour)
  new_split_hour_1, new_split_hour_2 = output_number[new_split_hour[0]], \
  output_number[new_split_hour[1]]
  return new_split_hour_1, new_split_hour_2

def new_minute(today_time):
  split_minute = [int(a) for a in str(today_time.minute)]
  new_split_minute = null_check(split_minute)
  new_split_minute_1, new_split_minute_2 = output_number[new_split_minute[0]], \
  output_number[new_split_minute[1]]
  return new_split_minute_1, new_split_minute_2

def new_second(today_time):
  split_second = [int(a) for a in str(today_time.second)]
  new_split_second = null_check(split_second)
  new_split_second_1, new_split_second_2 = output_number[new_split_second[0]], \
  output_number[new_split_second[1]]
  return new_split_second_1, new_split_second_2

def main():
  clear_screen()
  today_time=datetime.now()
  hour_1, hour_2 = new_hour(today_time)
  minute_1, minute_2 = new_minute(today_time)
  second_1, second_2 = new_second(today_time)
  print_result(hour_1, hour_2, minute_1, minute_2, second_1, second_2)
  time.sleep(1)

while True:
  main()