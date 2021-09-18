import math
l = input("enter a list\n").split(",")
for i in l:
    if int(i) >=10 and int(i) <=50:
        print(math.pow(int(i),2))
