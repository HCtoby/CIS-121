#Haozhe Chen
#09/08/2202

income = int(input("Enter the amount of imcome your earned in 2022: "))
marrystatus = "a"
status = 0

while status != 1:
    marrystatus = str(input("Are you are married or single? Enter m for married and s for single :"))
    if marrystatus == "m" or marrystatus == "s":
        if marrystatus == "m":
            if income <= 19900:
                tex = income / 10
            elif income <= 81050:
                tex = income / 100 * 12
            elif income <= 172750:
                tex = income / 100 * 22
            else:
                tex = income 
        elif marrystatus == "s":
            if income <= 9950:
                tex = income / 10
            elif income <= 40525:
                tex = income / 100 * 12
            elif income <= 86375:
                tex = income / 100 * 22
            else:
                tex = income
        earned = income - tex
        print("According to our tex rate, sence you are", marrystatus, "marry status, you should to pay", tex, "as your tex.", "This year you earned", earned, "without tex.")
        status = 1
    else:
        print("You have to and only can type 'm' or 's'!")