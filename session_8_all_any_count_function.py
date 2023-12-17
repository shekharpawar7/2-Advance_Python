#use of all()
#if 0 in list it return useless
lst=[1,34,5,742,85]
if all(lst):                   
    print("0 is not present") #0 is not present
else:
    print("0 is present")
    
    
lst=[1,34,5,742,85,0]
if all(lst):
    print("0 is not  present")
else:
    print("0 is present")    #0 is present

#......................................................................
#use of any()
#if any value is present
lst=[0,0,7,0,0,0]
if any(lst):                   
    print("its has a some value") #printed
else:
    print("all are zero")
    
lst=[0,0,0,0,0,0]
if any(lst):                   
    print("its has a some value") 
else:
    print("all are zero")  #printed
    
#......................................................................
#use of count()
#its create a object
#use next() to acces value
from itertools import count
counter=count()
print(next(counter)) #0
print(next(counter))  #1
print(next(counter))   #2


from itertools import count
counter=count(start=1)   #START FROM 1
print(next(counter)) #1
print(next(counter))  #2
print(next(counter))   #3
