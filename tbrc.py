import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mb
import pandas as pd
from scipy import stats
from scipy.stats.stats import pearsonr
import sys
from datetime import datetime
inDir = '/mnt/nas/Research/TBRC/in/'

for filename in os.listdir(inDir):
  print(inDir + filename)
  df = pd.read_csv(inDir + filename)
  Fe_init_per = 0.65
  df.set_value(0,'Fe_per',Fe_init_per*100)
  df['Fe_per'] = df['Fe_per'] *.01
  df['alloy_lb'] = pd.Series(df.iloc[0]['Hopper_lb']*(1-Fe_init_per),index=df.index)
  df['feFeed_lb'] = df['alloy_lb'] * df['Fe_per'] / (1 - df['Fe_per'])
  df['feSlag_lb'] = df.iloc[0]['feFeed_lb'] - df['feFeed_lb']
  outFile = '/mnt/nas/Research/TBRC/out/' + filename
  print(outFile)
  df.to_csv(outFile,index=False)
