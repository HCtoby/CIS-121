import Lab.Haozhe_Chen_Stats as Haozhe_Chen_Stats


file = open("50DayFruitData.txt","r")
data = file.read().splitlines()
data.pop(0)
apple_num = []


for item in data:
    temp = item.split()
    if temp[1] == "apple":
        apple_num.append(int(temp[2]))

a_mean = Haozhe_Chen_Stats.mean(apple_num)
a_median = Haozhe_Chen_Stats.median(apple_num)
a_mode = Haozhe_Chen_Stats.mode(apple_num)



dict = {
    "mean":round(a_mean,1),
    "median":a_median,
    "mode":a_mode
}


with open("Haozhe_Chen_Output.txt","w") as f:
    
    ###The normol 

    # f.write("The mean number of apples eaten is: "+str(a_mean)+"\n"
    # +"The median number of apple eaten is: "+str(a_median)+"\n"
    # +"The mode number of apple eaten is: "+str(a_mode)+"\n")

    ###From dictionarie

    for i in dict:
        f.write("The "+i+" number of apples eaten is: "+str(dict[i])+"\n")