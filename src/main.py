from battle_setup import battle_setup
from battle_run import battle_run
from data_ingestion import ingest_data
import pandas as pd

moves_data, pokemon_data = ingest_data()[0:2]

# attacking_moves = [move for move in moves_data.keys()]
attacking_moves = ['Ancientpower'
                    , 'Close Combat'
                    , 'Ice Ball'
                    , 'Earthquake']

NORMAL_SHINY_DARK_GOLDEN = ['Normal',
                            'Dark',
                             'Shiny']
ATTTACKER_ITEMS = [
                    'Power Boost'
                    # , 'Life Orb', 
                    # 'Elemental Stone'
                    ]
DEFENDER_LEVEL_ARRAY = [1, 
                        1.4, 
                        1.6, 
                        1.8, 
                        2]
ATTACKER_LEVEL = 100
ATTACKER_TYPE = None
ANCIENTPOWER_BOOSTS = [1, 
                       1.5, 
                       2, 
                       2.5, 
                       3, 
                       3.5, 
                       4]

one_hit_ko_array = []

def battle_loop_sim(attacker_name: str ='Arceus (Normal)'):
    for pokemon in pokemon_data:    
        for move in attacking_moves: 
            for level in DEFENDER_LEVEL_ARRAY:
                for type in NORMAL_SHINY_DARK_GOLDEN:
                    for boost in ANCIENTPOWER_BOOSTS:
                        for item in ATTTACKER_ITEMS:
                            setup = battle_setup(attacker_name, pokemon, moves=[move, move], atk_level=ATTACKER_LEVEL, def_level=int(ATTACKER_LEVEL*level), atk_sgd=ATTACKER_TYPE, def_sgd=type, ap_boost=boost, item=item)
                            battle_outcome = battle_run(setup[0], setup[1], setup[2])
                            move_used = setup[3]
                            if battle_outcome == 1:
                                one_hit_ko_array.append([attacker_name, pokemon, move_used, ATTACKER_LEVEL*level, type, boost, item])


def top_attackers(pokemon_data: dict, top_x: int) -> list:
    pokemon_attackers = []
    for pokemon, stats in pokemon_data.items():
        pokemon_attackers.append([pokemon, stats[2], stats[4]])
    attacker_df = pd.DataFrame(pokemon_attackers, columns=['Pokemon', 'Attack', 'SpAtk']).sort_values(by=['Attack'], ascending=False).head(top_x)
    spatk_df = pd.DataFrame(pokemon_attackers, columns=['Pokemon', 'Attack', 'SpAtk']).sort_values(by=['SpAtk'], ascending=False).head(top_x)
    best_attackers = pd.concat([attacker_df, spatk_df]).drop_duplicates(subset=['Pokemon'], keep='first')
    return best_attackers['Pokemon'].to_list()

if __name__ == '__main__':
    all_results = []
    attackers = top_attackers(pokemon_data, 2)
    for pokemon in attackers:
        print(pokemon)
        battle_loop_sim(pokemon)
        df = pd.DataFrame(one_hit_ko_array, columns=['attacker', 'defender', 'attacking_moves', 'defender_level', 'nsdg', 'ancientpower_boosts', 'attacker_item'])
        df['ancientpower_boosts'] = df['ancientpower_boosts'].replace({1: 0, 1.5: 1, 2: 2, 2.5: 3, 3: 4, 3.5: 5, 4: 6})
        # df = df.sort_values(by=['defender_level', 'nsdg'], ascending=False)
        if len(all_results) == 0:
            all_results = df
        else:
            all_results = pd.concat([all_results, df])
    min_ancientpower_boosts = all_results.groupby(['attacker', 'defender', 'attacking_moves', 'defender_level', 'nsdg', 'attacker_item']).agg({'ancientpower_boosts': 'max'}).reset_index()
    # all_results.to_csv('./data/one_hit_ko.csv', index=False)
    print(min_ancientpower_boosts)




