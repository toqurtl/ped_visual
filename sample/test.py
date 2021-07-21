from ped.read_file import read_group
from ped.analysis import basic
import os
import pandas as pd
import numpy as np

alone_folder_path = os.path.abspath("C:\\Users\\yoon9\\data\\ped_texas\\origin\\alone")
same_folder_path = os.path.abspath("C:\\Users\\yoon9\\data\\ped_texas\\origin\\same")
opossite_folder_path = os.path.abspath("C:\\Users\\yoon9\\data\\ped_texas\\origin\\opossite")

available_alone_folder_list = read_group.available_scene_list(alone_folder_path)
available_same_folder_list = read_group.available_scene_list(same_folder_path)
available_opossite_folder_list = read_group.available_scene_list(opossite_folder_path)

print("analyze alone")
alone = basic.to_pandas(available_alone_folder_list, group_name="alone")
print("analyze alone_5")
alone_5 = basic.to_pandas_interval(available_alone_folder_list, 5, group_name="alone_5")
print("analyze alone_10")
alone_10 = basic.to_pandas_interval(available_alone_folder_list, 10, group_name="alone_10")
alone.to_excel("alone.xlsx")
alone_5.to_excel("alone_5.xlsx")
alone_10.to_excel("alone_10.xlsx")

print("analyze opossite")
opossite = basic.to_pandas(available_opossite_folder_list, group_name="opossite")
print("analyze opossite_5")
opossite_5 = basic.to_pandas_interval(available_opossite_folder_list, 5, group_name="opossite_5")
print("analyze opossite_10")
opossite_10 = basic.to_pandas_interval(available_opossite_folder_list, 10, group_name="opossite_10")
opossite.to_excel("opossite.xlsx")
opossite_5.to_excel("opossite_5.xlsx")
opossite_10.to_excel("opossite_10.xlsx")


print("analyze same")
same = basic.to_pandas(available_same_folder_list, group_name="same")
print("analyze same_5")
same_5 = basic.to_pandas_interval(available_same_folder_list, 5, group_name="same_5")
print("analyze same_10")
same_10 = basic.to_pandas_interval(available_same_folder_list, 10, group_name="same_10")
same.to_excel("same.xlsx")
same_5.to_excel("same_5.xlsx")
same_10.to_excel("same_10.xlsx")
