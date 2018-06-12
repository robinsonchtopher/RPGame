import xml.etree.ElementTree as ET
import random
import msvcrt  # this is for waiting


class PC:

    def __init__(self, name, alter):
        #player should have the following stats:
        #name, class str, dex, con, int, wis, cha, skills, exp, Lvl, Hp. initiative?
        self.stats = {}
        self.skills = {}
        self.stats['Name'] = name
        self.stats['Class'] = alter
        self.stats['Lvl'] = 1
        self.stats['Exp'] = 0
        self.fill_Stats()
        self.stats['MaxHp'] = self.stats['Con']
        print("We will now decide how much health you will start with ... ")
        self.Hp_Up()
        self.stats['MyHp'] = self.stats['MaxHp']#set current hp
        print("These are your stats ...")
        print(self.stats)

    def Hp_Up(self):
        #if self.stats['Lvl'] > 1:
        improvement = dX(self.stats['Con'])
        if improvement < (self.stats['Con'] / 2):
            print("We will improve that to half of the max.")
            improvement = (self.stats['Con'] / 2)
        self.stats['MaxHp'] += int(improvement)



    def fill_Stats(self):
        # right now is using the dictionary
        #print(self.stats)
        doctitle = self.stats['Class'] + str(self.stats['Lvl']) + '.xml'
        #print (doctitle)
        print ('You now have chosen your path ... {alter}'.format(alter = self.stats['Class']))
        tree = ET.parse(doctitle)
        root = tree.getroot()
        #print(self.stats)

        tree = ET.parse('Saber1.xml')
        root = tree.getroot()


        # find all 'item' objects and print their 'name' attribute
        for elem in root:
            for subelem in elem.findall('Mod'):
                # if we know the name of the attribute, access it directly
                stat = subelem.get('name')
                #print('stat')
                #print(subelem.get('name'))
                #print ('value')
                #print (subelem.text)
                self.stats[subelem.get('name')] = int(subelem.text)

            for subelem in elem.findall('Skill'):
                # if we know the name of the attribute, access it directly
                stat = subelem.get('name')
                #print('skill')
                #print(subelem.get('name'))
                #print ('dmg')
                #print (subelem.text)
                self.skills[subelem.get('name')] = int(subelem.text)
        print("Your stats ...")
        print(self.stats)
        print("Your skills ...")
        print(self.skills)

class Combat:

    def __init__(self, player, enemies):

        #self.player = player
        #self.enemies = enemies  # this will be a list of the enemies
        self.player = player
        #self.playerName = player['Name']
        self.enemies = enemies
        self.fightersInts = {}
        self.newIntOrder = []
        for i in self.enemies:
        #for i in enemies:
            self.fightersInts[dX(20)] = i.stats['Name']
        #self.fightersInts[(player.stats['Dex'] + dX(20))] = player
        self.fightersInts[dX(20)] = self.player.stats['Name']
        #self.fightersInts[dX(20)] = player
        self.turn_Order()
        winner = self.action_Order()

    def action_Order(self):
        print("Turn start!")
        self.ssshow_privates(self.player.stats)
        if self.check_Continue() == True:
            #print(self.player.stats['Name'])
            #print(self.fightersInts[self.newIntOrder[0]])
            print ("It is " + self.fightersInts[self.newIntOrder[0]] + "'s turn.'")
            if (self.player.stats['Name'] == self.fightersInts[self.newIntOrder[0]]):
                self.player_Turn()
            else:
                self.enemy_Turn()
            #print(self.newIntOrder)
            self.newIntOrder.append(self.newIntOrder[0])
            self.newIntOrder.pop(0)
            #self.newIntOrder.append(self.newIntOrder.pop(self.newIntOrder.index(0)))
            self.action_Order()
        else:
            return (self.checkContinue)

    def turn_Order(self):
        #sorts dictionary and returns list of the order of keys

        self.newIntOrder = (sorted(self.fightersInts.keys(), reverse=True))


    def check_Continue(self):
        #Will return true or the victor of the fight
        return (True)

    def player_Turn(self):
        #Will be the player turn
        # show options
        # perform actions
        #display the new stats
        action = self.player_Actions()
        print("This will be the player's turn!")

    def player_Actions(self):
        for i in self.player.skills:
            print (i)
        impact = input("Please choose one of your skills")
        target = int(input("Now who is your target, please identify the index"))
        bigdikdmg = dX(self.player.skills[impact])
        print (bigdikdmg)
        print ('You attack with {skill} and deal {amount} damage to {enemy}!'.format(skill = impact, amount = bigdikdmg, enemy = self.enemies[target].stats['Name']))

    def enemy_Turn(self):
        #will display the stats
        #will do actions from choices(maybe random)
        #will display new stats
        print("This will be the villian's turn!")

    def ssshow_privates(self, privateArea):
        #will display the stats of everyone in the battle (neat way?)
        print(privateArea)
        for x in privateArea:
            print ('{privateSpots} : {privateStats}'.format(privateSpots = x, privateStats = privateArea[x]))


def dX(sides):
    # This function rolls a dX and prints out the value, returning it as well
    value = random.randint(1, sides)
    print("You rolled a D", +sides, " and got ...")
    msvcrt.getch()
    print(value)
    return (value)


def char_Create():
#This will be the starting function that helps guide the user through character creation
#later might be able to check this through the reading interpreter that I develop
    print('Should first start with an intro story probably or let them choose their class first?? unsure- \n')
    who = userInputHack(False, 'Please ... tell me your name ... \n')
    reply = input('So your name is {person}?'.format(person = who))
    if reply != True:
        print ("True")
    attribute = input('Now what devotion will you choose, Saber or Caster?')
    start = PC(who, attribute)
    badguy = PC("vil", 'Saber') #enemies should have their own class, should not print out any of these things, will have their own pre determined stats
    Combat(start, [badguy])

def userInputHack(restricion, prompt):
    input_Hack = input(prompt)
    print (prompt)
    print (restricion)
    if restricion != False:
        print("Why are you here??")
        if input_Hack in restricion:
            pass
        else:
            print("This is not a valid input for the prompt, try again.")
            input_Hack = userInputHack(restricion, prompt)
    return input_Hack


#I want to read the text for the VN and use it to move through the game
#Might just do it in XML instead of through a doc
class textReader:
    def __init__(self, fileName, location):

        self.fileToOpen = fileName
        self.startLocation = location  # this will be a list of the enemies

    def oneLine(self):
        #story = open("self.fileToOpen", "r")
        #print story.readline():
        #story.close()
            # functions
        pass

def main():
    char_Create()

main()
