from battle_setup import battle_setup
from battle_run import battle_run
from data_ingestion import ingest_data
import pandas as pd

moves_data, pokemon_data = ingest_data()[0:2]
normal_shiny_dark_golden = ['Normal', 'Shiny', 'Dark']
defender_level_array = [1, 1.4, 1.6, 1.8, 2]
attacker_level = 100
attacker_type = None

one_hit_ko_array = []

def battle_loop_sim():
    for pokemon in pokemon_data:
        for level in defender_level_array:
            for type in normal_shiny_dark_golden:
                setup = battle_setup('Arceus (Normal)', pokemon, atk_level=attacker_level, def_level=int(attacker_level*level), atk_sgd=attacker_type, def_sgd=type)
                battle_outcome = battle_run(setup[0], setup[1], setup[2])
                if battle_outcome == 1:
                    one_hit_ko_array.append([pokemon, attacker_level*level, type])

if __name__ == '__main__':
    battle_loop_sim()
    df = pd.DataFrame(one_hit_ko_array, columns=['Pokemon', 'Level', 'Type'])
    print(df.sort_values(by='Level'))



