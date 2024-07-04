import os
import random



# Returns if you are dead or not (Dead = True; Alive = False)
def russianRoulette():
    # Creates a new list of chambers (6 chambers, 1 bullet)
    chambers = [0, 0, 0, 0, 0, 1]
    
    # Shuffles the chambers randomly
    random.shuffle(chambers)
    
    # Pull the trigger 🔫🤠
    input("Press Enter to pull the trigger...")

    # Gets the value in the last chamber and checks if it has a bullet in it
    if chambers.pop() == 1:
        #rip
        print("💥 BANG! You're dead. Game over. (×_×;）")
        return True
    else:
        print("Click! You survived. Keep playing! ( -_•)︻デ═一")
        return False

def main():
    # Clears the terminal(for most of the os)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Welcome
    print("Welcome to Ziki's Russian Roulette! /̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿ (X__X)")
    # Makes the game run "forever" 
    while True:
        play_again = input("Do you want to play? (yes/no): ").lower()
        if play_again != "yes":
            print("(ㅍ_ㅍ)")
            break
        
        # Checks if you're dead. While playing the game (running the function)
        if(russianRoulette()):
            break


main()