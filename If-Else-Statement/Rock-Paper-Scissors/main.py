import random

a = {'rock': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    ,
     'paper': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    ,
     'scissors': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}
counter = 0
counter_computer = 0
total_score = 0
while total_score <= 3:

    choice = int(input('What do you choose?Type 0 for Rock,Type 1 for Paper or 2 for Scissors'))
    computer = random.choice(list(a))

    #     ------------------------------------------
    if choice == 0 and computer == 'rock':
        print('{}\n {} \n Competer Chose:\n {} \n There is no winner!!try again'.format(choice, a['rock'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))
    elif choice == 0 and computer == 'paper':
        counter_computer += 1
        total_score += 1
        print('{}\n {} \n Competer Chose:\n {} \n You Lose'.format(choice, a['rock'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))

    elif choice == 0 and computer == 'scissors':
        total_score += 1
        counter += 1
        print('{}\n {} \n Competer Chose:\n {} \n You win '.format(choice, a['rock'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))
    # ------------------------------------------------------------------------------
    elif choice == 1 and computer == 'paper':
        print(
            '{}\n {} \n Competer Chose:\n {} \n There is no winner!!try again'.format(choice, a['paper'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))
    elif choice == 1 and computer == 'rock':
        counter += 1
        total_score += 1
        print('{}\n {} \n Competer Chose:\n {} \n You Win'.format(choice, a['paper'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))

    elif choice == 1 and computer == 'scissors':
        total_score += 1
        counter_computer += 1
        print('{}\n {} \n Competer Chose:\n {} \n You lose '.format(choice, a['paper'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))

    # ------------------------------------------------------------------------------------

    elif choice == 2 and computer == 'scissors':
        print('{}\n {} \n Competer Chose:\n {} \n There is no winner!!try again'.format(choice, a['scissors'],
                                                                                        a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))
    elif choice == 2 and computer == 'rock':
        counter_computer += 1
        total_score += 1
        print('{}\n {} \n Competer Chose:\n {} \n You Lose'.format(choice, a['scissors'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))

    elif choice == 2 and computer == 'paper':
        total_score += 1
        counter = 1
        print('{}\n {} \n Competer Chose:\n {} \n You win '.format(choice, a['scissors'], a[computer]))
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))

    if total_score == 3 and counter > counter_computer:
        print('You win the game')
        print('you:{}\ncomputer:{}'.format(counter, counter_computer))
        break
    elif total_score == 3 and counter < counter_computer:
        print('you cant race with computer')
        break
