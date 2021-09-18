from datetime import datetime

my_string1 = str(input('Enter 1st date(yyyy-mm-dd): '))
my_string2 = str(input('Enter last date(yyyy-mm-dd): '))

f_date = datetime.strptime(my_string1, "%Y-%m-%d")
l_date = datetime.strptime(my_string2, "%Y-%m-%d")

diff = l_date - f_date
print("The number of days between those 2 are\n" , diff.days)