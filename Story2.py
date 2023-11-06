from Getters import*

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
     = getWord("Enter a game: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    adj1 = getAdj("Enter a adjective:" , debug)
    place1 = getPlace("Enter a place:", debug)
    activity1 =getActivity("Enter a activity:", debug)
    animal1 = getAnimal ("Enter a animal:", debug)
    action1 = getAction ("Enter a action word: ", debug)

    out = "\n"
    out += "I found a " + object1
    out += ", inside a " + place1
    out += " this seemed to be used for a " + crime1
    out += ". Once I left, I saw a" + celberity1
    out += " standing in the dark corner of the " + place1
    out += ". I was scared so I ran for my life, I tripped on a " + object2
    out += ". My knees were all bloody, I heard footsteps that sounded like " + sound1
    out += ", I was terrified so I turned around and noticed  " + action1
    out += " us."
    return out
