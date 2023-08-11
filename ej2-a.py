import csv
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

ball = "pokeball"
first_pokemon_name = "snorlax"
second_pokemon_name = "jolteon"
iterations = 1000
first_level = 100
second_level = 25
first_hp= 1
second_hp = 0.25
output_file = "ej2-a.csv"
status = [
        "POISON",
        "BURN",
        "PARALYSIS",
        "SLEEP",
        "FREEZE",
        "NONE"
    ]

#Checking how status condition affect catch rate, and if it is independant from pokemon, level or hp

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["pokemon", "level", "hp", "status", "catchRate"])


    factory = PokemonFactory("pokemon.json")

    for stat in status:
        catches = 0;
        pokemon = factory.create(first_pokemon_name, first_level, StatusEffect[stat], first_hp)
        for _ in range(iterations):
            catched, t2 = attempt_catch(pokemon, ball)
            if (catched):
                catches += 1

        catchRate = catches / iterations
        writer.writerow([str(first_pokemon_name), str(first_level), str(first_hp), str(stat), str(catchRate)])

    #reduce level and hp

    for stat in status:
        catches = 0;
        pokemon = factory.create(first_pokemon_name, second_level, StatusEffect[stat], second_hp)
        for _ in range(iterations):
            catched, t2 = attempt_catch(pokemon, ball)
            if (catched):
                catches += 1

        catchRate = catches / iterations
        writer.writerow([str(first_pokemon_name), str(second_level), str(second_hp), str(stat), str(catchRate)])


    #different pokemon with first level and hp

    for stat in status:
        catches = 0;
        pokemon = factory.create(second_pokemon_name, first_level, StatusEffect[stat], first_hp)
        for _ in range(iterations):
            catched, t2 = attempt_catch(pokemon, ball)
            if (catched):
                catches += 1

        catchRate = catches / iterations
        writer.writerow([str(second_pokemon_name), str(first_level), str(first_hp), str(stat), str(catchRate)])
