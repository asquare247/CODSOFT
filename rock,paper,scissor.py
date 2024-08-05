import random
while True:
    a=input("choose one:\n 1.rock\n 2.paper\n 3.scissor\n")
    print( "Your choice: ",a )
    s=['rock','paper','scissor']
    ai=random.choice(s)
    print("Computer choice: ",ai)

    if a==ai:
        print("Tie")
    elif a=='rock' and ai=='scissors':
        print("You win")
    elif a=='paper' and ai=='rock':
        print("You win")
    elif a=='scissor' and ai=='paper':
        print("You win")
    else:
        print("You lose")

    play=input("play again:(y/n)\n")
    if play=="y":
        continue
    elif play=="n":
        break
print("Thanks for playing")




