from datetime import datetime, time
import time
import os
from digits import zero, one, two, three, four, five, six, seven, eight, nine, space


def get_current_time():
    t_now = datetime.now().time()
    hour = t_now.strftime("%H")
    minutes = t_now.strftime("%M")
    seconds = t_now.strftime("%S")
    time = [hour, minutes, seconds]
    return time

def print_digits(current_time):
    clock_numbers = {'0' : zero, '1' : one, '2': two, '3' : three, '4' : four, '5' : five, '6' : six, '7' : seven, '8' : eight, '9' : nine}
    for i in range(5):
        print(clock_numbers[current_time[0][0]][i] + clock_numbers[current_time[0][1]][i] + clock_numbers[current_time[1][0]][i]  + clock_numbers[current_time[1][1]][i] + clock_numbers[current_time[2][0]][i] + clock_numbers[current_time[2][1]][i])


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep_for_a_while(period):
    time.sleep(period)

if __name__ == "__main__":
    while True:
        current_time = get_current_time()
        print_digits(current_time)
        sleep_for_a_while(0.3)
        clear_screen()
        



