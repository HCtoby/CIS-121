#Haozhe Chen
#09/08/2202

income = int(input("Enter the amount of imcome your earned in 2022: "))
marrystatus = "a"
print("Are you are married or single?")


while marrystatus != "m" and marrystatus != "s":
    marrystatus = str(input("Enter m for married and s for single :"))
    print("You have to and only can type 'm' or 's'!")


if marrystatus == "m":
    if income <= 19900:
        tex = income / 10
        earned = income - tex

    elif income <= 81050:
        tex = income / 100 * 12
        earned = income - tex

    elif income <= 172750:
        tex = income / 100 * 22
        earned = income - tex

    else:
        tex = income
        earned = income - tex

elif marrystatus == "s":    
    if income <= 9950:
        tex = income / 10
        earned = income - tex

    elif income <= 40525:
        tex = income / 100 * 12
        earned = income - tex

    elif income <= 86375:
        tex = income / 100 * 22
        earned = income - tex

    else:
        tex = income
        earned = income - tex


earned = income - tex

print("According to our tex rate, sence you are", marrystatus, "marry status, you should to pay", tex, "as your tex.", "This year you earned", earned, "without tex.")