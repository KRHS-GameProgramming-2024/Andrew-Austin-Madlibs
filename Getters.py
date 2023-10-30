def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("Please select an option: ")
        option = option.lower()
        if debug: print(option)
        if (option == "q" or 
            option == "quit" or
            option == "x" or
            option == "exit"):
                option = "q"
                goodInput = True
            
        elif (option == "1" or 
            option == "one" or
            option == "story 1" or
            option == "story1"):
                option = "1"
                goodInput = True
            
        else:
            print("Please make a valid choice")
        
    return option

def getWord(prompt, debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
            
    return word

def getSport(prompt, debug = False):
    if debug: print("getSport Function")
    
    goodInput = False
    
    sports = ["soccer", 
    "football", 
    "basketball", 
    "hockey", 
    "golf",
    "wrestling",
    "rugby",
    "horeback",
    "fencing",
    "field hockey",
    "bass fishing",
    "track",
    "cross country",
    "volleyball",
    "skiing",
    "snowboard",
    "ski",
    "swimming",
    "gymnastics",
    "bowling",
    "baseball"
    "lacrosse",
    "tennis",
    "cricket",
    "badmiton"]
    
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in sports:
            goodInput = False
            print("Sorry, I don't know that one")
            
            
    return word

def isSwear(word, debug = False):
    if debug: print("isSwear Fucntion")
    if word.lower() in swearList:
        return True
    else:
        return False

     
swearList = ["poop",
"pee",
"shit",
"piss",
"pee",
"dumbass",
"kike",
"ass",
"fuck",
"nigga",
"nigger",
"bitch",
"fag",
"gay",
"cock",
"dick",
"penis",
"retard",
"moron",
"idiot",
"pussy",
"wanker",
"cunt",
"clit",
"bastard",
"whore" ]

def getAdj(prompt, debug = False):
    if debug: print("getAdj Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
            
    return word

def getPlace(prompt, debug = False):
    if debug: print("getPlace Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
            
    return word
    
    def getPlace(prompt, debug = False):
    if debug: print("getPlace Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
            
    return word
