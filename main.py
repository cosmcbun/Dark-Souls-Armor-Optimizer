import csv

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def bprint(message, end="\n"):
    print(color.YELLOW + message + color.END, end=end)

class Armor():
    def __init__(self, array):
        self.set = array[0]
        self.name = array[1]
        self.position = int(array[2])
        self.poise = float(array[3])
        self.weight = float(array[4])
        self.physical = float(array[5])
        self.magic = float(array[6])
        self.fire = float(array[7])
        self.lightning = float(array[8])
        self.bleed = float(array[9])
        self.poison = float(array[10])
        self.curse = float(array[11])
        self.stamina = int(array[12])
        self.url = array[13]
        self.location = array[14].replace("http://darksoulswiki.wikispaces.com/","").replace("+"," ").lower()
        self.data = [self.set, self.name, self.position, self.poise, self.weight, self.physical, self.magic, self.fire,
                     self.lightning, self.bleed, self.poison, self.curse, self.stamina, self.url, self.location]
        if self.weight == 0:
            self.defenseDensity = 0
        else:
            self.defenseDensity = self.physical / self.weight

    def __repr__(self):
        return self.name


allArmor = [[], [], [], []]

character = "randomizer"
if character == "old":
    placesIHaveBeen = ["oolacile", "valley of drakes", "darkroot basin","kiln of the first flame","new londo ruins","the duke%27s archives","tomb of giants","lost izalith","demon ruins","anor londo","blighttown", "undead parish","darkroot garden","depths","the catacombs","undead burg","sen%27s fortress","painted world of ariamis"]
    placesIHaventBeen = []
    setsIDontHave = ["Ornstein's Set"]
    piecesIDonthave = ["Xanthous Crown"]
    file = 'armor-stats.csv'
elif character == "new":
    placesIHaveBeen = ["undead parish", "undead burg", "sen%27s fortress", "darkroot basin", "painted world of ariamis",
                       "darkroot garden", "blighttown", "anor londo", "demon ruins", "tomb of giants",
                       "the catacombs", "valley of drakes", "new londo ruins", "the duke%27s archives"]
    placesIHaventBeen = ["oolacile", "kiln of the first flame", "lost izalith", "depths"]
    setsIDontHave = ["Iron and Sun Set", "Shadow Set", "Smough's Set"]
    piecesIDonthave = []
    file = 'armor-stats-2.csv'
elif character == "randomizer":
    setsIHave = ["Warrior Set", "Elite Knight Set", "Fang Boar Set", "Chain Set", "Stone Set", "Bandit Set", "Balder Set",
                 "Knight Set", "Wanderer Set", "Thief Set", "Sorcerer Set", "Crimson Set", "Antiquated Set", "Eastern Set",
                 "Gold-Hemmed Black Set", "Hollow Thief Set", "Balder Set", "Black Iron Set", "Dingy Set",
                 "Crystalline Set", "Gargoyle Set"]
    file = 'armor-stats-backup.csv'

with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        # print(' '.join(row).split(","))
        armor = Armor(' '.join(row).split(","))
        if armor.name == "Mask of the Child": maskOfTheChild = armor
        elif armor.name == "Sunlight Maggot": sunlightMaggot = armor
        elif armor.name == "Naked Head": nakedHead = armor
        elif armor.name == "Crown of Dusk": duskCrown = armor
        elif armor.name == "Crown of the Dark Sun": crownOfTheDarkSun = armor
        elif armor.name == "Symbol of Avarice": symbolOfAvarice = armor
        if character == "randomizer":
            if armor.set in setsIHave: allArmor[armor.position - 1].append(armor)
        else:
            if armor.location not in placesIHaventBeen and armor.set not in setsIDontHave and armor.name not in piecesIDonthave: allArmor[armor.position - 1].append(armor)


def suitUp(currentCarryingCapacity, weaponWeight, minPoise, statToMax, startingSet = [None,None,None,None], printHavel = False):
    lightBurden = currentCarryingCapacity / 4 - weaponWeight
    midBurden = currentCarryingCapacity / 2 - weaponWeight
    #heavyBurden = currentCarryingCapacity - weaponWeight
    suitUpHelper("For light rolls, try", lightBurden, minPoise, statToMax, startingSet[:])
    suitUpHelper("For mid rolls, try", midBurden, minPoise, statToMax, startingSet[:])

    if printHavel:
        lightBurden = currentCarryingCapacity * 1.5 / 4 - weaponWeight
        midBurden = currentCarryingCapacity * 1.5 / 2 - weaponWeight
        maxBurden = currentCarryingCapacity * 1.5 - weaponWeight
        suitUpHelper("For light Havel rolls, try", lightBurden, minPoise, statToMax, startingSet[:])
        suitUpHelper("For mid Havel rolls, try", midBurden, minPoise, statToMax, startingSet[:])
        suitUpHelper("For fat Havel rolls, try", maxBurden, minPoise, statToMax, startingSet[:])


def suitUpHelper(firstThingToPrint, burden, minPoise, statsToMax, startingSet, bonusPoise = 0):
    global numbersToDefTypes
    set = optimize(burden, minPoise, statsToMax, startingSet)
    if set:
        print(firstThingToPrint, set)
        print("weight:", calculateStatSum(set, 4), "| poise:", calculateStatSum(set, 3)+bonusPoise, end="")
        for stat in statsToMax:
            if stat != 3: print(" |", numbersToDefTypes[stat] + ":", calculateStatSum(set, stat), end="")
        print()
        print()

def optimize(burden, minPoise, statsToMax, armorWorn):
    global allArmor

    #print(burden, minPoise, statsToMax, armorWorn, calculateStatSum(armorWorn, 5))

    if calculateStatSum(armorWorn, 4) > burden:
        #print("too heavy")
        return
    elif None not in armorWorn:
        if calculateStatSum(armorWorn, 3) < minPoise:
            #print("not enough poise")
            return
        else:
            #print("possible good set")
            return armorWorn

    else:
        record = 0
        recordSet = [None,None,None,None]
        pieceToFind = armorWorn.index(None)
        #print("searching")
        for armor in allArmor[pieceToFind]:
            setToTest = armorWorn[:]
            setToTest[pieceToFind] = armor
            bestSet = optimize(burden, minPoise, statsToMax, setToTest)
            if bestSet:
                if evaluateSet(bestSet, statsToMax) > record:
                    #print("this new set,",bestSet,"was better: stats go from",record,"to",evaluateSet(bestSet, statsToMax))
                    record = evaluateSet(bestSet, statsToMax)
                    recordSet = bestSet[:]
        #print("the best set was:",recordSet)
        return None if recordSet == [None, None, None, None] else recordSet

def calculateStatSum(armorSet, statNo): return round(sum([armor.data[statNo] for armor in list(filter(None, armorSet))]),1)

def evaluateSet(armorSet, statsToMax): return sum([calculateStatSum(armorSet, stat) * statsToMax[stat] for stat in statsToMax])


numbersToDefTypes = {3: "poise", 5: "physical", 6: "magic", 7: "fire", 8: "lightning", 9: "bleed", 10: "poison", 11: "curse", 12: "stamina"}
poise = 3
physical = 5
magic = 6
fire = 7
lightning = 8
bleed = 9
poison = 10
curse = 11
stamina = 12

# max equip load, weapon weight, min_poise, and stats to prioritize with weights
if character == "randomizer":
    equipLoad = 90
    weaponWeight = 15.5
    defaultPrefs = {physical: 5, poise: 2, magic: 1, fire:1, lightning:1, stamina:10}
    bprint("0 poise:")
    suitUp(equipLoad, weaponWeight, 0, defaultPrefs, [None, None, None, None], False)
    bprint("32 poise:")
    suitUp(equipLoad, weaponWeight, 32, defaultPrefs, [None, None, None, None], False)
    bprint("46 poise (wolf ring):")
    suitUp(equipLoad, weaponWeight, 46-40, defaultPrefs, [None, None, None, None], False)
    bprint("53 poise (wolf ring):")
    suitUp(equipLoad, weaponWeight, 53-40, defaultPrefs, [None, None, None, None], False)
    bprint("61 poise (wolf ring):")
    suitUp(equipLoad, weaponWeight, 61 - 40, defaultPrefs, [None, None, None, None], False)

elif character == "new":
    #Good poises: 46 and 61. optimize once I know my weapon.
    equipLoad = 72
    weaponWeight = 3+2
    defaultPrefs = {physical: 3, poise: 2, stamina:2}
    bprint("MLGS sets:")
    suitUp(equipLoad, weaponWeight + 6, 0, defaultPrefs, [None, None, None, None], True)
    suitUp(equipLoad, weaponWeight + 6, 0, defaultPrefs, [duskCrown, None, None, None], False)
    suitUp(equipLoad, weaponWeight + 6, 0, defaultPrefs, [crownOfTheDarkSun, None, None, None], False)
    bprint("MLGS sets with 46 poise:")
    suitUp(equipLoad, weaponWeight + 6, 46, {physical: 1}, [duskCrown, None, None, None], False)
    suitUp(equipLoad, weaponWeight + 6, 46, {physical: 1}, [crownOfTheDarkSun, None, None, None], False)
    bprint("MLGS sets with 61 poise:")
    suitUp(equipLoad, weaponWeight + 6, 61, {physical: 1}, [duskCrown, None, None, None], False)
    suitUp(equipLoad, weaponWeight + 6, 61, {physical: 1}, [crownOfTheDarkSun, None, None, None], False)
    bprint("Estoc sets:")
    suitUp(equipLoad, weaponWeight + 2, 0, defaultPrefs, [duskCrown, None, None, None], False)
    suitUp(equipLoad, weaponWeight + 2, 0, defaultPrefs, [crownOfTheDarkSun, None, None, None], False)
    bprint("Fire sets:")
    suitUp(equipLoad, weaponWeight + 6, 0, {physical:3, stamina:3, fire:2}, [duskCrown, None, None, None], True)

elif character == "old":
    equipLoad = 120.6/1.5 #108.2 to wear giants+gwyndolin crown with havel's ring, 162.3 to wear without it, at an annoyingly high 51 endurance
    weaponWeight = 13.3+2
    defaultPrefs = {physical: 1, poise: 1, stamina: 2, curse: 0}
    bprint("Kalameet sets:")
    suitUp(equipLoad, weaponWeight, 0, {physical:2, stamina:4, magic:2})
    bprint("Normal sets:")
    suitUp(equipLoad, weaponWeight, 0, defaultPrefs)  # for 74 def and 22 poise
    bprint("Sunlight Maggot:")
    suitUp(equipLoad, weaponWeight, 0, defaultPrefs, [sunlightMaggot, None, None, None])
    bprint("Farming Sets:")
    suitUp(equipLoad, weaponWeight, 0, defaultPrefs, [symbolOfAvarice, None, None, None])
    bprint("Dusk Crown:")
    suitUp(equipLoad, weaponWeight, 0, defaultPrefs, [duskCrown, None, None, None])
    bprint("Crown of the Dark Sun:")
    suitUp(equipLoad, weaponWeight, 0, defaultPrefs, [crownOfTheDarkSun, None, None, None])
    #bprint("Dragon Head Stone:")
    #suitUp(equipLoad, weaponWeight, 0, defaultPrefs, [nakedHead, None, None, None])

"""for i in range (101):
    armorSet = optimize(i/2,0,{physical:1},[None,None,None,None])
    print(i/2," ",calculateStatSum(armorSet,physical))"""

# for armor in sorted(allArmor[0],key = lambda x: x.defenseDensity):
#     print (armor, armor.defenseDensity)
# print()
# for armor in sorted(allArmor[1],key = lambda x: x.defenseDensity):
#     print (armor, armor.defenseDensity)
# print()
# for armor in sorted(allArmor[2],key = lambda x: x.defenseDensity):
#     print (armor, armor.defenseDensity)
# print()
# for armor in sorted(allArmor[3],key = lambda x: x.defenseDensity):
#     print (armor, armor.defenseDensity)