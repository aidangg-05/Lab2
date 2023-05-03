def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
if __name__ == "__main__":
    main()

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height * height)
    print(BMI)
    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif BMI >= 18.5 and BMI <= 25.0:
        print("Normal Weight")
        return 0
    elif BMI > 25.0:
        print("Over Weight")
        return 1

calculate_bmi(weight=57, height=1.73)
