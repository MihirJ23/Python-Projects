class Superhero:
    powerPoints = 0
    def __init__(self, name, heroType, side):
        self.title = name
        if (heroType == 'human'):
            self.health = 1000
        if (heroType == 'god'):
            self.health = 1500
        if (heroType == 'mutant'):
            self.health = 1250
        self.type = heroType
        self.side = side

    def heroAttack(self, hero, villian):
        if(hero.heroType == 'god'):
            print(hero, 'attacked', villian, 'with Cosmic Strike of 65 damage')
            villian.health = villian.health - 65
        if(hero.heroType == 'mutant'):
            print(hero, 'attacked', villian, 'with Shield Storm of 50 damage')
            villian.health = villian.health - 50
        if(hero.heroType == 'human'):
            print(hero, 'attacked', villian, 'with Frenzy Kick of 35 damage')
            villian.health = villian.health - 35

    def heroSuperAttack(self, hero, villian):
        if(hero.heroType == 'god'):
            print(hero, 'attacked', villian, 'with Bolt Attack of 130 damage')
            villian.health = villian.health - 130
        if(hero.heroType == 'mutant'):
            print(hero, 'attacked', villian,
                  'with Vibranium Attack of 95 damage')
            villian.health = villian.health - 95
        if(hero.heroType == 'human'):
            print(hero, 'attacked', villian, 'with Missile Swarm of 70 damage')
            villian.health = villian.health - 70


class Villian:
    powerPoints = 0
    def __init__(self, name, villianType, side):
        self.title = name
        if (villianType == 'human'):
            self.health = 1000
        if (villianType == 'god'):
            self.health = 1500
        if (villianType == 'mutant'):
            self.health = 1250
        self.type = villianType
        self.side = side

    def villianAttack(self, hero, villian):
        if(villian.heroType == 'god'):
            print(hero, 'attacked', villian, 'with Fire Breath of 75 damage')
            hero.health = hero.health - 75
        if(villian.heroType == 'mutant'):
            print(hero, 'attacked', villian,
                  'with Tentacle Strike of 45 damage')
            hero.health = hero.health - 45
        if(villian.heroType == 'human'):
            print(hero, 'attacked', villian, 'with Knife Carving of 35 damage')
            hero.health = hero.health - 35

    def villianSuperAttack(self, hero, villian):
        if(villian.heroType == 'god'):
            print(villian, 'attacked', hero, 'with a Wave of the Undead of 140 damage')
            hero.health = hero.health - 140
            powerPoints = 0
        if(villian.heroType == 'mutant'):
            print(villian, 'attacked', hero, 'with Poison Storm of 90 damage')
            hero.health = hero.health - 90
            powerPoints = 0
        if(villian.heroType == 'human'):
            print(villian, 'attacked', hero, 'with Speed Punch of 70 damage')
            hero.health = hero.health - 70
            powerPoints = 0

# code for gameplay starts below

print('    Welcome to Heros vs Villians     ')
print('                                  ')
print('We have assembled two teams of 3 for you\n', 
'On one side, we have the soldiers of the light', 'on the other side are the soldiers of the dark\n')
print('On each team is a god, mutant, and superhuman\n', 
'First team to eliminate all the other members wins')

Thor = Superhero("Thor", "god", "hero")
Cap = Superhero("Cap", "mutant", "hero")
Hawkeye = Superhero("Hawkeye", "human", "hero")

Loki = Villian("Loki", "god", "villian")
Octopus = Villian("Octopus", "mutant", "villian")
Maximus = Villian("Maximus", "human", "villian")

arr = [Thor, Cap, Hawkeye, Loki, Octopus, Maximus]

while(Thor.health > 0 and Cap.health > 0 and Hawkeye.health > 0 
or Loki.health > 0 and Octopus.health > 0 and Maximus.health > 0):
    attacker = input('Which character do you want to use?')
    
    receiver = input('Which character do you want to attack')

    move = input('Choose a move\n', 'r for regular attack, s for super attack')

    if (attacker.powerPoints < 100):
        move = input('Choose another option')

    for (i in arr[]):
        if (attacker == arr[i]):
            person = arr[i]
    
    if (move == 'r' and person.side == 'villian'):
        person.villianAttack(attacker, receiver)
    else:
        person.villianSuperAttack(attacker, receiver)

    if (move == 'r' and person.side == 'hero'):
        person.heroAttack(attacker, receiver)
    else:
        person.heroSuperAttack(attacker, receiver)




