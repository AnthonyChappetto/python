def addition():                     #Function handles addition
    yes = True
    print("Enter a number: ")
    num1 = int(input())             #Takes input only as number
    print("Enter a second number: ")
    num2 = int(input())
    result = num1 + num2            #Adds 2 nums
    print("The result is", result)  #prints result
    while yes == True:              #While user wants to add more numbers
        print("Keep going? Y/N")    #Prompt
        keepgoing = input()         
        if keepgoing == "y" or keepgoing == "Y":    #handles y or Y for yes
            print("Enter another number: ")
            num3 = int(input())
            result = result + num3                  #Adds more nums to result
            print("The result is", result)
        elif keepgoing == "n" or keepgoing == 'N':  #handles n or N for no
            yes == False                            #if user is done the loop exits and result is returned
            print("Your final result is:", result)
            return result
        else:
            print("Incorrect format. Use y/Y for yes or n/N for no")    #handles input that isn't correct y/n notation

def subtraction():
    print("Not started yet")
def multiplication():
    print("Not started yet")
def division(): 
    print("Not started yet")


print("What arithmatic function do you want to do?\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
choice = input()
if choice == "1":
    addition()
elif choice == "2":
    subtraction()
elif choice == "3":
    multiplication()
elif choice == "4":
    division()
else:
    print("Not a valid response")
    exit(1)