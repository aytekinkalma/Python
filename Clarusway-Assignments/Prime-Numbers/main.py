def prime_number(a):
    counter=0
    for i in range(2,a):
        if a%i==0:
            counter+=1
    if counter==0 and a!=1:
        return True
    else:
        return False

ln=int(input('Give the limit for prime number list'))
prime_list=[]
for i in range(1,ln):
    if prime_number(i):
        prime_list.append(i)
print(prime_list)
