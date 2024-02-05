from battle_setup import battle_setup
from battle_run import battle_run
from data_ingestion import ingest_data
import pandas as pd

moves_data, pokemon_data = ingest_data()[0:2]
normal_shiny_dark_golden = ['Normal',
                            'Dark',
                             'Shiny']
attacker_items = ['Power Boost', 
                  'Life Orb', 
                  'Elemental Stone']
defender_level_array = [1, 
                        1.4, 
                        1.6, 
                        1.8, 
                        2]
attacker_level = 100
attacker_type = None
ancientpower_boosts = [1, 
                       1.5, 
                       2, 
                       2.5, 
                       3, 
                       3.5, 
                       4]

one_hit_ko_array = []

def battle_loop_sim():
    for pokemon in pokemon_data:
        for level in defender_level_array:
            for type in normal_shiny_dark_golden:
                for boost in ancientpower_boosts:
                    for item in attacker_items:
                        setup = battle_setup('Arceus (Normal)', pokemon, atk_level=attacker_level, def_level=int(attacker_level*level), atk_sgd=attacker_type, def_sgd=type, ap_boost=boost, item=item)
                        battle_outcome = battle_run(setup[0], setup[1], setup[2])
                        if battle_outcome == 1:
                            one_hit_ko_array.append([pokemon, attacker_level*level, type, boost, item])
            

if __name__ == '__main__':
    battle_loop_sim()
    df = pd.DataFrame(one_hit_ko_array, columns=['Pokemon', 'Level', 'Type', 'Ancientpower Boosts', 'Item'])
    df = df.sort_values(by=['Level', 'Type'], ascending=False)
    df = df.drop_duplicates(subset=['Pokemon', 'Item', 'Ancientpower Boosts'], keep='first')
    power_boost = df[df['Item'] == 'Power Boost']
    life_orb = df[df['Item'] == 'Life Orb']
    elemental_stone = df[df['Item'] == 'Elemental Stone']
    print(power_boost.sort_values(by='Ancientpower Boosts', ascending=False))



