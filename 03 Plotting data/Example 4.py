
#example 4
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('03 Plotting data/data.csv')

data.set_index('food', inplace=True)

ax = data.plot(kind='bar', stacked=False, zorder=3)

plt.title('Calories and proteins')
plt.xlabel('food')
plt.ylabel('value')
plt.grid(axis='both',color='red',linestyle=":", zorder=0)
plt.xticks(rotation=0, ha='right')

plt.show()