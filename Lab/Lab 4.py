number = int(input("Please enter an upper bound for a check: "))
print("Between 1 and", number,"there are")

numbers = 1
num = 1
sum_divisors = 0
deficient = 0
perfect = 0
abundant = 0

while numbers <= number:          #This loop will check the number witch lower than the upper bound
    while num < numbers:          #This loop will check what the numbers is
        if numbers % num == 0:
            sum_divisors = sum_divisors + num
        num += 1
    if sum_divisors < numbers:
        deficient += 1
    elif sum_divisors == numbers:
        perfect += 1
    elif sum_divisors > numbers:
        abundant += 1
    num = 1
    sum_divisors = 0
    numbers += 1


print(deficient,"deficient number")
print(perfect,"perfect number")
print(abundant,"abundant number")
print("Thanks using is, have a good day :)")