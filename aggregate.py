import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mb
import pandas as pd
from scipy import stats
from scipy.stats.stats import pearsonr
import sys
from datetime import datetime
inDir = '/mnt/nas/Research/TBRC/out/'

obs =[]

for filename in os.listdir(inDir):
  print(inDir + filename)
  df = pd.read_csv(inDir + filename)
  for i in range(1,len(df)):
    if df.iloc[i]['feSlag_lb']>0 :
      obs.append([df.iloc[i]['O2_lb'],df.iloc[i]['Heat_BTU'],df.iloc[i]['feSlag_lb']])

df = pd.DataFrame(obs,columns=['O2_lbs','Heat_BTU','feSlag_lbs'])
outFile = '/mnt/nas/Research/TBRC/combined/aggregated.csv'
df.to_csv(outFile,index=False)
