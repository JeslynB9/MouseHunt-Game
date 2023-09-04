'''
Answer for Question 4 - The Training

Name: Jeslyn Joylie Bowman
SID: 530481526
unikey: jbow2146

'''

trap = ('High Strain Steel Trap', 'Hot Tub Trap', 'Cardboard and Hook Trap')

# Phase 1: Travvelling to the Meadow
def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")

def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    enter = input("Press Enter to travel to the Meadow...")
    if enter == "":
        print("Travelling to the Meadow...")
        print("Larry: This is your camp. Here you'll set up your mouse trap.")
        return enter
    else:
        return False

#Phase 2: Setting up a trap
def setup_trap(trap: tuple) -> bool:

    print("Larry: Let's get your first trap...")
    enter = input("Press Enter to view traps that Larry is holding...")
    if enter == "":
        print("Larry is holding...")
        print("Left: High Strain Steel Trap")
        print("Right: Hot Tub Trap")
    else:
        return False
    what_trap = input('Select a trap by typing "left" or "right": ').strip()
    if what_trap == 'left':
        print("Larry: Excellent choice.")
        print('Your "High Strain Steel Trap" is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        cheddar = True
        picked_trap_1 = trap[0]
        result = cheddar, picked_trap_1
        return (picked_trap_1, cheddar, "High Strain Steel Trap")
    elif what_trap == 'right':
        print("Larry: Excellent choice.")
        print('Your "Hot Tub Trap" is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        cheddar = True
        picked_trap_2 = trap[1]
        return (picked_trap_2, cheddar, "Hot Tub trap")
    else:
        print("Invalid command! No trap selected.")
        print("Larry: Odds are slim with no trap!")
        cheddar = False
        picked_trap_3 = trap[2]
        return (picked_trap_3, cheddar, "Cardboard and Hook Trap")

# Phase 3: Sound the horn
def basic_hunt(trap, cheddar):
    print("Sound the horn to call for the mouse...")
    horn = input('Sound the horn by typing "yes": ')
    if horn == 'yes' and cheddar:
        print("Caught a Brown mouse!")
        print("Congratulations. Ye have completed the training.")
        return True
    if horn != 'yes' and cheddar:
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!")
        return False
    if horn == 'yes' and not cheddar:
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!")
        return False
    elif horn != 'yes' and not cheddar:
        print("Nothing happens.")
        return False

def hunt_status(basic_hunt):
    status = basic_hunt(trap, cheddar)
    if status:
        return True
    else:
        return False

def end(status: bool):
    if status == True:
        print("Good luck~")
        return True
    elif status == False:
        return False

def main():
    intro()
    travel_to_camp()
    result = setup_trap(trap)
    hunt_result = basic_hunt(result[0], result[1])
    hunt_status = end(hunt_result)
    return result


if __name__ == '__main__':
    main()