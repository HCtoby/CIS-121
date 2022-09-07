human_age = float(input("Please enter your age: "))
dog_age = human_age * 7
dogs_age = (float(dog_age) - int(dog_age)) * 12
dog_ages = (float(dogs_age) - int(dogs_age)) * 30
print("An age",human_age, "human should be", int(dog_age), "years", int(dogs_age), "mongths, and", int(dog_ages), "days in dog age.")
print(dogs_age)