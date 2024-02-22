import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "precipitation_data_2023.csv"

df = pd.read_csv(FILENAME, index_col = 0, usecols = [1, 2, 3, 4, 5], parse_dates = [[0, 1, 2, 3]])
plt.figure(figsize=[12,6])
plt.plot(df)
plt.title("Precipitation data from Lappeenranta Lepola observation station 01/01/2023 - 31/12/2023")
plt.ylabel("Precipitation amount [mm]")
plt.xlabel("Time")
plt.grid(True)
plt.show()
