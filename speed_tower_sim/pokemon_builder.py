from data_ingestion import ingest_data

pokemon_data = ingest_data()[1]

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
                     sdg: str = None,
                     level: int = None):
            
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
                self.level = level

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

                if item == 'Power Boost':
                        self.attack = attack+5
                        self.special_attack = special_attack+5
                        self.speed = speed+5
                        self.defence = defence+5
                        self.special_defence = special_defence+5
                        self.hp = hp+5
                
                if item == 'Life Orb':
                        self.attack = attack*1.3
                
                if item == 'Elemental Stone':
                        self.attack = attack*1.5
                        self.special_attack = special_attack*1.5

def build_pokemon(name, held_item=None, sgd=None, moves: list[str] = ['Giga Drain', 'Ice Ball', 'Ancientpower', 'Earthquake'], level: int = 100):
    value = pokemon_data[name]
    built_pokemon = pokemon_init(name, str(value).replace("['",'').split(' ')[0], value[1], value[2], value[3], value[4], value[5], value[6], str(value).replace("',",'').split(' ')[1] if len(str(value).split(' ')) > 1 else None, item=held_item, moves=moves, sdg=sgd, level=level)
    return built_pokemon

if __name__ == "__main__":
    print(build_pokemon('Bulbasaur').attack)