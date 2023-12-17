  
import random
import string
adiectives=["red","orange","black","blue"]
nouns=["apple","banana","cherri","cat","dog"]

adiective=random.choice(adiectives)

noun=random.choice(nouns)
special_ch=random.choice(string.punctuation)
number=random.randrange(0,100)
passwoeds=adiective+noun+special_ch+str(number)
print(passwoeds)

#chaining 0f generaters
def length(ite):
    for ele in ite:
        yield len(ele)
#print(length("shekhar"))    #carete object

   
def hide(ite):
    for ele in ite:
        yield ele*'*'
#print(hide("shekhar"))        #create object


for password in hide(length(passwoeds)):
    print(password,end="")



   





