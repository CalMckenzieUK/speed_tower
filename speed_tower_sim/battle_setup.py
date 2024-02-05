from pokemon_builder import build_pokemon
from data_ingestion import ingest_data
from items_and_modifiers import item_mods, modifiers

moves_data, pokemon_data, weakness_matrix = ingest_data()

def attack_setup(attacking_pokemon):
    level = attacking_pokemon.level
    attack_dict = {}
    damage = 0
    move_used = ''
    attack_type = ''
    spec_phys_output = ''
    for move in attacking_pokemon.moves:
        spec_phys_stat = attacking_pokemon.special_attack if moves_data[move]['movetype'] == 'Special' else attacking_pokemon.attack
        move_damage = ((attacking_pokemon.attack + 46.875) * (level/50) + 5)
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
            , def_level: int = 100
            , atk_sgd: str = None
            , def_sgd: str = None
            , ap_boost: int = 1
            , item: str = None):
    attacker = build_pokemon(attacking_pokemon, held_item=item, sgd=atk_sgd, moves=moves, level=atk_level, ap_boost=ap_boost)
    defender = build_pokemon(defending_pokemon, sgd=def_sgd, level=def_level)
    damage, move_used = attack_setup(attacker)    
    defence = defence_setup(defender, move_used)
    mods_list = modifiers(move_used, attacker, defender)
    mods_sum = mods_list['stab'] * mods_list['weakness'] * mods_list['item'] * mods_list['extra']
    return damage, defence, mods_sum