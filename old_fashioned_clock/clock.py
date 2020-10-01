from datetime import datetime, time



def get_current_time():
    t_now = datetime.now().time()
    time = t_now.strftime("%H:%M:%S")
    return time

def print_digits(current_time):
    pass

def clear_screen():
    pass

def sleep_for_a_while(period):
    pass

if __name__ == "__main__":
    while True:
        current_time = get_current_time()
        print_digits(current_time)
        clear_screen()
        sleep_for_a_while(0.3)



