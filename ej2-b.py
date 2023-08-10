import csv
import numpy as np
from src.pokemon import PokemonFactory, StatusEffect
from src.catching import attempt_catch

# Config TODO: move to a config file?
ball = "pokeball"
pokemon_name = "snorlax"
noise = 0.15
iterations = 100
output_file = "data/ej2-b.csv"

# Experiment
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["hp", "catch_rate", "std"])

    factory = PokemonFactory("pokemon.json")
    pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)

    for hp in range(1, pokemon.max_hp):
        pokemon.current_hp = hp

        results = np.array(
            [attempt_catch(pokemon, ball, noise)[1] for _ in range(iterations)]
        )
        average = np.average(results)
        std = np.std(results)

        writer.writerow([hp, average, std])
