# elevator similator
def hello():
    print ("Welcome to a Python training project, an elevator simulator. Please input the data as requested in the following prompts with raw integers. No letters, spaces, letters, just raw intergers.\n")
# query base floor
def fbase_floor():
    while True:
        try:
            base_floor = int(input("What is the lobby floor number?\n>"))
            break
        except:
            print("That is not a number. Try again.")
    return int(base_floor)


# query total floors
def ftotal_floors():
    while True:
        try:
            total_floors = int(input("How many floors does the building have?\n>"))
            break
        except:
            print("That is not a number. Try again.")
        return int(total_floors)

# query current floor
def fcurrent_floor():
    while True:
        try:
            current_floor = int(input("What floor are you currently on?\n>"))
            break
        except:
            print("That is not a number. Try again.")
    return current_floor

# query target floor
def ftarget_floor():
    while True:
        try:
            target_floor = int(input("Which floor would you like to go to?\n>"))
            break
        except:
            print("That is not a number. Try again")
    return target_floor


# calculates how many floors in between current and target floor regardless if positive or negative

#elevator_current_floor = base_floor

def fdifference(current_floor, target_floor):
    difference = current_floor - target_floor
    difference = abs(difference)
    return difference

#while target_floor <= total_floors: | TO DO
def print_result():
    if current_floor < target_floor:
        print("You will go up %s floors") % (difference)

    elif current_floor > target_floor:
        print("You will go down %s floors") % (difference)

    elif current_floor == target_floor:
        print("No need to take the elevator buddy")

    else:
        print("The elevator will kill you")

 # Runs the functions one by one, operating the simulation. Starting with the greetings and ending with the simulation results
hello()
total_floors = ftotal_floors()
current_floor = fcurrent_floor()
target_floor = ftarget_floor()
difference = fdifference(current_floor, target_floor)
print ("difference: %s, current_floor: %s, target_floor: %s") % (difference, current_floor, target_floor)
print_result()