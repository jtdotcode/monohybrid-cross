import itertools




p1 = ("X","y")
p2 = ("Z","a")

parents = p1 + p2

child = []


for subset in itertools.combinations(parents, 2):
  if(subset != p1 and subset != p2):
   print(subset)
   child.append(subset)

print(child)


