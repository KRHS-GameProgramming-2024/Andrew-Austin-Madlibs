from Getters import*

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    adj1 = getWord("Enter a adjective:" , debug)
    place1 = getWord("Enter a place:", debug)
    activity1 =getWord("Enter a activity:", debug)
    animal1 = getWord ("Enter a animal:", debug)
    action1 = getWord ("Enter a action word: ", debug)

    out = "\n"
    out += "One day me and my friend " + friendName1
    out += " were out playing " + sport1
    out += " and he was " + adj1
    out += ". After, we went to the " + place1
    out += " and we were " + activity1
    out += ". While this was going on my friend " + friendName1 
    out += " noticed a giant " + animal1
    out += " and it " + action1
    out += " us."
    return out

