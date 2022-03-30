liste = ["eat", "tea", "tan", "ate", "nat", "bat"]
a = []
b=[]
c=[]
for i in range(0, len(liste)):
    if len(set(liste[0]).union(set(liste[i]))) == len(set(liste[i])):
        a.append(liste[i])
for i in range(0,len(a)):
    liste.remove(a[i])
for i in range(0, len(liste)):
    if len(set(liste[0]).union(set(liste[i]))) == len(set(liste[i])):
        b.append(liste[i])
for i in range(0,len(b)):
    liste.remove(b[i])
c.append(a)
c.append(b)
c.append(liste)
print(c)
