print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers seperated by commas (eg 5,67,32)")

def get_user_input ():
    global temp
    numbers = input()
    list1 = numbers.split(",")
    temp = list(map(float, list1))
    print(temp)


def calc_average(x):
    print("calc_average")
    average_temperature = sum(x) / len(x)
    return print("average temperature ="+str(average_temperature))
def find_min_max(x):
    print("find_min_max")
    min_max_list = [min(x), max(x)]
    print(min_max_list)
def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")

display_main_menu()
get_user_input()
calc_average(temp)
find_min_max(temp)