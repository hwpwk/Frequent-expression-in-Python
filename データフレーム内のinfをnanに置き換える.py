import pandas as pd
import numpy as np

# infをnanに置き換える
out_df = out_df.replace([np.inf, -np.inf], np.nan)