
### Open a file

# file = open("data.txt","r")

### Get data from file

# data = file.read().spilitlines()
# print(data)


# list = ["1","2","3","4","5"]

# def str_to_int(data):
#     intlist = []
#     info = data.read().splitlines()
#     for i in info:



# def str_to_int(data):
#     temp = []
#     for number in data:
#         if number.isdigit():
#             temp.append(int(number))
#     return temp
    


""



# def add_5_in_number(data):
#     temp = []
#     for number in data:
#         if number.isdigit( ):
#             number += 5
#             temp.append(number)
#     return temp


# def add_5(data):
#     temp = []
#     for number in data:
#         temp.append(number + 5)



""


# with open("results.txt","w") as f:
#     for number in data:
#         f.write(str(number)+"\n")

# import random
# a = random.randint(1,100)
# print(a)

### Part 1

# import random

# count = 1
# L1 = []
# while count<=100:
#     a = random.randint(1,3)
#     L1.append(a)
#     count += 1

# with open("result.txt","w") as f:
#     for number in L1:
#         f.write(str(number) + "\n")

### Part 2

# dic = {}

# num1 = 0
# num2 = 0
# num3 = 0


# file = open("result.txt","r")
# data = file.read().splitlines()
# for i in data:
#     if i == 1:
#         num1+=1
#     elif i ==2:
#         num2+=1
#     elif i ==3:
#         num3+=1
#     dic["1"]=[num1]
#     dic["2"]=[num2]
#     dic["3"]=[num3]
# print(dic)



""
# def count_num(data):
#     temp=()
#     for number in data:
#         if str(number) in temp:
#             pass
#         else:
#             temp[str(number)] = data.count(number)
#     return temp

# print(count_num(L1))



""
c = []

file = open("result.txt","r")
data = file.read().splitlines()
info = {}
info.append(data)
with open("rank.txt","w") as f:
    for i in info:
        f.write(i,"\n")

with open("final.txt","w") as f:
    f.write(c+": "+str(c[key])+"\n")

