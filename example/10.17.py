# def random_number(num,limit):
#     import random
#     temp = []
#     count = 1
#     while count <= num:
#         x = random.randint(1,limit)
#         temp.append(x)
#         count+=1
#     return temp

# num = int(input("Please enter how many number u want: "))
# limit = int(input("Please enter the higher bound u want: "))

# data = random_number(num,limit)

# def count_times(data):
#     info = {
#         "Number 10":0,
#         "Number 24":0,
#         "Number 7":0,
#         "Number 11":0
#     }
#     for i in data:
#         if i == 10:
#             info["Number 10"]+=1
#         elif i == 24:
#             info["Number 24"]+=1
#         elif i ==7:
#             info["Number 7"]+=1
#         elif i == 11:
#             info["Number 11"]+=1
#     return info

# print(data)
# print(count_times(data))



""





# dict1={
#     "Data":[0],
#     "Info":"NA"
# }
# dict2={
#     "Data":[3],
#     "Stats":"NA",
#     "Info":"NA"
# }


# def togather(d1,d2):
#     dict = {}

#     for i in d2:
#         dict[i].append(d2[i])
#         if dict[i]==d1[i]:
#             dict[i].append(dict[i]+d1[i])
    
#     for i in d1:
#         if dict[i]!=d1[i]:
#             dict[i].append(d1[i])
#     return dict

# print(togather(dict1,dict2))


# ''


# def checkdict(data1,data2):
#     result={}
    
#     for key in data1:
#         if key not in result:
#             result[key]=data1[key]
    
#     for i in data2:
#         if i not in result:
#             result[i]=data2[i]
#         else:
#             result[i].append(data2[i])
#     return result



""



# import random
# temp = []
# count = 1
# while count <= 300:
#     x = random.randint(1,2000)
#     temp.append(x)
#     count+=1

# with open("random_number.txt","w") as f:
#     for i in range(len(temp)):    
#         f.write(temp[i]+"\n")


# def ofile(filename):
#     l1 = []
#     file = open(filename,"r")
#     data = file.read().splitlines()
#     for i in data:
#         if i.isdigit():
#             l1.append(i)
#     for i in range(len(l1)):
#         if l1[i]%2==0:
#             l1[i]=l1[i]+" Even"
#         else:
#             l1[i]=l1[i]+" Old"
#     with open(filename,"w") as f: 
#         for i in range(len(l1)):
#             f.write(l1(i)+"\n")
# ofile("random_number.txt")   


# ''


# def add(filename):
#     file = open(filename,"r")
    

