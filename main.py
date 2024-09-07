from colorama import init as colorama_init
from colorama import Fore, Back
a = int(input("Сколько раз хотите повторить?"" "))
b = input("Что хотите повторить?"" ")
if a != int or a >100000:
    print("Это не число или нельзя так много")
    if b == int or len(b) > 100:
        print("Зачем такое большое предложение")
    else:
        for i in range(a):
            print(b)
        print(f"{Fore.CYAN}И да, {Fore.MAGENTA}ты знала, {Fore.BLUE}что хороших людей осталось {Fore.RED}мало?{Fore.GREEN} Так что береги себя {Fore.YELLOW}солнце<3")





