#use of filter()
age=[21,17,43,19]
adults=filter(lambda age:age<=18, age)
for i in adults:
    print(i)
