#Unit Converter
#Concepts Covered: Data Types, Arithmetic Operators, Variables
#Description: Create a program that converts units between different measurement systems. 
#For example, convert between miles and kilometers, Fahrenheit and Celsius, or pounds and kilograms. 
#Allow the user to choose the type of conversion they want to perform.

def choice():
    try:        # Catches non int response
        function = int(input(("What would you like to convert?\n1. Distance\n2. Temperature\n3. Weight\n0. Exit\n"))) #Takes variable function as int to determine user choice on what to convetr
        if function == 1: # user input 1 is for distance
            print("\nTime to convert distance!")
            print("Miles to Kilometers or Kilometers to Miles?\n0 to go back")
            ans = int(input()) #takes choice for how user wants to convert miles and kilometers
            try:
                while ans != 0:
                    if ans == 1:
                        mtk()   #miles to kilometers
                    elif ans == 2:
                        ktm()   #kilometers to miles
                    elif ans == 0:
                        choice()
                print("keep going")
            except ValueError:
                print("Answer is not an integer number")    # error checking for non-int input
                exit(1) # exits program due to bad user input
        elif function == 2: # user input 2 for temperature
            print("\nTime to convert temperature!")
            print("Fahrenheit to Celsius or Celsius to Fahrenheit")
        elif function == 3: # user input 3 for weight
            print("\nTime to convert weight!")
            print("Pounds to Kilograms or Kilograms to Pounds?")
    except ValueError:
        print("Answer is not an integer number")    # error checking for non-int input
        exit(1) # exits program due to bad user input

def mtk():
    miles = float(input(("Enter how many miles you want to convert. (0 to go back)\n")))
    kilometers = (miles * 1.60934)   
    print(str(miles) + " miles in kilometers is " + str(kilometers))  
def ktm():
    print("hellow Wo")


choice()