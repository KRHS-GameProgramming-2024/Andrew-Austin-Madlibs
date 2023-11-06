from Getters import*

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    object1 = getObject("Enter a object: ", debug)
    place1 = getPlace("Enter a place: ", debug)
    crime1 = getCrime("Enter a crime: ", debug)
    celebrity1 = getCelebrity("enter a celebrity: ", debug)
    object2 = getObject("Enter a different object: ", debug)
    sound1 = getSound("Enter a sound: ", debug)
    animal1 = getAnimal("Enter a animal: ", debug)
    adjective1 = getAdjective("enter a adjective: ", debug)

    return out
