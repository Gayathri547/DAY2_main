list1 = input("enter 1st list:\n").split(",")
list2 = input("enter 2nd list:\n").split(",")
pair = [(list1[i],list2[i]) for i in range(0,len(list1))]
print(pair)