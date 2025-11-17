import pandas as pd
import numpy as np


def linear_liking(prod, age, X_df):
    liking = (
    0.5 * X_df.loc[prod, 'sweetness'] # sweetness is liked
    - 0.4 * X_df.loc[prod, 'bitterness'] # bitterness is not liked
    - 0.2 * X_df.loc[prod, 'astringency'] # astringency is not liked
    + 0.02 * (75 - age)  # younger gets a boost
    + np.random.normal(0, 0.5) # noise
    )
    return liking
