from pokemon_builder import pokemon_init
from data_ingestion import ingest_data

moves_data, pokemon_data = ingest_data()

def users_pokemon(name, held_item=None):
    value = pokemon_data[name]
    built_pokemon = pokemon_init(name, str(value).split(' ')[0], value[1], value[2], value[3], value[4], value[5], value[6], str(value).split(' ')[1] if len(str(value).split(' ')) > 1 else None, item=held_item)
    print(built_pokemon.item)



users_pokemon('Bulbasaur', 'Leftovers')


