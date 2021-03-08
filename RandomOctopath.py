import sys
import random
import Config
from Restrictions import *

def main():
    Config.chapter = int(input("What chapter are you about to play? Enter 5 if you are about to fight Galdera: "))
    if Config.chapter < 5:
        Config.completed = int(input("How many characters have you completed this chapter with? Enter a number between 0 and 7: "))
    else: Config.completed = 0
    
    restrictionsByCompletion = [
        [1, 2, 3, 4, 6, 7, 8, 10],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [3, 3, 4, 4, 5, 5, 6, 6],
        [1, 2, 4, 5, 6, 7, 9, 10],
        [1]
    ]

    if Config.chapter == 1 and Config.completed == 0:
        printSeparator()
        print("Hello, and welcome to the Octopath Traveler challenge randomizer! The idea is that every time you complete a chapter for a character, you run the randomizer again to generate a new set of restrictions.  The randomizer is designed to give more restrictions at the less difficult parts of the game to ensure that it is always a challenge.")
        print("")
        print("This is designed with the idea that you will complete chapter 1 for every character, then chapter 2, etc. The run ends when you defeat Galdera. If you do things out of order, you might need to make up rulings on the fly to account for that. If you think there's a grey area in a restriction, I encourage you to just decide what is interesting for you and roll with it.")
        print("")
        print("Many restrictions refer to \"slots\". The character in \"slot 1\" is always your main character if they're in your party.  The character in \"slot 2\" is always the character whose chapter you are going to complete next (unless they're your main character, of course).  Otherwise, you can pick any character for any slot.")
        print("")
        print("The restrictions before the all-caps message below are meant to apply to the entire game. If you don't like one of these game-wide rules (e.g., you want to play with a specific main character or don't like skipping treasure/sidequests), just ignore it!")
        print("")
        print("Take a look at Config.py for a couple of extra options.")
        printCharacter()
        printOptionalLocationRestrictions()
        printChestRestrictions()
        printPathActionRestrictions()
        printSeparator()
        print("END OF RESTRICTIONS THAT APPLY TO THE ENTIRE PLAYTHROUGH")
        printSeparator()

    if Config.chapter == 5:
        printSeparator()
        print("Each of the following two restrictions applies to one of the parties that you will bring to the final encounter. You can choose which restriction applies to which party. The restrictions don't apply until the fight with Galdera. Good luck!")
    
    printSeparator()
    
    # Generate a new seed before adding values because there are otherwise some cases where the player could end up with similar lists of restrictions to previous playthroughs if they use similar restriction names
    random.seed(Config.seed)
    unpredicatableSeed = random.randrange(sys.maxsize)
    
    # Determine the correct seed and seed the RNG
    unpredicatableSeed = unpredicatableSeed + (10 * Config.chapter)
    if not Config.cumulative:
        unpredicatableSeed += Config.completed
    random.seed(unpredicatableSeed)
    
    # Apply all restrictions
    restrictions = generateRestrictions(restrictionsByCompletion[Config.chapter - 1][Config.completed])
    printRestrictions(restrictions)
    
    if Config.chapter == 5:
        restrictions = generateRestrictions(restrictionsByCompletion[Config.chapter - 1][Config.completed])
        printRestrictions(restrictions)
        
    printSeparator()
        
def generateRestrictions(restrictionCount):
    restrictions = [HelmetRestriction(), ShieldRestriction(), ArmourRestriction(), EncounterRestriction(), MenuRestriction(), SummonRestriction(), BoostRestriction(), CharacterRestriction(), AccessoryByCharacterSlotRestriction(), AccessoryByEquipmentSlotRestriction(), ItemRestriction(), EquipmentBySlotRestriction(), EquipmentByTypeRestriction(), SkillByTypeRestriction(), SkillBySlotRestriction(), PassiveSkillRestriction(), JobBySlotRestriction(), JobByJobRestriction(), WeaponRestriction()]
    conflictingRestrictions = []
    
    for i in range(0, restrictionCount): 
        restriction = chooseByWeight(restrictions)
        
        while restrictions and restriction.conflicts(restrictions + conflictingRestrictions):
            restrictions.remove(restriction)
            conflictingRestrictions.append(restriction)
            if not restrictions:
                return conflictingRestrictions
            restriction = chooseByWeight(restrictions)
            
        restriction.invoke()
        
    restrictions.extend(conflictingRestrictions)
    return restrictions;
    
def printRestrictions(restrictions):
    for restriction in restrictions:
        restriction.output()
        
def printSeparator():
    print("")
    print("***************************************")
    print("")
    
def chooseByWeight(restrictions):
    weights = map(lambda restriction: restriction.weight, restrictions)
    return random.choices(restrictions, weights=weights, k=1)[0]

def printCharacter():
    characters = ["Cyrus", "Tressa", "Olberic", "Primrose", "Tressa", "Alfyn", "Ophelia", "Therion"]
    printSeparator()
    print("Your main character is " + random.choice(characters) + ".")

def printOptionalLocationRestrictions():
    optionalLocations = ["The Whistlewood", "Untouched Sanctum", "Path of Beasts", "Whistling Cavern", "Twin Falls", "Carrion Caves", "Hoarfrost Grotto", "The Hollow Throne", "Tomb of Kings", "Farshore", "Derelict Mine", "Tomb of the Imperator", "Captains' Bane", "Quicksand Caves", "Maw of the Ice Dragon", "Undertow Cove", "Moldering Ruins", "Forest of No Return", "Marsalim Catacombs", "Refuge Ruins", "Dragonsong Fane", "Loch of the Lost King", "Everhold Tunnels", "Forest of Purgation"]
    
    restrictedLocationsCount = random.randrange(3, 7)
    restrictedLocations = random.sample(optionalLocations, k=restrictedLocationsCount)
    
    printSeparator()
    print("You may not set foot into any of the following optional locations:")
    for location in restrictedLocations:
        print(location)
        
def printChestRestrictions():
    mandatoryLocations = ["Cave of Origin", "Subterranean Study", "Caves of Maiya", "Brigands' Den", "Sunshade Catacombs", "Cave of Rhiyo", "Ravus Manor", "The Whisperwood", "Morlock's Manse", "Secret Path", "Orlick's Manse", "The Murkwood", "The Sewers", "Caves of Azure", "The Spectrewood", "Arena", "Lizardman's Den", "Rivira Woods", "The Forgotten Grotto", "Black Market", "The Whitewood", "Seaside Grotto", "Obsidian Manse", "Yvon's Birthplace", "Ebony Grotto", "Ruins of Eld", "Grandport Sewers", "Lord's Manse", "Amphitheatre", "Forest of Rubeh", "Lorn Cathedral", "Grimsand Ruins"]
    
    restrictedLocationsCount = random.randrange(3, 7)
    restrictedLocations = random.sample(mandatoryLocations, k=restrictedLocationsCount)
    
    printSeparator()
    print("You may not collect any treasure chests in the following locations:")
    for location in restrictedLocations:
        print(location)
        
def printPathActionRestrictions():
    towns = ["Flamesgrace", "Atlasdam", "Rippletide", "Cobbleston", "Sunshade", "Clearbrook", "Bolderfall", "S'warkii", "Quarrycrest", "Stillsnow", "Noblecourt", "Saintsbridge", "Goldshore", "Stonegard", "Victors Hollow", "Wellspring", "Wispermill", "Duskbarrow", "Grandport", "Riverford", "Everhold", "Orewell", "Northreach", "Marsalim"]
    singleActions = ["Steal", "Purchase", "Scrutinize", "Inquire", "Challenge", "Provoke", "Guide", "Allure", "All"]
    actionPairs = [("Steal", "Purchase"), ("Scrutinize", "Inquire"), ("Challenge", "Provoke"), ("Guide", "Allure")]
    
    actionRestrictions = {}
    for town in towns:
        actionRestrictions[town] = set()
        
    for action in singleActions:
        actionRestrictions[random.choice(towns)].add(action)
        actionRestrictions[random.choice(towns)].add(action)
            
    for actionPair in actionPairs:
        restrictedTown = random.choice(towns)
        actionRestrictions[restrictedTown].add(actionPair[0])
        actionRestrictions[restrictedTown].add(actionPair[1])
    
    printSeparator()
    print("In the following towns, the listed path actions cannot be used (unless needed to complete a character's storyline or unlock Galdera):")
    for restriction in actionRestrictions:
        if actionRestrictions[restriction]:
            print(restriction + ": " + str(actionRestrictions[restriction]))
    
if __name__ == "__main__":
    main()