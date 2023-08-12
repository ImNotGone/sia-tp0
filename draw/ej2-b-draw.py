import pandas as pd
import matplotlib.pyplot as plt

csv_file = "../data/ej2-b.csv"
data = pd.read_csv(csv_file)

hp_values = data["hp_percentage"]
average_values = data["catch_rate"]
std_dev_values = data["std"]

plt.errorbar(
    hp_values,
    average_values,
    yerr=std_dev_values,
    fmt="o",
    label="Catch Rate",
    capsize=5,
)
plt.xlabel("HP")
plt.ylabel("Average Catch Rate")
plt.title("Average Catch Rate vs. HP with Standard Deviation")
plt.legend()
plt.grid()

# Reverse x-axis
plt.xlim(max(hp_values), 1)

plt.show()