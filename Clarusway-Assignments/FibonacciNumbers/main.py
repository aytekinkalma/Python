#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

l=[1,1]

for i in range(2,10):
    l.append(l[i-1]+l[i-2])
print(l)
