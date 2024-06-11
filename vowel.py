def keepgoing():
    print("Try another letter? (1) Or go back? (2)")
    choice = input()
    if choice == '1':
        vowel_or_cons()
    elif choice == '2':
        main()
    else:
        print("Incorrect option")
        exit(1)

def vowel_or_cons():
    print("Type a single character")
    x = input()
    if len(x) > 1:
        print("Needs to be 1 character only")
        vowel_or_cons()
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        print("This letter is a vowel")
        keepgoing()
    else:
        print("This letter is a consonant")
        keepgoing()

def main():
    print()
    lang = input("1. Take single letter\n 2. Exit\n")
    match lang:
        case "1":
            vowel_or_cons()
        case "2":
            exit(0)

main()