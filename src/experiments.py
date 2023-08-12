import csv
import numpy as np
import math
from itertools import product
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

    iterations = 100

    for ball, pokemon in product(balls, pokemons):
        catch_rate = np.average(
            [attempt_catch(pokemon, ball)[0] for _ in range(iterations)]
        )
        data.append([catch_rate, pokemon.name, ball])

    # save data to csv
    with open(output_file, "w") as file:
        writer = csv.writer(file)
        # write header
        header = ["catch_rate", "pokemon", "ball"]
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
        pokemon = factory.create(pokemon_name, level, StatusEffect.NONE, hp_percentage)

        for stat in StatusEffect:
            pokemon.status_effect = stat

            catch_rate = np.average(
                [attempt_catch(pokemon, ball)[0] for _ in range(iterations)]
            )

            writer.writerow([stat.name, catch_rate])


# ----------------------------------- Ej 2-b -----------------------------------


def variating_hp_experiment(
    pokemon_name: str, ball: str, noise: float, iterations: int, output_file: str
):
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["hp_percentage", "catch_rate", "std"])

        factory = PokemonFactory("pokemon.json")
        pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)

        for hp_percentage in range(1, 101):
            pokemon.current_hp = math.floor(pokemon.max_hp * hp_percentage / 100)

            results = np.array(
                [attempt_catch(pokemon, ball, noise)[1] for _ in range(iterations)]
            )
            catch_rate = np.average(results)
            std = np.std(results)

            writer.writerow([hp_percentage, catch_rate, std])


# ----------------------------------- Ej 2-d -----------------------------------
def variating_everything_experiment(
    pokemon_name: str, iterations: int, output_file: str
):
    factory = PokemonFactory("pokemon.json")
    pokemon = factory.create(pokemon_name, 1, StatusEffect.NONE, 1)

    balls = ["pokeball", "ultraball", "fastball", "heavyball"]

    header = ["pokemon", "status_effect", "hp", "level", "pokeball", "catch_rate"]
    data = []

    for stat, current_hp, current_lvl, ball in product(
        StatusEffect, range(1, pokemon.max_hp), range(1, 100), balls
    ):
        pokemon.status_effect = stat
        pokemon.current_hp = current_hp
        pokemon.level = current_lvl

        catch_rate = np.average(
            [attempt_catch(pokemon, ball)[0] for _ in range(iterations)]
        )

        data.append(
            [
                pokemon.name,
                stat.name,
                current_hp,
                current_lvl,
                ball,
                catch_rate,
            ]
        )

    with open(output_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
