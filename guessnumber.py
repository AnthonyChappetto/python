import random  # random module is imported

def check_num_easy():   # checks the number for the easy function
    try:    # try exception for determining if input is an int or not
        user_guess = int(input("Enter your guess: "))    # takes user input for a guess
        if user_guess > 10:  
            print("Guess is too large, number must be between 1 and 10.")   # error if guess > 10
            return check_num_easy()
        elif user_guess == 0 or user_guess < -1:
            print("Guess is too small, number must be between 1 and 10.")   # error if guess < 1
            return check_num_easy()
        elif user_guess == -1:  #failsafe exit
            quit(0)
    except ValueError:  
        print("Answer is not an integer number")    # error checking for non-int input
        return check_num_easy()
    return user_guess    #returns user input

def check_num_med():
    try:    # try exception for determining if input is an int or not
        user_guess = int(input("Enter your guess: "))    # takes user input for a guess
        if user_guess > 100:  
            print("Guess is too large, number must be between 1 and 100.")   # error if guess > 100
            return check_num_med()
        elif user_guess < -1 or user_guess == 0:
            print("Guess is too small, number must be between 1 and 100.")   # error if guess < 1
            return check_num_med()
        elif user_guess == -1:  #failsafe exit
            quit(0)
    except ValueError:  
        print("Answer is not an integer number")    # error checking for non-int input
        return check_num_med()
    return user_guess    #returns user input

def check_num_hard():
    try:    # try exception for determining if input is an int or not
        user_guess = int(input("Enter your guess: "))    # takes user input for a guess
        if user_guess > 1000:  
            print("Guess is too large, number must be between 1 and 1000.")   # error if guess > 1000
            return check_num_hard()
        elif user_guess < -1 or user_guess == 0:
            print("Guess is too small, number must be between 1 and 1000.")   # error if guess < 1
            return check_num_hard()
        elif user_guess == -1:
            quit(0)
    except ValueError:  
        print("Answer is not an integer number")    # error checking for non-int input
        return check_num_hard()
    return user_guess    #returns user input

def easy():
    count = 1
    randnum = random.randint(1,10)
    print("\nGuess a number between 1 and 10")
    x = check_num_easy()
    while x != randnum:
        print("Sorry, your guess of " + str(x) + " is not equal to " + str(randnum) + ". Try again!")
        count = count + 1
        randnum = random.randint(1,10)
        check_num_easy()
    print("Congratulations! Your guess of " + str(x) + " is equal to " + str(randnum) + "! It only took you " + str(count) + " guesses!")
    print("Try again? (1) Or press any other key to go back to level difficulty selection")
    choice = input()
    if choice == '1':
        return easy()
    else:
        return main()

def medium():       #Need to add in count
    randnum = random.randint(1,100)
    print("\nGuess a number between 1 and 100")
    x = check_num_med()
    while x != randnum:
        print("Sorry, your guess of " + str(x) + " is not equal to " + str(randnum) + ". Try again!")
        randnum = random.randint(1,100)
        check_num_med()
    print("Congratulations! Your guess of " + str(x) + " is equal to " + str(randnum) + "!")
    print("Try again? (1) Or press any other key to go back to level difficulty selection")
    choice = input()
    if choice == '1':
        return medium()
    else:
        return main()

def hard():     #need to add in count
    randnum = random.randint(1,1000)
    print("\nGuess a number between 1 and 1000")
    x = check_num_hard()
    while x != randnum:
        print("Sorry, your guess of " + str(x) + " is not equal to " + str(randnum) + ". Try again!")
        randnum = random.randint(1,1000)
        check_num_hard()
    print("Congratulations! Your guess of " + str(x) + " is equal to " + str(randnum) + "!")
    print("Try again? (1) Or press any other key to go back to level difficulty selection")
    choice = input()
    if choice == '1':
        return hard()
    else:
        return main()

def main():
    print("Guess the number minigame! Chose what level you want!\n")
    print("Type '1' for Easy (1-10)\nType '2' for Medium (1-100)\nType '3' for Hard (1-1000)\n\nType any other key to quit")
    choice = input()
    match choice:
        case "1":
            easy()
        case "2":
            medium()
        case "3":
            hard()
        case _:
            exit(0)

main()

# Idea to add a counter of how many times it took to reach correct answer
# After 5 incorrect guesses inform user about failsafe