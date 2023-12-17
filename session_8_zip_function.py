#zip function
name=["dada","kaka","mama"]
num=[3662,3211,4221]
for nm,inf in zip(num,name):
    print(nm,inf)

#zip to unmatch list
name=["dada","papa","kaka","mama"]   #not use mama to output
num=[3662,3211,4221]
for nm,inf in zip(num,name):
    print(nm,inf)
    
from itertools import zip_longest      #zip_longest  is in itertool
name=["dada","papa","kaka","mama"]  
num=[3662,3211,4221]
for nm,inf in zip_longest(num,name):   #use zip_longest() to print non match item
    print(nm,inf)  #it print unmatch item with none value
    
    
from itertools import zip_longest      #zip_longest  is in itertool
name=["dada","papa","kaka","mama"]  
num=[3662,3211,4221]
for nm,inf in zip_longest(num,name,fillvalue=0): #use fillvalue
    print(nm,inf)  #it print unmatch item with 0 value  
    
