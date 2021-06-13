import random

def number_hit_game():
    
    print("This is hit number game")
    print("The number range is 1 ~ 100")

    answer = random.randrange(start=1, stop=100)  
    guess = int(input("please input number"))

    trial = 1
    
    while(guess != answer):
        trial += 1
        if(guess > answer):
            print("your input number is larger than the answer")
        else:
            print("your input number is smaller than the answer")
        trial += 1
        guess = int(input("please input number"))
    print("Collect! answer is {}".format(answer))
    print("trial number is {} times".format(trial))

if __name__ == "__main__":
    number_hit_game()