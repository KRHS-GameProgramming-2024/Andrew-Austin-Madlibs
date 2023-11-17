from Getters import*

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    object1 = getWord("Enter a object: ", debug)
    place1 = getWord("Enter a place: ", debug)
    crime1 = getWord("Enter a crime: ", debug)
    celebrity1 = getWord("Enter a celebrity: ", debug)
    object2 = getWord("Enter a different object: ", debug)
    sound1 = getWord("Enter a sound: ", debug)
    animal1 = getWord ("Enter a animal: ", debug)
    adj1 = getWord ("Enter a adjective: ", debug)

    out = "\n"
    out += "I found a " + object1
    out += ", inside a " + place1
    out += " this seemed to be used for a " + crime1
    out += ". Once I left, I saw " + celebrity1
    out += " standing in the dark corner of the " + place1
    out += ". I was scared so I ran for my life, I tripped on a " + object2
    out += ". My knees were all bloody, I heard footsteps that sounded like " + sound1
    out += ", I was terrified so I turned around and noticed a " + animal1
    out += ". It turned out he was super " +adj1
    return out
