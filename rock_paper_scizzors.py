import random
user_choice = int(input("Welcome to the python rock paper scizzors game, type 0 for rock, 1 for paper and 2 for scissors: "))
computer_choice = random.randint(0,2)
rock = '''  
           _______
       ---'   ____)  
            (_____)  
            (_____)  
            (____)
      ---.__(___)  
    '''
paper = ''' 
         _______
     ---'   ____)____  
               ______)  
              _______)  
             _______)
     ---.__________)  
        '''
scissors = '''  
        _______
    ---'   ____)____  
              ______)  
            _________)  
            (____)
    ---.__(___)  
        '''  

game_images = [rock, paper, scissors]

if user_choice >= 3:
    print("You have typed an invalid number, You lose")
elif user_choice == 0:
    print("\nYou chose:")
    print(game_images[0])
    print("Computer chose:")
    if computer_choice == 0:
        print(game_images[0])
        print("Looks like you have tied")
    elif computer_choice == 1:
        print(game_images[1])
        print("You lose")
    else:
        print(game_images[2])
        print("You win")
elif user_choice == 1:
    print("\nYou chose:")
    print(game_images[1])
    print("Computer chose:")
    if computer_choice == 0:
        print(game_images[0])
        print("You win")
    elif computer_choice == 1:
        print(game_images[1])
        print("Looks like you have tied")
    else:
        print(game_images[2])
        print("You lose")
elif user_choice == 2:
    print("\nYou chose:")
    print(game_images[2])
    print("Computer chose:")
    if computer_choice == 0:
        print(game_images[0])
        print("You lose")
    elif computer_choice == 1:
        print(game_images[1])
        print("You win")
    else:
        print(game_images[2])
        print("Looks like you have tied")
