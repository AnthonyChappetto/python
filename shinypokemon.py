import random

#Represents Sinnoh region and all its routes
class Sinnoh:
    @staticmethod
    def route201():
        pokemonFound = random.randint(0,10) #Randomly generates num 1-10 and stores in pokemonFound
        if pokemonFound in [0, 1, 2, 3]: #Simulates Starly being 40% chance of finding in the wild
            shiny = "Starly"
        elif pokemonFound in [4, 5, 6, 7]:
            shiny = "Bidoof"
        else:
            shiny = "Kricketot"
        return shiny
    @staticmethod
    def route202():
        pokemonFound = random.randint(0,10)
        if pokemonFound in [0, 1]:
            shiny = "Starly"
        elif pokemonFound in [2, 3, 4, 5, 6,]:
            shiny = "Bidoof"
        else:
            shiny = "Shinx"
        return shiny
    def route203():
        return
    def route204():
        return
    def route205():
        return
    def route206():
        return
    def route207():
        return
    def route208():
        return
    def route209():
        return
    def route210():
        return
    def route211():
        return
    def route212():
        return
    def route213():
        return

            
def main():
    #Prompts user to choose a route
    print("Choose a route: \n201\n202")
    try:
        #Takes user input as an int
        route_choice = int(input())   
    except ValueError:
        #Error handling if char is entered as input instead of number
        print("Not a valid number")
        exit(0)

    #Assigns corresponding method based on user choice
    if route_choice == 201:
        route = Sinnoh.route201
    elif route_choice == 202:
        route = Sinnoh.route202
    else:
        print("Invalid route selected")
        exit(1)
    
    #Askes how many should be hunted
    print("How many shiny pokemon do you want to hunt?")
    try:
        shiny_num = int(input())
    except ValueError:
        print("Not a valid number")
        exit(0)

    #Holds total encounters during the hunts
    total_encounters = 0
    #List to hold the shinys caught
    shinies_found = []

    #Loops through shiny num, amount of shinys that are going to be hunted
    for i in range(shiny_num): 
        #Shiny value represents the value of the shiny pokemon, ie the number that needs to be hit to gaureentee a shiny
        shiny_value = random.randint(1, 8192)
        count = 0
        #Loops until shiny is found, ie encounter value being equal to shiny value
        while True:
            encounter_value = random.randint(1,8192) #generates shiny values, simulating encounteres in the wild
            count += 1  #increments number of shinies
            if shiny_value == encounter_value:
                #Calls route to determine which pokemon was found when shiny value is hit
                shiny = route()
                shinies_found.append(shiny) #Apends shiny to the list
                break
        print("Shiny " + shiny + " found! It took " + str(count) + " encounters to find")
        total_encounters += count #Tallies up total encounters
    avg = total_encounters / shiny_num #Calculates average per phase
    print("\nTotal shinies: " + str(shiny_num) + " and it took " + str(total_encounters) + " encounters to find them all!")
    print("\nAverage Phase: " + str(avg))
    print(f"The shiny found were: {', '.join(shinies_found)}")

#Entry point
if __name__ == "__main__":
    main()

# To do list:

# add in more routes from sinnoh
# Add in shiny charm probability
# Add in other region compatibility
# Add in day night cycle odds based on computer time
# Add in individual randomly generated stats for each shiny
# Organize these shinies by most appeal in their stats