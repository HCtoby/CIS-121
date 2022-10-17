from math import trunc


L1 = ["Number 1","Number 2","Number 3"]
L2 = [1,2,3]

# def take_list_to_make_a_dict(L1,L2):
#     dict = {}
#     for i in L1:
#         dict.append(i)
#         print(dict)
#     for a in len(L2):
#         dict[a].append(L2)
#     return dict

# take_list_to_make_a_dict(L1,L2)

# print(dict)




# def createDictionary(keys,data):
#     temp ={ }
#     if len(data) == len(keys):
#         for i in range(len(keys)):
#             temp[keys[i]] = data[i]
#     return temp

# print(createDictionary(L1,L2))



""



# info = {
#     "NUm 1":"12",
#     "NUm 2":"abcs",
#     "Num 3":"56",
# }


# def MultipleNumber(data):
#     num = 1
#     for i in data:
#         if data[i].isdigit():
#             num = num * int(data[i])
#     return num
# print(MultipleNumber(info))

    

# def multiplyValues(data,number):
#     for key in data:
#         if data[key].isdigit():
#             print(data[key],number,int(data[key])*number)


# multiplyValues(info,2)



""



def generate_number(data,number):
    count = 1
    data = {}
    L1 = []
    while count <= number:
        num = int(input("Please enter your number: "))
        L1.append(num)
        count += 1
    for i in len(L1):
        data.append[i]=L1[i]
    return data



def match_number(dict):
    import random
    num = 0
    for i in dict:
        num = num + dict[i]
    times = 0
    s = 0
    while s !=1:
        x = random.randint(0,num)
        for b in dict:
            if x == dict[b]:
                s == 1
        else:
            times +=1
    return times


        
''


def createDictionary():
    temp = {}
    for i in range(5):
        temp["number"+str(i+1)]=i*2
    return temp

def getData(data):
    temp = []
    for i in data:
        temp.append(data[i])
        return temp


def guessNUmber(data):
    import random
    guess = False
    
    values = getData(data)

    while guess != True:
        random_number = random.randint(1,1000)

        if random_number in values:
            print("Found one!",random_number)
            guess = True



