import json

def ingest_data():
    with open('./data/tppc_move_data.json') as f:
        moves_data = json.load(f)
    with open('./data/tppc_poke_data.json') as f:
        pokemon_data = json.load(f)
    with open('./data/weakness_matrix.json') as f:
        weakness_matrix = json.load(f)
    return moves_data, pokemon_data, weakness_matrix

if __name__ == '__main__':
    moves_data, pokemon_data, weakness_matrix = ingest_data()
    print(weakness_matrix['WATER']['FIRE'])
    