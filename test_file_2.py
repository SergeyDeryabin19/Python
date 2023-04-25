from colorama import init, Fore

init()   # инициализация colorama

colors = [Fore.RED, Fore.GREEN, Fore.BLUE]   # список используемых цветов

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # список чисел, которые нужно вывести на экран

for i in range(len(numbers)):
    print(colors[i % len(colors)] + str(numbers[i])) # окрашиваем число в нужный цвет и выводим на экран