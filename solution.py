import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 440117284 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
     t_stat, p_value = ttest_ind(x, y)
    return p_value < 0.07 # Ваш ответ, True или False
