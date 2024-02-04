from pokemon_builder import pokemon_init
from data_ingestion import ingest_data

moves_data, pokemon_data, weakness_matrix = ingest_data()

def build_pokemon(name, held_item=None):
    value = pokemon_data[name]
    built_pokemon = pokemon_init(name, str(value).split(' ')[0], value[1], value[2], value[3], value[4], value[5], value[6], str(value).split(' ')[1] if len(str(value).split(' ')) > 1 else None, item=held_item)
    return built_pokemon




def battle(attacking_pokemon, defending_pokemon):
    attacker = build_pokemon(attacking_pokemon, 'Leftovers')
    defender = build_pokemon(defending_pokemon)

print(moves_data['Ice Ball'])



