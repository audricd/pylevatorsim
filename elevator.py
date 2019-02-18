import sys
import os
import platform

 # elevator similator

 # meant to be running on python 3.5 or 3.6 (both should work)

def pyvercheck():
    detectedos = "%s %s" % (platform.system(), platform.release())
    version = sys.version_info[:2]
    strversionM = str(version[0])
    strversionm = str(version[1])
    strversion = ("%s.%s" % (strversionM, strversionm))
    if version == (3, 5) or (3, 6):
        print ("You are using the ideal Python %s (running on %s), for this program." % (strversion, detectedos))
    elif version < (3, 5):
        print ("You are using version of Python %s which is below 3.5 (running on %s), the intented version. The program will now exit." % (strversion, detectedos))
        sys.exit()
    elif version > (3, 6):
        print ("You are using version of Python %s which is above 3.6 (running on %s), the intented version. The program will now exit." % (strversion, detectedos))
        sys.exit()
    else:
        sys.exit("Unrecognized Python version (%s) on %s" % (strversion, detectedos))

 # hello function. basic information about the program itself and myself
def hello():
    version = ("0.4")
    github = ("https://github.com/audricd/pylevatorsim")
    print ("=" * 100)
    print ("Welcome to a Python training project, an elevator simulator. Please input the data as requested in \nthe following prompts with raw integers. No letters, spaces, symbols, just raw intergers.")
    print ("=" * 100)
    print ("This is version %s of the training program. All info can be found at \n%s" % (version, github))
    print ("=" * 100)
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

# query target floor and checks if it is not above the roof!
def ftarget_floor():
    while True:
        try:
            target_floor = int(input("Which floor would you like to go to?\n>"))
            while target_floor > total_floors:
                print("That is impossible, it is above the roof!")
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

 # print results if all data is good, with all possible outcomes
def print_result():
    if current_floor < target_floor:
        print("You will go up %s floors" % (difference))

    elif current_floor > target_floor:
        print("You will go down %s floors" % (difference))

    elif current_floor == target_floor:
        print("No need to take the elevator buddy")

    else:
        print("The elevator will kill you")
 # Runs the functions one by one, operating the simulation. Starting with the greetings and ending with the simulation results

pyvercheck()
hello()
total_floors = ftotal_floors()
current_floor = fcurrent_floor()
target_floor = ftarget_floor()
difference = fdifference(current_floor, target_floor)
#print ("difference: %s, current_floor: %s, target_floor: %s") % (difference, current_floor, target_floor)
print_result()