from Screens import *
from Getters import *
from Story1 import *
from Story2 import *

def Madlibs (debug = False):
    if debug: print("welcome to debug")
    
    print(TitleScreen(debug))
    input("Press enter to continue")
        
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
    
        if choice == "q":
            exit();
        elif choice == "1":
            print(Story1())
            print("\n")
            input("Press enter to continue")
    
    
Madlibs(True)
