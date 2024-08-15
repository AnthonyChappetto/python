#Unit Converter
#Concepts Covered: Data Types, Arithmetic Operators, Variables
#Description: Create a program that converts units between different measurement systems. 
#For example, convert between miles and kilometers, Fahrenheit and Celsius, or pounds and kilograms. 
#Allow the user to choose the type of conversion they want to perform.

function = int(input(("What would you like to convert?\n1. Distance\n2. Temperature\n3. Weight\n")))
if function == 1:
    print("\nTime to convert distance!")
    print("Miles to Kilometers or Kilometers to Miles?")
if function == 2:
    print("\nTime to convert temperature!")
    print("Fahrenheit to Celsius or Celsius to Fahrenheit")
if function == 3:
    print()

