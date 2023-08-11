import os
import json
from src.experiments import (
    pokeball_in_ideal_conditions_experiment,
    variating_status_experiment,
    variating_hp_experiment,
    variating_everything_experiment,
)

if __name__ == "__main__":
    config_file = "config.json"

    with open(config_file) as f:
        config = json.load(f)

        # Pokeball in ideal conditions, Ej 1-a
        experiment_config = config["pokeball_in_ideal_conditions_experiment"]
        has_ran = os.path.isfile(experiment_config["csv"])

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Pokeball in ideal conditions Experiment, output file: "
                + experiment_config["csv"]
                + "..."
            )

            pokeball_in_ideal_conditions_experiment(
                output_file=experiment_config["csv"]
            )

        # Status Experiment, Ej 2-a
        experiment_config = config["variating_status_experiment"]
        has_ran = os.path.isfile(experiment_config["csv"])

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Variating Status Experiment, output file: "
                + experiment_config["csv"]
                + "..."
            )

            variating_status_experiment(
                pokemon_name=experiment_config["pokemon"],
                ball=experiment_config["ball"],
                level=experiment_config["level"],
                hp_percentage=experiment_config["hp_percentage"],
                iterations=experiment_config["iterations"],
                output_file=experiment_config["csv"],
            )

        # HP Experiment, Ej 2-b
        experiment_config = config["variating_hp_experiment"]
        has_ran = os.path.isfile(experiment_config["csv"])

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Variating HP Experiment, output file: "
                + experiment_config["csv"]
                + "..."
            )

            variating_hp_experiment(
                pokemon_name=experiment_config["pokemon"],
                ball=experiment_config["ball"],
                noise=experiment_config["noise"],
                iterations=experiment_config["iterations"],
                output_file=experiment_config["csv"],
            )

        # Everything Experiment, Ej 2-d
        experiment_config = config["variating_everything_experiment"]
        has_ran = os.path.isfile(experiment_config["csv"])

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Variating Everything Experiment, output file: "
                + experiment_config["csv"]
                + "..."
            )

            variating_everything_experiment(
                pokemon_name=experiment_config["pokemon"],
                iterations=experiment_config["iterations"],
                output_file=experiment_config["csv"],
            )
