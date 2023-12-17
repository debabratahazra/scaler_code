def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    height = int(input())   # height in centimeter
    height = height / 100   # height in meters
    weight = int(input())  # weight in kg

    bmi = weight / (height * height)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 24.9:
        print("Normal")
    elif bmi >= 24.9 and bmi < 29.9:
        print("Overweight")
    else:
        print("Obese")

    print(bmi)
    return 0


if __name__ == '__main__':
    main()
