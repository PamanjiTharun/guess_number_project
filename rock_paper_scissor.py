import random
class ROCK_PAPER_SCISSOR:
    def game(self):
        while True:
            print("choose your choice: ")
            print("0.ROCK \n1.PAPER \n2.SCISSOR")
            print("-------------------")
            try:
                user_choice=int(input("Enter your choice:"))
                list_1=['ROCK','PAPER','SCISSOR']
                if user_choice<0 or user_choice>2:
                    print("you chosee wrong number you lose the game")
                else:
                    print(f"your choseen {list_1[user_choice]}")
                    computer_choice=random.randint(0,2)
                    print(f"computer choice is {list_1[computer_choice]}")
                    if user_choice == computer_choice:
                        print("<== Draw game ==>")
                    elif user_choice==0 and computer_choice==2:
                        print("<== You win the game ==>")
                    elif computer_choice==0 and user_choice==2:
                        print("<== You lose the game ==>")
                    elif computer_choice>user_choice:
                        print("<== You lose the game ==>")
                    elif user_choice>computer_choice:
                        print("<== You win the game ==>")            
            except ValueError:
                print("Invalid input you lose the game ")
            print("--------------------")
            user_choice=input("Do you want to play again (Y/N) : ")
            if user_choice=='n' or user_choice =='N'or user_choice.isdigit():
                print("<== Thanks for playing ==>")
                break    
              
print("game rules of ROCK PAPER SCISSOR")
print("ROCK VS PAPER -> PAPER WINS")
print("ROCK VS SICSSOR -> ROCK WINS")
print("PAPER VS SCISSOR -> SCISSOR WINS")
r=ROCK_PAPER_SCISSOR()
r.game()