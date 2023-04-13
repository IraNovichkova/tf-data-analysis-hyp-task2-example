import pandas as pd
import numpy as np
from scipy import stats


chat_id = 335933917

def solution(x: np.array, y: np.array) -> bool:
    x = x.ravel()
    y = y.ravel()
    p = 0.06
    if (stats.ks_2samp(x, y).pvalue > p):
        return False
    else:
        return True
