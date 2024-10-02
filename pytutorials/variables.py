#Strings, integers, floats, booleans


# Strings
first_name = "Anthony"
food = "pizza"
email = "anthonychappettocareers@gmail.com"
lego = "Republic Venator Attack Cruiser"

print(first_name) #prints variable first_name which is defined as "Anthony"

print(f"Hello {first_name}") #f string formats strings with variables easier
print(f"You like {food}")
print(f"Your email is {email}")

# Integers

age = 22
quantity = 3
num_of_students = 30

print(f"You are {age} years old buying {quantity} double chunk chocolate cookies at Costco")
print(f"Your class has {num_of_students} students")

# Floats

price = 649.99
gpa = 3.69
distance = 7.1

print(f"Your total is ${price} for the {lego}")
print(f"My high school gpa was {gpa}")
print(f"I ran {distance} miles with Jerik, Carlos, and Jake")  

# Booleans

is_student = False
for_sale = True

print(f"Are you a student?: {is_student}")

if for_sale:
    print("That car is for sale!")
else:
    print("That car is NOT for sale!")