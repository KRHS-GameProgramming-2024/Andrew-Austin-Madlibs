from Getters import*

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    adj1 = getAdj(" Enter a adj:" , debug)
    place1 = getPlace(" Enter a place:", debug)
    activity1 =getActivity(" Enter a activity:", debug)

    out = "\n"
    out += "One day me and my friend " + friendName1
    out += " were out playing " + sport1
    out += "and he was " + adj1, ". "
    out += "After, we went to, " + place1
    out += "and we" + activity1, ". "

    
    return out

