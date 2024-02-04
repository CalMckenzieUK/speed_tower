# Description: This file is used to create the pokemon objects that will be used in the simulation

class pokemon_init:
        def __init__(self, 
                     name: str, 
                     type1: str, 
                     hp: int, 
                     attack: int, 
                     defence: int, 
                     special_attack: int,
                     special_defence: int, 
                     speed: int,  
                     type2: str = None, 
                     item: str = None,
                     moves: list[str] = None,
                     sdg: str = None):
            
                self.name = name
                self.type1 = type1
                self.hp = hp
                self.attack = attack
                self.defence = defence
                self.special_attack = special_attack
                self.special_defence = special_defence
                self.speed = speed
                self.type2 = type2
                self.item = item
                self.moves = moves
                self.level = 100

                if sdg == 'Shiny':
                        self.hp = hp+5
                        self.attack = attack+5
                        self.defence = defence+5
                        self.special_attack = special_attack+5
                        self.special_defence = special_defence+5
                        self.speed = speed+5

                elif sdg == 'Dark':
                        self.hp = hp+15
                        self.attack = attack+15
                        self.defence = defence+15
                        self.special_attack = special_attack+15
                        self.special_defence = special_defence+15
                        self.speed = speed+15
                
                elif sdg == 'Golden':
                        self.hp = hp+15
                        self.attack = attack+15
                        self.defence = defence+15
                        self.special_attack = special_attack+15
                        self.special_defence = special_defence+15
                        self.speed = speed+15

# bulbasaur = pokemon_init('bulbasaur', 'grass', 45, 49, 49, 65, 65, 45, 'poison', item='leftovers')