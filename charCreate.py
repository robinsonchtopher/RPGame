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
        self.stats['Alter'] = alter
        self.stats['Lvl'] = 1
        self.stats['Exp'] = 0
        self.fill_Stats()
        self.stats['MaxHp'] = self.stats['Con']
        self.Hp_Up()
        self.stats['MyHp'] = self.stats['MaxHp']
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
        print(self.stats)
        doctitle = self.stats['Alter'] + str(self.stats['Lvl']) + '.xml'
        print (doctitle)
        print ('You now have chosen your path.')
        tree = ET.parse(doctitle)
        root = tree.getroot()
        print(self.stats)

        tree = ET.parse('Saber1.xml')
        root = tree.getroot()


        # find all 'item' objects and print their 'name' attribute
        for elem in root:
            for subelem in elem.findall('Mod'):
                # if we know the name of the attribute, access it directly
                stat = subelem.get('name')
                print('stat')
                print(subelem.get('name'))
                print ('value')
                print (subelem.text)
                self.stats[subelem.get('name')] = int(subelem.text)

            for subelem in elem.findall('Skill'):
                # if we know the name of the attribute, access it directly
                stat = subelem.get('name')
                print('skill')
                print(subelem.get('name'))
                print ('dmg')
                print (subelem.text)
                self.skills[subelem.get('name')] = int(subelem.text)
        print(self.stats)
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
        print(self.fightersInts)
        print(player.stats['Name'])
        print("enemy name")
        self.turn_Order()
        print("this is the first fighter")
        print(self.fightersInts[self.newIntOrder[0]])
        self.action_Order()

    def action_Order(self):
        print("Start action!")
        dX(100)
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
            print("This is with the append")
            print(self.newIntOrder)
            self.newIntOrder.pop(0)
            #self.newIntOrder.append(self.newIntOrder.pop(self.newIntOrder.index(0)))
            print ("this is the new order")
            print(self.newIntOrder)
            self.action_Order()
        else:
            return (self.checkContinue)

    def turn_Order(self):
        #sorts dictionary and returns list of the order of keys

        self.newIntOrder = (sorted(self.fightersInts.keys(), reverse=True))
        print (self.newIntOrder)


    def check_Continue(self):
        #Will return true or the victor of the fight
        return (True)

    def player_Turn(self):
        #Will be the player turn
        # show options
        # perform actions
        #display the new stats
        action = self.player_Actions()
        dX(100)
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
        dX(100)
        print("This will be the villian's turn!")

    def show_Stats(self):
        #will display the stats of everyone in the battle (neat way?)
        pass


def dX(sides):
    # This function rolls a dX and prints out the value, returning it as well
    value = random.randint(1, sides)
    print("You rolled a D", +sides, " and got ...")
    msvcrt.getch()
    print(value)
    return (value)



print('This is where your journey begins ...  more will be read from a file later')
who = input('Please ... tell me your name ...')

attribute = input('Now what devotion will you choose, Saber or Caster?')
start = PC(who, attribute)
badguy = PC("vil", 'Saber')
Combat(start, [badguy])


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
