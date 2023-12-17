#lsit_Conpehesion
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

lst=[num for num in range(0,20)] #lsit_name=[verible for verible in range(,)]
print(lst)

#Capitalize
names=["dada","mama","kaka"]
lst=[name.capitalize() for name in names]
print(lst)

#even number
def is_even(num):
    return num%2==0
lst=[num for num in range(0,20) if is_even(num)] 
print(lst)


lst=[f"{a}{b}" for a in range(3) for b in  range(3)]
print(lst)

#.............................................................................
#find all number between 1-1000 divide by 7
lit=[num for num in range(1,1000)  if num%7==0]
print(lit) 

#find all number between 1-1000 that have 3 in them
lit=[num for num in range(1,1000) if "3" in str(num)]
print(lit)

#count the number of spcae in string
some_string="the sun rice in north"
space =[s for s in some_string if s==" "]
print(len(space))

#create a list all the consonants in the string 
#"yrllo yaks like yrlling and yawaning and yesterday they yodled while eating uky yans"

sent="yrllo yaks like yrlling and yawaning and yesterday they yodled while eating uky yans"
result=[letter for letter in sent            if  letter not in 'a,e,u,i,o," "']
print(result)

#find commen number in two list without usin set ,tuple
list1=[3,7,4,8,0,6]
list2=[5,7,9,3,2,0]
list3=[ele for ele in list1     if ele in list2]
print(list3)

#get number in string
sent="in 1990 thene were 13 instance of a product with over 1000"
word=sent.split()      #split()- use to sentence to word by space
result=[num for num in word    if not num.isalpha()]#isalpha()- use to check alphabates
print(result)

#given number is even put in list Even if odd put odd
result=[]
for num in range(20):
    if num %2==0:
        result.append("even")
    else:
        result.append("odd")
print(result)

result=["even" if num%2==0 else "odd"  for num in range(20) ] #write if-else before for loop
print(result)


        
        
        
        
        
    


