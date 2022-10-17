# def random_value(num):
#     import random
#     L1 = []
#     L2 = []
#     for i in range(num):
#         L1.append(random.randint(0,num))
#         L2.append(random.randint(0,num))
#     return [L1 L2]

# number = int(input("Please enter how many number u want: "))
# print(random_value(number))

''

# import random

# def createList(amout):
#     L1 = []
#     L2 = []
#     for i in range(amout):
#         L1.append(random.randint(1,amout))
#         L2.append(random.randint(1,amout))
#     return [L1,L2]
# print(createList(5))



""



# def count_num(word):
#     word1 = word
#     word1 = { }
#     litter_a = 0
#     litter_u = 0
#     for i in word:
#         if i == "a":
#             litter_a+=1
#         if i == "u":
#             litter_u+=1
#         word1["a"]=litter_a
#         word1["u"]=litter_u
#     return word1

# print(count_num("apple"))



""



# def running_gread(x):
#     info = {}
#     count = 1
#     L1 = []
#     h = 0
#     ave = 0
#     while count<=10:
#         time = input("Please how many min u run 4 miles: ")
#         L1.append(time)
#         count+=1
#     for i in len(L1):
#         ave = (ave + i)/len(L1)
#         if L1[i] < L1[i+1]:
#             h = L1[i+1]
#         elif L1[i]==L1[i+1]:
#             pass
#         else:
#             h =L1[i]
#     for i in len(L1):
#         info[i]=L1[i]


''

# def run():
#     info ={
#         "Times":[],
#         "Ave":0,
#         "Best Time":0,
#         "Worst Time":0
#     }

#     for i in range(10):
#         user = int(input("Enter ur time: "))
#         info["Times"].append(user)

#     if user>info["Worse Time"]:
#         info["Worse Time"]=user

#     if user<info["Best Time"]:
#         info




""


L1 = [1,2,3]
L2 = ["num 1","num 2","num 3"]

# def times5(L1,L2):
#     dict = {}
#     if len(L1)==len(L2):
#         for i in L2:
#             if i.isdigit():

    
    
    

#         for i in range(len(L1)):
#             dict[L2[i]]=L1[i]*5
#     return dict

# print(times5(L1,L2))


''


# def createDict(L1,L2):
#     info ={}
    
#     for i in range(len(L1)):
#         info[L2[i]]=L1[i]

#     info["num "+str(L1[i])*5]=L1[i]*5
    
#     return info

# print(L1,L2)


