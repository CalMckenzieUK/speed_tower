# Description: This file is used to create the pokemon objects that will be used in the simulation

class pokemon_init:
        def __init__(self, name, type1, hp, attack, defence, special_attack ,special_defence, speed, type2 = None, item=None):
            self.name = name
            self.type1 = type1
            self.hp = hp
            self.attack = attack
            self.defence = defence
            self.special_attack = special_attack
            self.special_defence = special_defence
            self.speed = speed
            self.type2 = type2

bulbasaur = pokemon_init('bulbasaur', 'grass', 45, 49, 49, 65, 65, 45, 'poison')

