# Euclid's algorithm
def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 % num2 == 0:
        print(num2)
    else:
        new_num = num2
        new_num2 = num1 % num2
        gcd(new_num, new_num2)



gcd(1122, 867)