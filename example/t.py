# for i in range(1,7):
#     for j in range(1,6):
#         print(j,end=" ")
#     print(" ")


""


import random

# def str_to_int(data):
#   temp = []
  
#   for number in data:
#     if number.isdigit():
#       temp.append(int(number))    

#   return temp

# def add_5(data):
#   temp = []
#   for number in data:
#     temp.append(number+5)

#   return temp

def write_to_file(data,name):
  with open(name+".txt","w") as f:
    for number in data:
      f.write(str(number) +"\n")


  
# names = ["Kendrick","Morales"]

# info = {
#   "Kendrick": 23,
#   "Bob": 3456
# }


# #Open a file
# file = open("data.txt",'r')
# #Get data from file, remeber everything from a file is a consider a str
# data = file.read().splitlines()

# print(data)

# #Create a function that takes a list of values in str and returns a new list with only int.

# data = str_to_int(data)
# print(data)


# #Create a function that takes the numbers and adds 5 to them. 
# data = add_5(data)

# print(data)


# #Write the results to a new file

# with open("results.txt","w") as f:
#   for number in data:
#     f.write(str(number) +"\n")


#Generate a random number
a = random.randint(1,100)

#Part 1
#Generate a list with 100 random values. Then write the values to a file called "random_numbers_generated.txt"

rand = []

for i in range(100):
  rand.append(random.randint(1,100))
  
#writing to a file
write_to_file(rand,"random_numbers_generated")



#USE THE DOCS
#Part 2
#Create a function that counts how many times each number appears. Use a dict to keep track of it. 
def count_num(data):

  temp = {}

  for number in data:
    if str(number) in temp:
      pass
    else:
      temp[str(number)] = data.count(number)

  return temp


c = count_num(rand)


#Part C
#Write the info from dict to a file called final.txt


with open("final.txt",'w') as f:
  for key in c:
    f.write(key+": "+str(c[key])+'\n')

# 1,2,3
# "1" : 3
# "2" : 1
# "3" : 2



  