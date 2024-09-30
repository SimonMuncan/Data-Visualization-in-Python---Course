#Example 1
import pandas as pd

data = pd.read_csv('02 Data manipulation/data.csv')

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 


#Example 2
import pandas as pd

data = pd.read_csv('02 Data manipulation/data.csv')

print(data) 

#Example 3
import pandas as pd

data = pd.read_csv('02 Data manipulation/data.csv')

data_to_displey = ["burger","fries"]

data_fil = data[data["food"].isin(data_to_displey)]

print(data_fil.sort_values("calories",ascending=True))

