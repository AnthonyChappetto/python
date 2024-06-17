import random  # random module is imported

def check_num_easy(easy1, randnum):
    easy1 = int(input())
    if isinstance(easy1, str):
        print("Answer must be an integer number")
        easy()
    if easy1 > 10:
        print("Guess is too large, number must be between 1 and 10.")
        easy()
    randnum = random.randint(1, 10)
    return easy1, randnum

def easy():
    print("Guess a number 1-10")
    check_num_easy(x, y)
    while x != y:
        print("Sorry, your guess of " + str(x) + " is not equal to " + str(y) + ". Try again!")
        check_num_easy()
    print("Congratulations! Your guess of " + str(x) + " is equal to " + str(y) + "!")
    print("Try again? (1) Or go back to level difficulty")
    x = input()
    if x == '1':
        easy()
    else:
        main()

def medium():
    return
def hard():
    return
def main():
    print("Guess the number minigame! Chose what level you want!")
    print("Type '1' for Easy (1-10)\nType '2' for Medium (1-100)\nType '3' for Hard (1-1000)\nType '4' to quit")
    choice = input()
    match choice:
        case "1":
            easy()
        case "2":
            medium()
        case "3":
            hard()
        case "4":
            exit(0)
        case _:
            print("Invalid choice, must be either 1, 2, or 3")
            main()

main()


#print(randnum)

