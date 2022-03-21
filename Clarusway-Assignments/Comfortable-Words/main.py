print('If you want to exit please press E')
left = ['a', 'A', 'q', 'Q', 'z', 'Z', 'W', 'w', 's', 'S', 'x', 'X', 'e', 'E', 'd', 'D', 'C', 'c', 'R', 'r', 'f', 'F',
        'v', 'V', 't', 'g', 'h', 'T', 'G', 'H']
right = ['Y', 'H', 'N', 'n', 'h', 'y', 'u', 'j', 'm', 'U', 'J', 'M', 'I', 'K', 'O', 'L', 'i', 'k', 'o', 'l', 'p', 'P',
         'L']
while True:
    word = input('Enter the word which you want to test\n')
    a=True
    counter=0
    counter1=0

    if word == 'E':
        break
    for i in word:
        if i in left:
            counter += 1
            if len(word) == counter:
                print('{} uses only left-hand fingers'.format(False))
                break
        if i in right:
            counter1 += 1
            if len(word) == counter1:
                print('{} uses only right-hand fingers'.format(False))
                break
        if ((i not in right) and (i not in left)):
            a=False
            print('{} there is different type character.please try again'.format(False))
            break
    if len(word) != counter1 and len(word) != counter and a==True:
        print('{} (uses both hand fingers)'.format(True))

print('Exit Done!!!!')
