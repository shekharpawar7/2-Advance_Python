#combinations()
from itertools import combinations
lst=["shekhar","sanjivani","pawar"]
for comp in combinations(lst, 2):
    print(comp)
#output:    
('shekhar', 'sanjivani')
('shekhar', 'pawar')
('sanjivani', 'pawar')

#..............................................................................
#permutations()    
from itertools import permutations
lst=["shekhar","sanjivani","pawar"]
for per in permutations(lst, 2):
    print(per)
#output:    
('shekhar', 'sanjivani')
('shekhar', 'pawar')
('sanjivani', 'shekhar')
('sanjivani', 'pawar')
('pawar', 'shekhar')
('pawar', 'sanjivani')