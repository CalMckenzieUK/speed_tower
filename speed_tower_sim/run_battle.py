from pokemon_builder import pokemon_init
from data_ingestion import ingest_data

moves_data, pokemon_data, weakness_matrix = ingest_data()

def build_pokemon(name, held_item=None, sgd=None, moves: list[str] = ['Giga Drain', 'Ice Ball', 'Ancientpower', 'Earthquake'], level: int = 100):
    value = pokemon_data[name]
    built_pokemon = pokemon_init(name, str(value).replace("['",'').split(' ')[0], value[1], value[2], value[3], value[4], value[5], value[6], str(value).replace("',",'').split(' ')[1] if len(str(value).split(' ')) > 1 else None, item=held_item, moves=moves, sdg=sgd, level=level)
    return built_pokemon

def attack_setup(attacking_pokemon, defending_pokemon, item:str):
    level = attacking_pokemon.level
    attack_dict = {}
    damage = 0
    item_multiplier = {'Life Orb': 1.3, 'Power Boost': 5, 'Elemental Stone' : 1.5, 'None': 1}
    attacking_pokemon.attack = attacking_pokemon.attack * item_multiplier[item] if item != None and item != 'Power Boost' else attacking_pokemon.attack
    attacking_pokemon.attack = attacking_pokemon.attack + item_multiplier[item] if item == 'Power Boost' else attacking_pokemon.attack
    attacking_pokemon.speed = attacking_pokemon.speed * item_multiplier[item] if item == 'Power Boost' else attacking_pokemon.speed 
    move_used = ''
    attack_type = ''
    spec_phys_output = ''
    for move in attacking_pokemon.moves:
        stab = 1.5 if moves_data[move]['type'] == attacking_pokemon.type1 or moves_data[move]['type'] == attacking_pokemon.type2 else 1
        move_power = moves_data[move]['power']
        type_weakness_1 = weakness_matrix[moves_data[move]['type'].upper()][str(defending_pokemon.type1).upper()] 
        type_weakness_2 = weakness_matrix[moves_data[move]['type'].upper()][str(defending_pokemon.type2).upper()] if defending_pokemon.type2 else 1
        combined_type_multipler = type_weakness_1 * type_weakness_2
        spec_phys_stat = attacking_pokemon.special_attack if moves_data[move]['movetype'] == 'Special' else attacking_pokemon.attack
        move_damage = ((attacking_pokemon.attack + 46.875) * (level/50) + 5)*stab
        spec_phys_output = 'Special' if moves_data[move]['movetype'] == 'Special' else 'Physical'
        move_used = move if move_damage > damage else move_used
        attack_type = spec_phys_stat if move_damage > damage else attack_type
        damage = move_damage if move_damage > damage else damage    

    attack_dict['type'] = spec_phys_output
    attack_dict['attack'] = attack_type
    attack_dict['speed'] = attacking_pokemon.speed
    attack_dict['move_power'] = moves_data[move_used]['power']
    attack_dict['level'] = attacking_pokemon.level
    return attack_dict, move_used

def defence_setup(defending_pokemon, move_used):
    defence_dict = {}
    defence_dict['hp'] = defending_pokemon.hp
    defence_dict['defence'] = defending_pokemon.special_defence if moves_data[move_used]['movetype'] == 'Special' else defending_pokemon.defence
    defence_dict['speed'] = defending_pokemon.speed
    defence_dict['level'] = defending_pokemon.level
    return defence_dict

def battle_setup(attacking_pokemon: str
            , defending_pokemon: str
            , moves: list[str] = ['Close Combat', 'Ice Ball', 'Ancientpower', 'Earthquake']
            , atk_level: int = 100
            , def_level: int = 100):
    print(atk_level, def_level)
    attacker = build_pokemon(attacking_pokemon, held_item='Power Boost', sgd='Shiny', moves=moves, level=atk_level)
    defender = build_pokemon(defending_pokemon, sgd=None, level=def_level)
    damage, move_used = attack_setup(attacker, defender, attacker.item)    
    defence = defence_setup(defender, move_used)
    return damage, defence

def battle_run(damage, defence):
    print(damage)
    hp = (defence['hp'] + 65) * defence['level']/50 + 10
    defence_def = (defence['defence'] + 46.875) * defence['level']/50 + 5
    attack = (damage['attack'] + 46.875) * damage['level']/50 + 5
    damageMin = (((2* damage['level']/5 + 2) * attack * damage['move_power'] /defence_def)/50 * 85 / 100 + 2) 
    print(damageMin, hp)
    
    
    # print(f'HP: {hp} Defence: {defence_def} Attack: {attack} Move Power: {damage["move_power"]}')

if __name__ == '__main__':
    setup = battle_setup('Hitmonlee', 'Blissey', atk_level=290, def_level=300)
    battle_run(setup[0], setup[1])



