humans_age = float(input("Please enter your age: "))
horse_age = 3 * (((humans_age**2 - 47) / 7) + 12)
horses_age = (float(horse_age) - int(horse_age)) * 12
horse_ages = (float(horses_age) - int(horses_age)) * 30
print("An age", humans_age, "human should be", int(horse_age), "years", int(horses_age), "mongths, and", int(horse_ages), "days in horse age.")
print(horse_age)