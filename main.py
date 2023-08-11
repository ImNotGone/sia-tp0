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
        data_path = config["data_path"]["path"]

        if not os.path.exists(data_path):
            os.mkdir(data_path)

        # Pokeball in ideal conditions, Ej 1-a
        experiment_config = config["pokeball_in_ideal_conditions_experiment"]
        output_path = os.path.join(data_path, experiment_config["csv"])
        has_ran = os.path.isfile(output_path)

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Pokeball in ideal conditions Experiment, output file: "
                + output_path
                + "..."
            )

            pokeball_in_ideal_conditions_experiment(
                output_file=output_path
            )

        # Status Experiment, Ej 2-a
        experiment_config = config["variating_status_experiment"]
        output_path = os.path.join(data_path, experiment_config["csv"])
        has_ran = os.path.isfile(output_path)

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Variating Status Experiment, output file: "
                + output_path
                + "..."
            )

            variating_status_experiment(
                pokemon_name=experiment_config["pokemon"],
                ball=experiment_config["ball"],
                level=experiment_config["level"],
                hp_percentage=experiment_config["hp_percentage"],
                iterations=experiment_config["iterations"],
                output_file=output_path,
            )

        # HP Experiment, Ej 2-b
        experiment_config = config["variating_hp_experiment"]
        output_path = os.path.join(data_path, experiment_config["csv"])
        has_ran = os.path.isfile(output_path)

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Variating HP Experiment, output file: "
                + output_path
                + "..."
            )

            variating_hp_experiment(
                pokemon_name=experiment_config["pokemon"],
                ball=experiment_config["ball"],
                noise=experiment_config["noise"],
                iterations=experiment_config["iterations"],
                output_file=output_path,
            )

        # Everything Experiment, Ej 2-d
        experiment_config = config["variating_everything_experiment"]
        output_path = os.path.join(data_path, experiment_config["csv"])
        has_ran = os.path.isfile(output_path)

        if not has_ran or experiment_config["rerun"]:
            print(
                "Running Variating Everything Experiment, output file: "
                + output_path
                + "..."
            )

            variating_everything_experiment(
                pokemon_name=experiment_config["pokemon"],
                iterations=experiment_config["iterations"],
                output_file=output_path,
            )
