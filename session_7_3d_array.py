#generte a 3*4*6 row/col/col  3d array each element having *
array=[[["*" for col in range(6)] for col in range(4)] for row in range(3) ]
print(array)

#write a python progream to print the number of a spcifiied lsit after removing 
#even number from it
num=[22,34,46,78,49,23,89,69]
list1=[n for n in num   if n%2!=0 ]
print(list1)
