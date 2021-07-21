from ped.read_file import read_group
from ped.analysis import basic
import os
import pandas as pd
import numpy as np

# opossite = pd.read_excel("opossite.xlsx")
# alone = pd.read_excel("alone.xlsx")
# cond = opossite['d_mean'] > 0 
# opossite = opossite[cond]
# cond_1 = alone['d_mean'] > 0
# cond_2 = alone['v_mean_avg'] < 100
# alone = alone[cond_1 & cond_2]

# print("v_mean: ", opossite["v_mean"].to_numpy().mean(), alone["v_mean"].to_numpy().mean())
# print("v_std: ", opossite["v_std"].to_numpy().mean(), alone["v_std"].to_numpy().mean())
# print("a_mean: ", opossite["a_mean"].to_numpy().mean(), alone["a_mean"].to_numpy().mean())
# print("a_std: ", opossite["a_std"].to_numpy().mean(), alone["a_std"].to_numpy().mean())
# print("d_mean: ", opossite["d_mean"].to_numpy().mean(), alone["d_mean"].to_numpy().mean())
# print("d_std: ", opossite["d_std"].to_numpy().mean(), alone["d_std"].to_numpy().mean())
# print("v_mean_avg: ", opossite["v_mean_avg"].to_numpy().mean(), alone["v_mean_avg"].to_numpy().mean())
# print("d_mean_avg: ", opossite["d_mean_avg"].to_numpy().mean(), alone["d_mean_avg"].to_numpy().mean())


opossite = pd.read_excel("opossite_5.xlsx")
alone = pd.read_excel("alone_5.xlsx")
cond = opossite['d_mean'] > 0 
opossite = opossite[cond]
cond_1 = alone['d_mean'] > 0
# cond_2 = alone['v_mean_avg'] < 100
alone = alone[cond_1]

print("v_mean: ", opossite["v_mean"].to_numpy().mean(), alone["v_mean"].to_numpy().mean())
print("v_std: ", opossite["v_std"].to_numpy().mean(), alone["v_std"].to_numpy().mean())
print("a_mean: ", opossite["a_mean"].to_numpy().mean(), alone["a_mean"].to_numpy().mean())
print("a_std: ", opossite["a_std"].to_numpy().mean(), alone["a_std"].to_numpy().mean())
print("d_mean: ", opossite["d_mean"].to_numpy().mean(), alone["d_mean"].to_numpy().mean())
print("d_std: ", opossite["d_std"].to_numpy().mean(), alone["d_std"].to_numpy().mean())
print("v_mean_avg: ", opossite["v_mean_avg"].to_numpy().mean(), alone["v_mean_avg"].to_numpy().mean())
print("d_mean_avg: ", opossite["d_mean_avg"].to_numpy().mean(), alone["d_mean_avg"].to_numpy().mean())


