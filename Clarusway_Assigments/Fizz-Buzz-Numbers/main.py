for i in range(1,51):
    if i % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
        
    elif i % 3 == 0:
        print("fizz")
        continue
        
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)
