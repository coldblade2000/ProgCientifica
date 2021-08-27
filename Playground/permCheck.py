
amigos = [1,2,3,4,5,6,7]

import itertools
perms = list(itertools.permutations(amigos))
print("size", len(perms))
count = 0
for x in perms:
    for i,amigo in enumerate(x):
        if i < 6 and (amigo == 1 and x[i+1] == 2):
            print(x)
            count = count + 1

print(count)