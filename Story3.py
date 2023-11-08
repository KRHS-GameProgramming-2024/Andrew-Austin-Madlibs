from Getters import*

def Story3(debug = False):
    if debug: print("Story3 Function")

    print("\n")
    country1 = getWord("Enter a country: ", debug)
    friendName1 = getWord("Enter a name: ", debug)
    fish1 = getWord("Enter a fish: ", debug)
    animal1 = getAnimal ("Enter a animal: ", debug)
    hotelName1 = getWord("Enter a hotel name: ", debug)
    friendName2 = getWord("Enter another name: ", debug)
    adj1 = getAdj ("Enter a adjective: ", debug)
    naturalDisaster1 = getNaturalDisaster ("Enter a natural disaster: ", debug)
    time1 = getWord ("Enter a time: ", debug)

    out = "\n"
    out += " While I was on vacation in " + country1
    out += " Me and my friend " + friendName1
    out += " went deep sea fishing and we caught a " + fish1
    out += ". We noticed it was very fat so we cut it open and found a " + animal1
    out += ". We were shocked and I ended up getting sick so we went to the " + hotelName1
    out += ", while I was asleep my other friend " + friendName2
    out += " came over. We decided " + adj1
    out += " was the best thing after being so tired, it ended up " + naturalDisaster1
    out += ". This day kept gettng worse and worse so we called it a night amd went to bed at " +time1

    

    return out
