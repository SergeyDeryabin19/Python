import time
import os

digits = {
    '0': [' 000 ', '0   0', '0   0', '0   0', ' 000 '],
    '1': ['  0  ', ' 00  ', '  0  ', '  0  ', ' 000 '],
    '2': [' 000 ', '    0', ' 000 ', '0    ', ' 000 '],
    '3': [' 000 ', '    0', ' 000 ', '    0', ' 000 '],
    '4': ['0  0 ', '0  0 ', ' 000 ', '    0', '    0'],
    '5': [' 000 ', '0    ', ' 000 ', '    0', ' 000 '],
    '6': [' 000 ', '0    ', ' 000 ', '0   0', ' 000 '],
    '7': [' 000 ', '    0', '    0', '    0', '    0'],
    '8': [' 000 ', '0   0', ' 000 ', '0   0', ' 000 '],
    '9': [' 000 ', '0   0', ' 000 ', '    0', ' 000 ']
}

def display_time(hours, minutes, seconds, colon=True):
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(5):
        for digit in [hours[0], hours[1], minutes[0], minutes[1], seconds[0], seconds[1]]:
            print(digits[digit][i], end=' ')
            if colon and i == 1:
                print(' . ', end='')
            else:
                print('   ', end='')
        print()

while True:
    current_time = time.localtime()
    hours = str(current_time.tm_hour).zfill(2)
    minutes = str(current_time.tm_min).zfill(2)
    seconds = str(current_time.tm_sec).zfill(2)
 
    if int(hours) < 24 and int(minutes) < 60 and int(seconds) < 60:
        colon = current_time.tm_sec % 2 == 0
        display_time(hours, minutes, seconds, colon)

    time.sleep(1)