import random

print("How many shiny pokemon do you want to hunt?")
try:
    shiny_num = int(input())
except ValueError:
    print("Not a valid number")
    exit(0)

total_encounters = 0

for i in range(shiny_num):
    shiny_value = random.randint(1, 8192)
    count = 0
    while True:
        encounter_value = random.randint(1,8192)
        count += 1
        if shiny_value == encounter_value:
            break
    print("Shiny pokemon found! It took " + str(count) + " encounters to find")
    total_encounters += count
avg = total_encounters / shiny_num
print("\nTotal shinies: " + str(shiny_num) + " and it took " + str(total_encounters) + " encounters to find them all!")
print("\nAverage Phase: " + str(avg))

# Add in what pokemon you find
# Add in shiny charm probability