# ###  Haozhe Chen                  
                  
#                   ### Question 1

# # read file's content 
# L1 = []
# file = open("steps.txt","r")
# data = file.read().splitlines()
# for i in data:
#     if i.isdigit():
#         L1.append(i)

# # determain is the numbers are odd or even
# info ={}
# even = []
# odd = []
# for i in L1:
#     if int(i) % 2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)
# info["even"]=even
# info["odd"]=odd

# # write to a file
# with open("exam_2_even_or_odd_number.txt","w") as f:
#     f.write("Even : "+str(info["even"])+"\n"
#     +"Odd : "+str(info["odd"])+"\n")


                ### Question 2

#  Generate two list
import random

list1 = []
list2 = []
for i in range(200):
    list1.append(random.randint(1,100))
    list2.append(random.randint(1,100))

# count times of number
list3 = list1+list2
info = {}
num = 1
for i in list3:
    count = 0
    if num == i:
        count +=1
    info.append[num]=count
    num += 1

# Write to a file
with open("RESULTS4.txt","w") as f:
    for i in range(len(info)):
        f.write(i+info[i]+"\n")


                ### Question 3

# read file's content 
L1 = []
file = open("steps.txt","r")
data = file.read().splitlines()
for i in data:
    if i.isdigit():
        L1.append(i)

# find average
import statistics

jen = statistics.average(0,31)
feb = statistics.average(30,59)
mar = statistics.average(58,90)
apr = statistics.average(89,120)
may = statistics.average(119,151)
june = statistics.average(150,181)
july = statistics.average(180,212)
aug = statistics.average(211,243)
sep = statistics.average(242,273)
oc = statistics.average(272,304)
nov = statistics.average(303,334)
dec = statistics.average(333,365)




print("Month         Average")
print(%2f.%15.2f)