import pandas as pd
import matplotlib.pyplot as plt

csv_file = "../data/ej1-a.csv"
data = pd.read_csv(csv_file)

group_by = data.groupby('ball')

balls = []
catch_rates = []
std_devs = []

for ball, group_data in group_by:
    balls.append(str(ball))
    catch_rates.append(group_data['catch_rate'].mean())
    std_devs.append(group_data['catch_rate'].std())

plt.errorbar(
    balls,
    catch_rates,
    yerr=std_devs,
    fmt="o",
    label="Catch Rate",
    capsize=5,
)

plt.xlabel("Pokeball")
plt.ylabel("Average Catch Rate")
plt.title("Average Catch Rate for each Pokeball")
plt.grid()
plt.legend()

plt.show()



