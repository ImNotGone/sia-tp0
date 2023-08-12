import pandas as pd
import matplotlib.pyplot as plt

csv_file = "data/ej2-a.csv"
data = pd.read_csv(csv_file)

status = data["status"]
catch_rate = data["catchRate"]


plt.bar(status, catch_rate)

for i, value in enumerate(catch_rate):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.xlabel("Status Effect")
plt.ylabel("Catch Rate")
plt.title("Catch Rate and Status Effect")


plt.show()
