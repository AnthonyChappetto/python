name = "Anther"
age = 22
gpa = 3.5
is_student = False

print(type(name)) #prints type of variable name
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa) #Truncates decimal from 3.5 to 3
print(gpa)

age = float(age) #Turns 22 to 22.0
print(age)

age = str(age) #Turns 22.0 to "22.0"
print(age) #Can be used in print statements, but f statements are preferred

name = bool(name) #Turns "Anther" to True
print(name) #If the string was empty it would be false