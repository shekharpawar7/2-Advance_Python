#program for to create an iterator from saeral iterables in a and
# display the type and element of new iterator
from itertools import chain
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
result=chain_fun([1,2,3,4], ['a',"s","f","c"], [2,4,6,7,8,4,4])
print("type of the new itertor:",type(result))
print("elements of new itertor:")
for i in result:
    print(i,end="")   #1234asfc2467844
    
#tuple
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
result=chain_fun((1,2,3,4), ('a',"s","f","c"), (2,4,6,7,8,4,4))
print("type of the new itertor:",type(result))
print("elements of new itertor:")
for i in result:
    print(i,end="")   #1234asfc2467844

#..............................................................................
#generates the ruuning product of elemnt in an iterable
from itertools import accumulate
import operator
def running_prod(lst):
    return accumulate(lst,operator.mul)
result=running_prod([2,3,5,6,7,4])
print(result)#object
for i in result:
    print(i)
    
#......................................................................
#program for to construct an infinite iterator that 
#that return evenly spaced value starting with specifed number and step
import itertools as it
start=10
step=1
print("the stating num is",start,"and ending is",step)
my_counter=it.count(start,step)
for i in my_counter:
    print(i)
    
#...............................................................................
#generte an infinte cycle of elements from iterable
from itertools import cycle
def cycle_def(data):
    return cycle(data)

result=cycle_def(["a","f","v","g"])
for i in result:
    print(i)

#string
def cycle_def(data):
    return cycle(data)

result=cycle_def("python itertools")
for i in result:
    print(i)        

#............................................................................
#program for to make iterator that drop elements from
#the iterable as soon as an element is a positive number
from itertools import dropwhile
def drop_while(*nums):
    return dropwhile(lambda x: x<0,nums)
result=drop_while(-3,-5,-6,-7,-2,7,3,2,3)
for i in  result:
    print(i)
    
    