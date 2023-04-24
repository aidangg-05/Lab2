def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height * height)
    print(BMI)
    if BMI < 18.5:
        print("Under Weight")
    elif BMI >= 18.5 and BMI <= 25.0:
        print("Normal Weight")
    elif BMI > 25.0:
        print("Over Weight")

calculate_bmi(weight=57, height=1.73)
