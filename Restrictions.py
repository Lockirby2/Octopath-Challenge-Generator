import random
import Config
from RestrictionInterface import Restriction

class HelmetRestriction(Restriction):
    def __init__(self):
        self.initialize("Helmet", 2, 5.0, range(1, 6))
        
    def invoke(self):
        super().invoke()
        if self.invocations == 1:
            self.restrictedSlots = getSlots(2)
        
    def output(self):
        if self.invocations == 1:
            print("The characters in slots " + str(self.restrictedSlots[0]) + " and " + str(self.restrictedSlots[1]) + " may not wear any helmets.")
        elif self.invocations == 2:
            print("None of your characters can wear a helmet.")
            
class ShieldRestriction(Restriction):
    def __init__(self):
        self.initialize("Shield", 2, 5.0, range(1, 6))
        
    def invoke(self):
        super().invoke()
        if self.invocations == 1:
            self.restrictedSlots = getSlots(2)
        
    def output(self):
        if self.invocations == 1:
            print("The characters in slots " + str(self.restrictedSlots[0]) + " and " + str(self.restrictedSlots[1]) + " may not use any shields.")
        elif self.invocations == 2:
            print("None of your characters can use a shield.")
            
class ArmourRestriction(Restriction):
    def __init__(self):
        self.initialize("Armour", 4, 4.0, range(1, 6))
        self.restrictedSlots = []
        
    def invoke(self):
        super().invoke()
        self.restrictedSlots = getSlots(1, currentSlots=self.restrictedSlots)
        
    def output(self):
        if self.invocations == 1:
            print("The character in slot " + str(self.restrictedSlots[0]) + " may not wear any body armour.")
        elif self.invocations == 2:
            print("The characters in slots " + str(self.restrictedSlots[0]) + " and " + str(self.restrictedSlots[1]) + " may not wear any body armour.")
        elif self.invocations == 3:
            print("The characters in slots " + str(self.restrictedSlots[0]) + ", " + str(self.restrictedSlots[1]) + ", and " + str(self.restrictedSlots[2]) + " may not wear any body armour.")
        elif self.invocations == 4:
            print("None of your characters can wear any body armour.")
            
class EncounterRestriction(Restriction):
    def __init__(self):
        self.initialize("Encounter", 1, 0.5, range(1, 5))
        
    def conflicts(self, restrictions):
        if Config.cumulative: return True
        return super().conflicts(restrictions)
        
    def output(self):
        if self.invocations == 1:
            print("You may not fight any random encounters between now and the chapter's end.")
            
class MenuRestriction(Restriction):
    def __init__(self):
        self.initialize("Menu", 1, 2.0, range(1, 5))
        
    def output(self):
        if self.invocations == 1:
            print("You may not open the menu in any areas that contain monsters.")
            
class SummonRestriction(Restriction):
    def __init__(self):
        self.initialize("Summon", 1, 1.0, range(2, 6))
        
    def output(self):
        if self.invocations == 1:
            print("You may not summon NPCs in battle.")
            
class BoostRestriction(Restriction):
    def __init__(self):
        self.initialize("Boost", 4, 2.0, range(1, 6))
        self.restrictedSlots = []
        
    def invoke(self):
        super().invoke()
        self.restrictedSlots = getSlots(1, currentSlots=self.restrictedSlots)
        
    def output(self):
        if self.invocations == 1:
            print("The character in slot " + str(self.restrictedSlots[0]) + " may not boost.")
        elif self.invocations == 2:
            print("The characters in slots " + str(self.restrictedSlots[0]) + " and " + str(self.restrictedSlots[1]) + " may not boost.")
        elif self.invocations == 3:
            print("The characters in slots " + str(self.restrictedSlots[0]) + ", " + str(self.restrictedSlots[1]) + ", and " + str(self.restrictedSlots[2]) + " may not boost.")
        elif self.invocations == 4:
            print("None of your characters can boost.")
            
class CharacterRestriction(Restriction):
    def __init__(self):
        self.initialize("Character", 2, 5.0, range(2, 6))
        self.characters = ["Cyrus", "Tressa", "Olberic", "Primrose", "Tressa", "Alfyn", "Ophelia", "Therion"]
        self.restrictedCharacters = []
        
    def invoke(self):
        super().invoke()
        if self.invocations == 1:
            self.restrictedCharacters = random.sample(self.characters, k=2)
        
    def output(self):
        if self.invocations >= 1:
            print("The character in slot 3 must be " + self.restrictedCharacters[0] + " if they aren't in slot 1 or 2.")
        if self.invocations == 1:
            print("The character in slot 4 must be " + self.restrictedCharacters[1] + " if they aren't in slot 1 or 2.")
        elif self.invocations == 2:
            print("Slot 4 must be empty (your party should consist of three people).")
     
class AccessoryByCharacterSlotRestriction(Restriction):
    def __init__(self):
        self.initialize("AccessoryByCharacterSlot", 2, 5.0, range(1, 6), conflictsWith=["AccessoryByEquipmentSlot"])
        self.accessories = getAccessoryList()
        self.restrictedAccessories = []
        
    def invoke(self):
        super().invoke()
        if self.invocations == 1:
            self.restrictedSlots = getSlots(2)
        self.restrictedAccessories.append(random.choice(self.accessories))
        
    def output(self):
        if self.invocations >= 1:
            print("The characters in slots " + str(self.restrictedSlots[0]) + " and " + str(self.restrictedSlots[1]) + " may only wear accessories that " + self.restrictedAccessories[0] + ".")
        if self.invocations == 2:
            print("The other two characters may only wear accessories that " + self.restrictedAccessories[1] + ".")

class AccessoryByEquipmentSlotRestriction(Restriction):
    def __init__(self):
        self.initialize("AccessoryByEquipmentSlot", 2, 5.0, range(1, 6), conflictsWith=["AccessoryByCharacterSlot"])
        self.accessories = getAccessoryList()
        self.restrictedAccessories = []
        
    def invoke(self):
        super().invoke()
        self.restrictedAccessories.append(random.choice(self.accessories))
        
    def output(self): 
        if self.invocations >= 1:
            print("Each character may only wear accessories that " + self.restrictedAccessories[0] + " in their first accessory slot.")
        if self.invocations == 2:
            print("Each character may only wear accessories that " + self.restrictedAccessories[1] + " in their second accessory slot.")
                
class ItemRestriction(Restriction):
    def __init__(self):
        self.initialize("Item", 6, 5.0, range(1, 6))
        self.items = ["grapes", "plums", "pomegranates", "olives", "herbs", "soulstones"]
        self.restrictedItems = []
        
    def invoke(self):
        super().invoke()
        self.restrictedItems.append(random.choice(self.items))
        self.items.remove(self.restrictedItems[-1])
        
    def output(self):
        for item in self.restrictedItems:
            print("You may not use any " + item + " inside or outside of combat, even through Concoct.")
    
class EquipmentBySlotRestriction(Restriction):
    def __init__(self):
        self.initialize("EquipmentBySlot", 4, 5.0, range(1, 6), conflictsWith=["EquipmentByType"])
        self.equipmentTypes = getEquipmentList()
        self.restrictedTypes = []
        self.restrictedSlots = []
        
    def invoke(self):
        super().invoke()
        self.restrictedSlots = getSlots(1, currentSlots=self.restrictedSlots, sort=False)
        self.restrictedTypes.append(random.choice(self.equipmentTypes))
        
    def output(self):
        restrictions = list(map(lambda x, y: (x, y), self.restrictedSlots, self.restrictedTypes))
        for restriction in restrictions:
            print("The character in slot " + str(restriction[0]) + " may only use shields, helmets, or armour that " + restriction[1] + ".")
    
class EquipmentByTypeRestriction(Restriction):
    def __init__(self):
        self.initialize("EquipmentByType", 2, 5.0, range(1, 6), conflictsWith=["EquipmentBySlot"])
        self.equipmentTypes = getEquipmentList()
        self.restrictedTypes = []
        
    def invoke(self):
        super().invoke()
        self.restrictedTypes.append(random.choice(self.equipmentTypes))
        self.equipmentTypes.remove(self.restrictedTypes[-1])
        
    def output(self):
        for restrictedType in self.restrictedTypes:
            print("No character can use shields, helmets, or armour that " + restrictedType + ".")
            
class SkillByTypeRestriction(Restriction):
    def __init__(self):
        self.initialize("SkillByType", 4, 4.0, range(1, 6), conflictsWith=["SkillBySlot"])
        self.skills = getSkillList()
        self.restrictedSkills = []
        self.unrestrictedSlots = []
        
    def invoke(self):
        super().invoke()
        self.unrestrictedSlot = getSlots(1, unfilledSlots=True, sort=False)
        self.unrestrictedSlots.extend(self.unrestrictedSlot)
        self.restrictedSkills.append(random.choice(self.skills))
        self.skills.remove(self.restrictedSkills[-1])
        
    def output(self):
        restrictions = list(map(lambda x, y: (x, y), self.unrestrictedSlots, self.restrictedSkills)) 
        for restriction in restrictions:
            print("No character can " + restriction[1] + ", except the character in slot " + str(restriction[0]) + ".")
            
class SkillBySlotRestriction(Restriction):
    def __init__(self):
        self.initialize("SkillBySlot", 4, 4.0, range(1, 6), conflictsWith=["SkillByType"])
        self.skills = getSkillList()
        self.restrictedSkills = []
        self.restrictedSlots = []
        
    def invoke(self):
        super().invoke()
        self.restrictedSlots = getSlots(1, currentSlots=self.restrictedSlots, sort=False)
        self.restrictedSkills.append(random.choice(self.skills))
        
    def output(self):
        restrictions = list(map(lambda x, y: (x, y), self.restrictedSlots, self.restrictedSkills))
        for restriction in restrictions:
            print("The character in slot " + str(restriction[0]) + " can only " + restriction[1] + " (items are still allowed).")
            
class PassiveSkillRestriction(Restriction):
    def __init__(self):
        self.initialize("PassiveSkill", 2, 5.0, range(2, 6))
        self.jobs = getJobList()
        self.numRestrictions = 3
        if Config.chapter == 5:
            self.numRestrictions = 4
        self.restrictedJobs = []
        
    def invoke(self):
        super().invoke()
        newJobRestrictions = random.sample(self.jobs, k=self.numRestrictions)
        self.restrictedJobs.extend(newJobRestrictions)
        self.jobs = list(set(self.jobs) - set(newJobRestrictions))
        
    def output(self):
        if self.invocations >= 1:
            print("No character is allowed to use passive skills from any of the following secondary jobs: " + str(self.restrictedJobs))
        
class JobBySlotRestriction(Restriction):
    def __init__(self):
        self.initialize("JobBySlot", 2, 5.0, range(2, 6), conflictsWith=["JobByJob"])
        self.jobs = getJobList()
        self.restrictedSlots = []
        self.restrictedJobs = []
        
    def invoke(self):
        super().invoke()
        newJobRestrictions = random.sample(self.jobs, k=2)
        self.restrictedJobs.extend(newJobRestrictions)
        self.jobs = list(set(self.jobs) - set(newJobRestrictions))
        self.restrictedSlots = getSlots(2, currentSlots=self.restrictedSlots, sort=False)
        
    def output(self):
        restrictions = list(map(lambda x, y: (x, y), self.restrictedSlots, self.restrictedJobs))
        for restriction in restrictions:
            print("The character in slot " + str(restriction[0]) + " may only use " + restriction[1] + " as their secondary job.")
            
class JobByJobRestriction(Restriction):
    def __init__(self):
        self.initialize("JobByJob", 2, 5.0, range(2, 6), conflictsWith=["JobBySlot"])
        self.jobs = getJobList()
        self.numRestrictions = 3
        if Config.chapter >= 5:
            self.numRestrictions = 4
        self.restrictedJobs = []
        
    def invoke(self):
        super().invoke()
        newJobRestrictions = random.sample(self.jobs, k=self.numRestrictions)
        self.restrictedJobs.extend(newJobRestrictions)
        self.jobs = list(set(self.jobs) - set(newJobRestrictions))
        
    def output(self):
        if self.invocations >= 1:
            print("No character is allowed to use any of the following secondary jobs: " + str(self.restrictedJobs))
            
class WeaponRestriction(Restriction):
    def __init__(self):
        self.initialize("Weapon", 6, 5.0, range(2, 6))
        self.weapons = ["swords", "spears", "daggers", "bows", "axes", "staves"]
        self.restrictedWeapons = []
        
    def invoke(self):
        super().invoke()
        self.restrictedWeapons.append(random.choice(self.weapons))
        self.weapons.remove(self.restrictedWeapons[-1])
        
    def output(self):
        for weapon in self.restrictedWeapons:
            print("No characters are allowed to equip any " + weapon + ".")

# Gets the number of slots specified by numberNeeded and appends them to currentSlots
# The first slot can be chosen from either the filled slots or the unfilled slots
# Used to guarantee that at least one relevant slot is affected
def getSlots(numberNeeded, currentSlots=[], unfilledSlots=False, sort=True):
    if currentSlots:
        potentialSlots = list(set(range(1, 5)) - set(currentSlots))
        currentSlots.extend(random.sample(potentialSlots, k=numberNeeded))
        if sort: currentSlots.sort()
        return currentSlots

    slots = []
    mandatorySlotChoices = getFilledSlots()
    if unfilledSlots and mandatorySlotChoices != range(1, 5):
        mandatorySlotChoices = list(set(range(1, 5)) - set(getFilledSlots()))
    slots.append(random.choice(mandatorySlotChoices))
    
    potentialSlots = list(range(1, 5))
    potentialSlots.remove(slots[-1])
    slots.extend(random.sample(potentialSlots, k=numberNeeded-1))
    if sort: slots.sort()
    return slots
    
# Helper function to get the list of slots that characters are currently in (based on the chapter)
def getFilledSlots():
    if Config.chapter != 1 or Config.completed > 2: return range(1, 5)
    if Config.completed == 2: return range(1, 4)
    if Config.completed == 1: return range(1, 3)
    return [1]
    
# Helper function to get the list of skills
def getSkillList():
    useSkillsThat = "use skills (including Beast Lore) that "
    return [
        useSkillsThat + "heal HP, SP, or BP",
        useSkillsThat + "deal elemental damage",
        useSkillsThat + "deal physical damage",
        useSkillsThat + "inflict debuffs or negative status ailments",
        useSkillsThat + "apply buffs or positive status ailments",
        useSkillsThat + "hit all enemies",
        useSkillsThat + "hit multiple times",
        useSkillsThat + "hit only one enemy",
        "use regular attacks",
        "defend"
    ]
  
# Helper function to get the list of accessory types  
def getAccessoryList():
    return [
        "boost HP",
        "boost SP",
        "boost physical or elemental attack",
        "boost physical or elemental defense",
        "boost speed",
        "boost critical",
        "boost accuracy",
        "boost evasion",
        "protect from status ailments",
        "protect from elements"
    ]
    
# Helper function to get the list of equipment types
def getEquipmentList():
    return [
        "boost evasion",
        "do NOT boost elemental defense",
        "boost physical AND elemental defense, but no other stats",
        "boost SP or elemental attack"
    ]
    
# Helper function to get the list of jobs depending on what chapter is being played
def getJobList():
    jobs = [
        "scholar",
        "cleric",
        "warrior",
        "dancer",
        "thief",
        "apothecary",
        "merchant",
        "hunter"
    ]
    lateJobs = [
        "runelord",
        "warmaster",
        "sorceror",
        "starseer"
    ]
    if Config.chapter >= 5:
        jobs.extend(lateJobs)
    return jobs
    