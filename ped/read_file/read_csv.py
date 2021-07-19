import pandas as pd

def getXY(data: pd.DataFrame):    
    num_person = len(data.columns) - 1
    last_time_unit = data.iloc[-1,0]
    return num_person, last_time_unit

def person_idx_list(data: pd.DataFrame):
    return data.columns[1:]


def get_person_info(columns: pd.Index):
    pass