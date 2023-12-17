#Enumerate

lat=["maik","egg","butter"]
for index in range(len(lat)):
    print(f"{index+1}:{lat[index]}")

lst=["milk","buttter","egg"]
for index,value in enumerate(lst): #using enumerate
    print(f"{index+1}:{value}")