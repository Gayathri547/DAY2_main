from datetime import timedelta, datetime
date = datetime(2021, 5, 10)
date += timedelta(days=1)
l = input("enter subjects list:\n").split(",")

for i in range(len(l)):
    for ele in l:
        date += timedelta(days=1)
        print(date, end ="")
        print("\t" + ele)
  