#..........................................................................
#USE OF CYCLE
#to repestrd tasks
from itertools import cycle
instruction=["eat","code","sleep"]
for inst in cycle(instruction):   #repeted print instructions
    print(inst)

import itertools
instruction=["eat","code","sleep"]
for inst in itertools.cycle(instruction):   #repeted print instructions
    print(inst)
    
#..........................................................................
#use of repeat()
import itertools
for mag in itertools.repeat("keep",times=3):   #wait for 3 sec
    print(mag)
    
