counter=0
while counter<10:



    total=0
    check_number = 0
    
    
    try:

        check_number = int(input('Write the number which you want to check it is  Armstrong.'))  

    except :
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!") 

    if check_number < 0:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
     
    if check_number > 0:
        for i in str(check_number):

            total+=int(i)**len(str(check_number))
        if total==check_number:
            print('{} is an Armstrong number'.format(check_number))


        else:

            print('{} is not an Armstrong number'.format(check_number))
    counter+=1
            
