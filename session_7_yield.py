#function return multiple value use yield
def range_even(end):   #function use like genretor
    for num in range(0,end,2):
        yield num
         
range_even(6)   #cretaing object

for num in range_even(6):  #access value using for loop
    print(num)

range_even(6)   #cretaing object
gen=range_even(6)   #value store in gen
next(gen)   #0
next(gen)   #1

#chaining 0f generaters
def length(ite):
    for ele in ite:
        yield len(ele)
#print(length("shekhar"))    #carete object

   
def hide(ite):
    for ele in ite:
        yield ele*'*'
#print(hide("shekhar"))        #create object

passwords=["Sp@122","pawar$222","dsanjiv2"]
for password in hide(length(passwords)):
    print(password)

#..........................................................................
import random
def random_gen(start,end):
        while True:
            yield random.randint(start,end)
            
start=int(input("enetr start:"))
end=int(input("enetr end:"))
random_num=random_gen(start, end)
#print(random_num)   #print object

for i in random_num:   #for one random number
    print(i)
    break

for _ in range(10):    #for 10 random number
    print(next(random_num))
 


    
    
    
  