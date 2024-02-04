from data_ingestion import ingest_data

moves_data, pokemon_data, weakness_matrix = ingest_data()

def item_mods(attacking_pokemon):
    item = attacking_pokemon.item
    if item == 'Life Orb':
        return 1.3
    elif item == 'Elemental Stone':
        return 1.5
    else:
        return 1

def modifiers(move, attacking_pokemon, defending_pokemon):
    mods = {}
    mods['stab'] = 1.5 if moves_data[move]['type'] == attacking_pokemon.type1 or moves_data[move]['type'] == attacking_pokemon.type2 else 1
    type_weakness_1 = weakness_matrix[moves_data[move]['type'].upper()][str(defending_pokemon.type1).upper()] 
    type_weakness_2 = weakness_matrix[moves_data[move]['type'].upper()][str(defending_pokemon.type2).upper()] if defending_pokemon.type2 else 1
    mods['weakness'] = type_weakness_1 * type_weakness_2
    mods['item'] = item_mods(attacking_pokemon)
    mods['extra'] = 1.5
    return mods