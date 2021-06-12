def number_hit_game():

    answer = 10
    
    print("This is hit number game")
    print("Please input number >>>")
    print(answer)

    a = input()
    guess = int(a)
    print(type(guess))

    trial = 1
    
    while answer != guess:
        trial += 1
        print("You input wrong number")
        print("next challenge?")
        a = input()
        guess = int(a) 
    else:
        print("You good")
        print("trial_number is")
        text = ("{trial} + time")
        print(text)

if __name__ == "__main__":
    number_hit_game()