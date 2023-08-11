import csv
import numpy as np
from .pokemon import PokemonFactory, StatusEffect
from .catching import attempt_catch

# ----------------------------------- Ej 1-a -----------------------------------


def pokeball_in_ideal_conditions_experiment(output_file: str):
    factory = PokemonFactory("pokemon.json")

    # pokemons at lvl 100 & HP 100%
    jolteon = factory.create("jolteon", 100, StatusEffect.NONE, 1)
    caterpie = factory.create("caterpie", 100, StatusEffect.NONE, 1)
    snorlax = factory.create("snorlax", 100, StatusEffect.NONE, 1)
    onix = factory.create("onix", 100, StatusEffect.NONE, 1)
    mewtwo = factory.create("mewtwo", 100, StatusEffect.NONE, 1)

    pokemons = [jolteon, caterpie, snorlax, onix, mewtwo]
    balls = [
        "pokeball",
        "ultraball",
        "fastball",
        "heavyball",
    ]
    data = []

    for ball in balls:
        catches = 0
        for pokemon in pokemons:
            for _ in range(100):
                if attempt_catch(pokemon, ball)[0]:
                    catches += 1
            successrate = catches / 100
            data += [[successrate, pokemon.name, ball]]

    # save data to csv
    with open(output_file, "w") as file:
        writer = csv.writer(file)
        # write header
        header = ["successrate", "pokemon", "ball"]
        writer.writerow(header)
        writer.writerows(data)


# ----------------------------------- Ej 2-a -----------------------------------


def variating_status_experiment(
    pokemon_name: str,
    ball: str,
    level: int,
    hp_percentage: float,
    iterations: int,
    output_file: str,
):
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["status", "catchRate"])

        factory = PokemonFactory("pokemon.json")

        for stat in StatusEffect:
            pokemon = factory.create(
                pokemon_name, level, stat, hp_percentage
            )

            catches = 0
            for _ in range(iterations):
                catched, _ = attempt_catch(pokemon, ball)
                if catched:
                    catches += 1

            catchRate = catches / iterations
            writer.writerow([str(stat), str(catchRate)])


# ----------------------------------- Ej 2-b -----------------------------------


def variating_hp_experiment(
    pokemon_name: str, ball: str, noise: float, iterations: int, output_file: str
):
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


# ----------------------------------- Ej 2-d -----------------------------------
def variating_everything_experiment(
    pokemon_name: str, iterations: int, output_file: str
):
    factory = PokemonFactory("pokemon.json")
    pokemon = factory.create(pokemon_name, 1, StatusEffect.NONE, 1)

    balls = ["pokeball", "ultraball", "fastball", "heavyball"]

    header = ["pokemon", "status_effect", "hp", "level", "pokeball", "success_rate"]
    data = []

    for stat in StatusEffect:
        pokemon.status_effect = stat
        for current_hp in range(1, pokemon.max_hp):
            pokemon.current_hp = current_hp
            for current_lvl in range(1, 100):
                pokemon.level = current_lvl
                for ball in balls:
                    catches = 0
                    for _ in range(iterations):
                        if attempt_catch(pokemon, ball)[0]:
                            catches += 1
                    success_rate = catches / iterations
                    data += [
                        [
                            pokemon.name,
                            stat.name,
                            current_hp,
                            current_lvl,
                            ball,
                            success_rate,
                        ]
                    ]

    with open(output_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
