import csv
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

ball = "pokeball"
pokemon_name = "snorlax"
iterations = 1000
level = 100
hp= 1
output_file = "ej2-a.csv"
status = [
        "POISON",
        "BURN",
        "PARALYSIS",
        "SLEEP",
        "FREEZE",
        "NONE"
    ]


with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["status", "catchRate"])


    factory = PokemonFactory("pokemon.json")
    pokemon = factory.create(pokemon_name, level, StatusEffect.NONE, hp)

    # t1, no_status_catch_rate = attempt_catch(pokemon, ball)
    for stat in status:
        catches = 0;
        pokemon = factory.create(pokemon_name, level, StatusEffect[stat], hp)
        for _ in range(iterations):
            catched, t2 = attempt_catch(pokemon, ball)
            if (catched):
                catches += 1

        catchRate = catches / iterations
        writer.writerow([ str(stat), str(catchRate)])


