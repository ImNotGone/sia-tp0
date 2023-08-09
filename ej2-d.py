import csv
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

output_file = "ej2-d.csv"
pokemon_name = "caterpie"
catch_attempts = 100

factory = PokemonFactory("pokemon.json")
pokemon = factory.create(pokemon_name, 1, StatusEffect.NONE, 1)

status = [StatusEffect.BURN, StatusEffect.SLEEP, StatusEffect.POISON, StatusEffect.FREEZE, StatusEffect.PARALYSIS]
balls = ["pokeball", "ultraball", "fastball", "heavyball"]

header = ["pokemon", "status_effect", "hp", "level", "pokeball", "success_rate"]
data = []

for stat in status:
    pokemon.status_effect = stat
    for current_hp in range(1, pokemon.max_hp):
        pokemon.current_hp = current_hp
        for current_lvl in range(1, 100):
            pokemon.level = current_lvl
            for ball in balls:
                catches = 0
                for _ in range(catch_attempts):
                    if attempt_catch(pokemon, ball)[0]:
                        catches += 1
                success_rate = catches / catch_attempts
                data += [[pokemon.name, stat.name, current_hp, current_lvl, ball, success_rate]]

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)