#new file for oopё
numbers={
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
    
}
from datetime import datetime
current_datetime = datetime.now() 
new_hour=[int(a) for a in str(current_datetime.hour)]
print(new_hour)
print(numbers[new_hour[0]],numbers[new_hour[1]])
    
    

