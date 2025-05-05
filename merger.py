import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

tackles = pd.read_csv('tackles.csv')
players = pd.read_csv('players.csv')

tackles_new = pd.merge(tackles, players, on=['nflId'])

# Keep only the 'tackle' and 'displayName' columns
tackles_new = tackles_new[['tackle', 'displayName', 'nflId']]

print(tackles_new)
# Assuming your DataFrame is called 'your_dataframe'

# Group by the 'displayName' column and sum the 'value' column
summed_df = tackles_new.groupby(['nflId', 'displayName'])['tackle'].sum().reset_index()


# Print or use the resulting DataFrame
summed_df.to_csv('tackles_new.csv')

