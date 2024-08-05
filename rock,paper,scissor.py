import random
a=input("choose one:\n 1.rock\n 2.paper\n 3.scissor\n Your choice: ")
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



