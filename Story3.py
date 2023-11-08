from Getters import*

def Story3(debug = False):
    if debug: print("Story3 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    adj1 = getAdj("Enter a adjective:" , debug)
    place1 = getPlace("Enter a place:", debug)
    activity1 =getActivity("Enter a activity:", debug)
    animal1 = getAnimal ("Enter a animal:", debug)
    action1 = getAction ("Enter a action word: ", debug)

    out = "\n"
    
    out += " While I was on vacation in " + Country1
    out += " Me and my friend " + friendName1
    out += " went deep sea fishing and we caught a" + fish1
    out += ". We noticed it was very fat so we cut it open and found a " + animal1
    out += ". We were shocked and I ended upgetting sick so we went to the " + hotelname1
    out += ", while I was asleep my other friend " + friendName2
    out += ". So we decided " + verb1
    out += " was the best thing after being so tired, it ended up " + naturaldisaster1
    out += ". This day kept gettng worse and worse so we called it a night amd went to bed at" Time1
    return out
