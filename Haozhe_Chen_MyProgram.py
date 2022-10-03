import Haozhe_Chen_Stats


file = open("500DayFruitData.txt","r")
data = file.read().splitlines()
data.pop(0)
apple_num = []
banana_num = []
Strawberry_num = []


for item in data:
    temp = item.split()
    if temp[1] == "apple":
        apple_num.append(int(temp[2]))
    elif temp[1] == "banana":
        banana_num.append(int(temp[2]))
    else:
        Strawberry_num.append(int(temp[2]))

a_mean = Haozhe_Chen_Stats.mean(apple_num)
a_median = Haozhe_Chen_Stats.median(apple_num)

b_mean = Haozhe_Chen_Stats.mean(banana_num)
b_median = Haozhe_Chen_Stats.median(banana_num)

s_mean = Haozhe_Chen_Stats.mean(Strawberry_num)
s_median = Haozhe_Chen_Stats.median(Strawberry_num)

print("The mean number of apples eaten is: ",a_mean)
print("The median number of apples eaten is: ",a_median)

print("The mean number of bananaa eaten is: ",b_mean)
print("The median number of bananas eaten is: ",b_median)

print("The mean number of straberries eaten is: ",s_mean)
print("The median number of strawrries eaten is: ",s_median)

with open("Haozhe_Chen_Output.txt","w") as f:
    f.write("The mean number of apples eaten is: "+str(a_mean)+"\n"+"The median number of apple eaten is: "+str(a_median)
    +"\n"+"The mean number of bananaa eaten is: "+str(b_mean)+"\n"+"The median number of bananas eaten is: "+str(b_median)
    +"\n"+"The mean number of straberries eaten is: "+str(s_mean)+"\n"+"The median number of strawrries eaten is: "+str(s_median))
