def check_factor(num1, num2):
    return num1 % num2 == 0


num1 = int(input("Enter your NUMBER!"))
num2 = int(input("What num do you want to check factor?: "))
if check_factor(num1, num2):
    print(f"{num2} is a factor of {num1}")
else:
    print(f"{num2} is NOT a factor of {num1}")
