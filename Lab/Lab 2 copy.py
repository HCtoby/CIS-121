#Dog age
human_age = float(input("Please enter your age: "))
dog_age = human_age * 7
dogs_age = (float(dog_age) - int(dog_age)) * 12
dog_ages = (float(dogs_age) - int(dogs_age)) * 30
print("An age",human_age, "human should be", int(dog_age), "years", int(dogs_age), "mongths, and", int(dog_ages), "days in dog age.")

#Cat age
cat_age = human_age / 9
cat_ages = (float(cat_age) - int(cat_age)) * 12
cats_age = (float(cat_ages) - int(cat_ages)) * 30
print("An age", human_age, "human should be", int(cat_age), "years", int(cat_ages), "mongths, and", int(cats_age), "days in cat age.")

#Horse age
horse_age = 3 * (((human_age**2 - 47) / 7) + 12)
horses_age = (float(horse_age) - int(horse_age)) * 12
horse_ages = (float(horses_age) - int(horses_age)) * 30
print("An age", human_age, "human should be", int(horse_age), "years", int(horses_age), "mongths, and", int(horse_ages), "days in horse age.")
