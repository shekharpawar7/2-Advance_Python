#Generater #tuple Compreshesion
#it return multimuple value
#implemented using function
#tuple compreshenion create one object we can access using for loop

gen=(x for x in range(5))   #creating Opject
print(gen)      #output:<generator object <genexpr> at 0x000001B8D72665A0>
for num in gen:
    print(num)

gen=(x for x in range(7))   #creating Opject
print(gen)      
next(gen)  #0
next(gen)  #1
next(gen)  #2



