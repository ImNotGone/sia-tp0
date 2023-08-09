from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")

    # pokemons at lvl 100 & HP 100%
    jolteon = factory.create("jolteon", 100, StatusEffect.NONE, 1)
    caterpie = factory.create("caterpie", 100, StatusEffect.NONE, 1)
    snorlax = factory.create("snorlax", 100, StatusEffect.NONE, 1)
    onix = factory.create("onix", 100, StatusEffect.NONE, 1)
    mewtwo = factory.create("mewtwo", 100, StatusEffect.NONE, 1)

    pokemons = [
        jolteon,
        caterpie,
        snorlax,
        onix,
        mewtwo
    ]

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
                if(attempt_catch(pokemon, ball)[0]):
                    catches += 1
            successrate = catches/100
            data += [[successrate, pokemon.name, ball]]

    for row in data:
        print(f"{row[0]} for {row[1]} with {row[2]}")
