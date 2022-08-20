import pandas as pd
import json
from pandas import json_normalize
import matplotlib.pyplot as plt

with open('TPE.json') as f:
    dict = json.loads(f.read()) 

def dataparser(datatype,target):

    tag_dict = {"c:125":['TPE_region','Taipei','NTPE','TPE_YoY'],"c:151":['Tainan','Taipei','NewTaipei','CHU','KHH','HSC','Taiwan']}

    df = pd.json_normalize(dict['data'][datatype],record_path='s')
    df = df.transpose()
    df.columns = tag_dict[datatype]
    df = df[target]
    '''Split list into Date and Index'''
    df = pd.DataFrame(df.dropna().to_list(),columns=['Date','Index'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Index'] = pd.to_numeric(df['Index'])
    return df

class Price:
    def __init__(self,datatype,target):
        self.df = dataparser(datatype,target)
        self.target = target
        self.source = datatype
