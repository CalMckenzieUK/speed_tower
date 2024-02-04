Objectives:

- Program that can receive an input in the form of a proposed speed-tower set-up comprising of a single Pokemon, Item, and Moveset
- Tests this input setup against all combinations of possible enemy Pokemon (S/D/N) at levels compared to the input Pokemon ==, *1.4, *1.6, *1.8, *2
- The program will return a list of results of which enemy Pokemon could be outsped & 1HKO

Approach:

- Ingest ingest moves and Pokemon datasets from data folder (importing the JSON files tppc_poke_data.json & tppc_moves_data.json into dictionaries or arrays)
- Translate the javascript functions in damage.js to Python for ease of dev





Notes: 

- Suspect there will be scenarios where no Pokemon at *2 level can be outsped, in which case will need to rethink parameters and also deal w/ eneny movesets
- Need to factor in Ancientpower buffs, possibly creating subgroups of enemies that be used for set-up of Ancientpowers, and then show results based on minimum number of Ancientpowers required to 1HKO. 

Folder structure plans:

- separate files containing functions for data ingestion and cleaning
- use separate classes for input Pokemon and enemy Pokemon, possibly in a pokemon_builder module eg. 

for pokemon in enemy:  
    run_battle(pokemon_builder(pokemon[name:speed]), pokemon_builder(input_poke[name:speed]))

- the run_battle function will largely be a translation of the 'calculate' function from the original damage.js file