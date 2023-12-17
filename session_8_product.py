#product()
from itertools import product
team_a=["virat","rohit","pandya"]
team_b=["manish","saurbh","sami"]
for pair in product(team_a,team_b):
    print(pair)
#output:
    ('virat', 'manish')
    ('virat', 'saurbh')
    ('virat', 'sami')
    ('rohit', 'manish')
    ('rohit', 'saurbh')
    ('rohit', 'sami')
    ('pandya', 'manish')
    ('pandya', 'saurbh')
    ('pandya', 'sami')