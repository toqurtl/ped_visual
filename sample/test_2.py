from ped.read_file import read_group
from ped.analysis import basic
import os
import pandas as pd
import numpy as np

def forward(file_name):
    df = pd.read_excel(file_name)
    cond_1 = df['d_mean'] > 0
    cond_2 = df['v_mean_avg'] < 100
    return df[cond_1 & cond_2]

def backward(file_name):
    df = pd.read_excel(file_name)
    cond_1 = df['d_mean'] < 0
    cond_2 = df['v_mean_avg'] < 100
    return df[cond_1 & cond_2]
    

def get_list(df: pd.DataFrame):
    return [
        df["v_mean"].to_numpy().mean(),
        df["v_std"].to_numpy().mean(),
        df["a_mean"].to_numpy().mean(),
        df["a_std"].to_numpy().mean(),
        df["d_mean"].to_numpy().mean(),
        df["d_std"].to_numpy().mean(),
        df["v_mean_avg"].to_numpy().mean(),
        df["d_mean_avg"].to_numpy().mean()
    ]
    
file_list = ["alone", "same", "opossite", "alone_5", "same_5", "opossite_5", "alone_10", "same_10", "opossite_10"]

data = {}

for f in file_list:
    data[f+"_forward"] = forward(f+".xlsx")

for f in file_list:
    data[f+"_backward"] = backward(f+".xlsx")

result_data = {}

for key, values in data.items():
    result_data[key] = get_list(values)

columns = ["v_mean", "v_std", "a_mean", "a_std", "d_mean", "d_std", "v_mean_avg", "d_mean_avg"]

test = pd.DataFrame.from_dict(result_data, orient="index", columns=columns)
test.to_excel("compare.xlsx")
