#assigment operter
lsit_a=[2,3,4,5,6]
lsit_b=lsit_a     #hold same object
lsit_a[0]=-10   

print(lsit_a)    #[-10, 3, 4, 5, 6]
print(lsit_b)     #[-10, 3, 4, 5, 6]

#shallow copies
from copy import copy
list_a=[2,3,4,5,6]
list_b=copy(list_a)  #differnt-diffent object to each list
list_a[0]=-10    
print(list_a)    #[-10, 3, 4, 5, 6]
print(list_b)    #[2, 3, 4, 5, 6]



list_a=[[2,3,4,5,6],[8,7,0,6,3],[2,3,5,6]]
list_b=copy(list_a)    #effect the other list
list_a[0][0]=-10    
print(list_a)    #[[-10, 3, 4, 5, 6], [8, 7, 0, 6, 3]]
print(list_b)   #[[-10, 3, 4, 5, 6], [8, 7, 0, 6, 3]]


#deep copies 
#full indenpentent clones. use copy.deepcopy()
from copy import deepcopy
list_a=[[2,3,4,5,6],[8,7,0,6,3],[2,3,5,6]]
list_b=deepcopy(list_a)  
list_a[0][0]=-10    
print(list_a)    #[[-10, 3, 4, 5, 6], [8, 7, 0, 6, 3], [2, 3, 5, 6]]
print(list_b)    #[[2, 3, 4, 5, 6], [8, 7, 0, 6, 3], [2, 3, 5, 6]]
