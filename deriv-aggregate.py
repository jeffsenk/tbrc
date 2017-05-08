import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mb
import pandas as pd
from scipy import stats
from scipy.stats.stats import pearsonr
import sys
from datetime import datetime
inDir = '/mnt/nas/Research/TBRC/derivOut/'

obs =[]

for filename in os.listdir(inDir):
  print(inDir + filename)
  df = pd.read_csv(inDir + filename)
  firstRow = True
  for i in range(1,len(df)):
    if df.iloc[i]['feSlag_lb']>0 :
      if firstRow :
        #drop first row
        firstRow = False
      else:
        obs.append([df.iloc[i]['O2_lb'],df.iloc[i]['feSlag_lb'],df.iloc[i]['O2_chg'],df.iloc[i]['feSlag_chg'],filename])
df = pd.DataFrame(obs,columns=['O2_lb','feSlag_lb','O2_chg','feSlag_chg','Date'])
outFile = '/mnt/nas/Research/TBRC/combined/derivAggregated.csv'
df.to_csv(outFile,index=False)
