#it is a game where you have to guess the number and you have 5 chances and you have to guess the number in 5 chances with each correct guess you will get 10 points


import random

print("welcome to guess the number game")
print("This a game where you have to guess the number between 1 to 10 \nyou have 5 chances and you have to guess the number \nin 5 chances with each correct guess you will get 10 points")


def guess_number():
       number_guess=0
       correct_guess=0
# Generate a random number between 1 and 50
       number_to_guess = random.randint(1,10)
       while number_guess<10:
            number=int(input("Guess the number: "))  
            if(number>number_to_guess):
                  print("too high try again")
                  number_guess+=1
            elif(number<number_to_guess):
                  print("too low try again")
                  number_guess+=1
            else:
                  print("you guessed the right number")
                  number_to_guess = random.randint(1,10)
                  number_guess+=1
                  correct_guess+=1
       return (correct_guess*10)


if __name__=="__main__":
      points=guess_number()
      print(f"you got {points} points")
      with open("high_score.txt","r") as f:
            if(points>int(f.read())):
                  print("Congrates you got the high score")
                  print(f"New High score in {points} ")
                  with open("high_score.txt","w") as f:
                        f.write(str(points))

            else:
     
                 print("thank you for playing")
            
    
               

