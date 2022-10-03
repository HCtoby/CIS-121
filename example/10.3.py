# info = {
#     "patient 0": ["Haozhe","Chen",2],
#     "patient 1": 23,
#     "patient 2": ["Bob","builder",45]
# }



""



# name = input("Please enter your fitst name: ")
# names = input("Please enter your last name: ")
# age = input("Please enter your age: ")
# info = {
#     name : [name,names,age]
# }

# print(info[name])



""

# count = 0
# while count < 5:
#     name = input("What is the name of soccer players: ")
#     goals = input("How mane goals he has made in this season: ")
#     info = {}
#     info[count] =  [name,goals]
#     count += 1
# print(info)



# def ave_goals(players):
#     sum = 0
#     for player in players:
#         sum += players[player]
#     return sum/len(players)
    
# players = {}
# for i in range(5):
#     name = input("Enter the players name: ")
#     goals = int(input("Enter how mane goals he has made in this season: "))
#     players[name] = goals


""



# def check(info,name):
#     names = input("Please enter the name witch you want check: ")
#     count = len(info)
#     stop = 1
#     while stop == 1:
#         if names == info[names]:
#             print("The kay about",names,"is exist!")
#             print(info[names])
#             stop = 0
        
#         if count < 0:
#             print("Sorry the kay is not found.")
#             stop = 0

#         count = count - 1



# info = {
#     "Test 0":0,
#     "Test 1":1,
#     "Test 2":2,

# }

# def check_keys(data,key):
#     keys = input("enter your key: ")
#     for key in data:
#         if keys == key:
#             return True
#         return False

# print(check_keys(info,"Test 2"))



""


info1 = {
    "data" : [1,2,3,4,5]
}
info2 = {
    "data" : [6,7,8,9,10]
}

# info3 = {}
# info3 = info1 + info2


# print(info3)


def add_togather(data,data2):
    total = []
    for i in range(len(data["data"])):
        total.append(data["data"][i]+data2["data"][i])
    print(total)

add_togather(info1,info2)


