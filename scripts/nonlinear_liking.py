import pandas as pd
import numpy as np

def nonlinear_liking(prod, age, X_df, noise_sd=0.5, random_seed=None):
    """
      - younger people (<=25): strong sweetness liking, bitterness disliked, with a small inverted-U sweet nonlinearity.
      - older people (>25): sweetness still positive but less intense, bitterness becomes liked.
    """
    if random_seed is not None:
        rng = np.random.RandomState(random_seed)
    else:
        rng = np.random

    sweet   = float(X_df.loc[prod, 'sweetness'])
    bitter  = float(X_df.loc[prod, 'bitterness'])
    crunchy = float(X_df.loc[prod, 'crunchy'])

    # younger (18–25)
    if age <= 25:
        liking = (
            1.2 * sweet              # strong sweet liking
            - 0.3 * bitter           # bitterness disliked
            + 0.6 * crunchy          # crunchy positive
            - 0.4 * (sweet ** 2)     # inverted-U sweetness (non-linear)
            + rng.normal(0, noise_sd)   # add some noise
        )

    # older (>25)
    else:
        liking = (
            0.9 * sweet                # sweet liked, but not as much as younger people
            + 0.2 * bitter                # bitterness becomes liked
            + 0.6 * crunchy               # crunchy liked equally
            + rng.normal(0, noise_sd)     # add some noise
        )

    return liking
