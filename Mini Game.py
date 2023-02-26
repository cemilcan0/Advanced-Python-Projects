import time
import random
import sys

class mainclass():
    def __init__(self,player,health=100,energy=80,):
        self.player    = player
        self.health       = health
        self.energy    = energy
        self.damage     = 0
        self.damage_taken    = 0
    def status(self):
        print("Health :",self.health,"\nEnergy: ",self.energy,"\nTotal damage taken: ",self.damage,'\n Attack Power: ',self.damage_taken )
    def saldır(self,bot):
        power = self.attack_calculation()
        print('ATTACKING')
        for i in range(10):
            time.sleep(.3)
            print(".\n",end="",flush=True)
        
        if power == 0:
            print('No Damage, You Missed...\n')
        elif power == 1:
            print('Enemy Damaged\n')
            self.damage_calculation(bot)
        elif power == 2:
            print('Your Opponent Counterattacked, You Taken the Damage\n')
            bot.damage_calculation(self)

    def damage_calculation(self,enemy):
        if self.damage_taken  == 0:
            enemy.health-=10
        else:
            enemy.health-=20
        enemy.energy-=5
        enemy.damage+=1
        if enemy.damage>5:
            enemy.health-=5
            if enemy.health<=0:
                print(f'{enemy.player} Died... Game Winner {self.player}')
                sys.exit()
        if enemy.health<=0:
            print(f'{enemy.player} Died... Game Winner {self.player}')
            sys.exit()
            
    def attack_calculation(self):
        return random.randint(0,2)
    def weapon_damage(self):
        self.damage_taken +=1
        
        
        

    def escape(self):
        escape= random.randint(0,2)
        print('Running')
        for i in range(5):
                time.sleep(.1)
                print(".",end="",flush=True)
        if escape==0:
            print('\nYou Ran Away From The Enemy... you are healing.')
            self.health+=5
            print('You found a gun piece on the ground while you were running away.. Press 1 to upgrade your weapon')
            take_gun=int(input('Take the gun'))
            if take_gun==1:
                self.weapon_damage()
        else:
            print('\nThe enemy has caught you...')
        
        
def write(history):
    for i in history:
        time.sleep(.031)
        print(i,end="",flush=True)
        
history='Annie and Alex get lost on an island. They argue among themselves, they get into a fight...\n'
write(history)

p1 = mainclass('Alex')
p2 = mainclass('Annie')
        
        
        
while True:
    print('\Alex is currently facing her opponent.',
          'The move you want to make: ',
          'Attack :  a',
          'Escape :  e',
          'Quit   :  q', sep='\n')

    move = input('\n> ')
    if move =='a':
        p1.saldır(p2)
        print('Annie\'s Status...')
        p2.status()
        
        print('\nAlex\'s Status...')
        p1.status()
    elif move == 'e':
        p1.escape()
        print('Annie\'s Status...')
        p2.status()
        
        print('\nAlex\'s Status...')
        p1.status()
    elif move == "q":
        print('The Game Is Closing',end='')
        for i in range(5):
            time.sleep(.3)
            print('.',end='',flush=True)
        break
    else:
        print("Please Press A Defined Key")