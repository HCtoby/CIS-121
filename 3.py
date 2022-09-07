human_ages = float(input("Please enter your age: "))
cat_age = human_ages / 9
cat_ages = (float(cat_age) - int(cat_age)) * 12
cats_age = (float(cat_ages) - int(cat_ages)) * 30
print("An age", human_ages, "human should be", int(cat_age), "years", int(cat_ages), "mongths, and", int(cats_age), "days in cat age.")