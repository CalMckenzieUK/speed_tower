from pokemon_builder import pokemon_init
from data_ingestion import ingest_data

moves_data, pokemon_data, weakness_matrix = ingest_data()

def build_pokemon(name, held_item=None, sgd=None, moves: list[str] = ['Giga Drain', 'Ice Ball', 'Ancientpower', 'Earthquake']):
    value = pokemon_data[name]
    built_pokemon = pokemon_init(name, str(value).replace("['",'').split(' ')[0], value[1], value[2], value[3], value[4], value[5], value[6], str(value).replace("',",'').split(' ')[1] if len(str(value).split(' ')) > 1 else None, item=held_item, moves=moves, sdg=sgd)
    return built_pokemon

def attack_setup(attacking_pokemon, defending_pokemon, item:str, level: int):
    damage = 0
    item_multiplier = {'Life Orb': 1.3, 'Power Boost': 5, 'Elemental Stone' : 1.5, 'None': 1}
    attacking_pokemon.attack = attacking_pokemon.attack * item_multiplier[item] if item != None and item != 'Power Boost' else attacking_pokemon.attack
    attacking_pokemon.attack = attacking_pokemon.attack + item_multiplier[item] if item == 'Power Boost' else attacking_pokemon.attack
    attacking_pokemon.speed = attacking_pokemon.speed * item_multiplier[item] if item == 'Power Boost' else attacking_pokemon.speed 
    move_used = ''
    for move in attacking_pokemon.moves:
        stab = 1.5 if moves_data[move]['type'] == attacking_pokemon.type1 or moves_data[move]['type'] == attacking_pokemon.type2 else 1
        move_power = moves_data[move]['power']
        type_weakness_1 = weakness_matrix[moves_data[move]['type'].upper()][str(defending_pokemon.type1).upper()] 
        type_weakness_2 = weakness_matrix[moves_data[move]['type'].upper()][str(defending_pokemon.type2).upper()] if defending_pokemon.type2 else 1
        combined_type_multipler = type_weakness_1 * type_weakness_2
        spec_phys_stat = attacking_pokemon.special_attack if moves_data[move]['movetype'] == 'Special' else attacking_pokemon.attack
        # move_damage = stab * move_power * combined_type_multipler * spec_phys_stat
        move_damage = ((attacking_pokemon.attack + 46.875) * (level/50) + 5)*stab
        damage = move_damage if move_damage > damage else damage    
        move_used = move if move_damage == damage else move_used
    print('attack_setup done. damage from {} using {} is : {} '.format(attacking_pokemon.name, move_used, damage))
    return damage

def defence_setup(defending_pokemon, defence_level=100):
    defence = defending_pokemon.defence
    print('defence_setup done. defence is: {}'.format(defence))
    return defence

def battle(attacking_pokemon: str
            , defending_pokemon: str
            , moves: list[str] = ['Close Combat', 'Ice Ball', 'Ancientpower', 'Earthquake']
            , level: int = 100):
    attacker = build_pokemon(attacking_pokemon, held_item='Power Boost', sgd='Shiny', moves=moves)
    defender = build_pokemon(defending_pokemon)
    print(attacker.moves)
    damage = attack_setup(attacker, defender, attacker.item, level)
    # defence = defence_setup(defender)
    if damage > defender.hp:
        return defender.name


battle('Hitmonlee', 'Blissey', level=100)



