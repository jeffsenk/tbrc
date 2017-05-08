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

for filename in os.listdir(inDir):
  #read in
  print(inDir + filename)
  df = pd.read_csv(inDir + filename)
  #fill in empties
  df.set_value(0,'O2_lb',0)
  df.set_value(0,'Heat_BTU',0)
#  df['feFeed_lb'] = df['feFeed_lb'].fillna(method='ffill')
#  df['feSlag_lb'] = df['feSlag_lb'].fillna(method='ffill')
  #1st deriv
#  df['Heat_1step'] = df['Heat_BTU'].diff()
#  df['O2_1step'] = df['O2_lb'].diff()
#  df['feSlag_1step'] = df['feSlag_lb'].diff()
#  df.set_value(0,'Heat_1step',0)
#  df.set_value(0,'O2_1step',0)
#  df.set_value(0,'feSlag_1step',0)
  #chg
  feSlag = 0
  O2 = 0
  Heat = 0
  for i in range(1,len(df)):
    feSlag_last = df.iloc[i]['feSlag_lb']
    O2_last = df.iloc[i]['O2_lb']
    Heat_last = df.iloc[i]['Heat_BTU']
    if feSlag_last >0 :
      df.set_value(i,'Heat_chg',Heat_last - Heat)
      df.set_value(i,'O2_chg',O2_last - O2)
      df.set_value(i,'feSlag_chg',feSlag_last - feSlag)
      feSlag = feSlag_last
      O2 = O2_last
      Heat = Heat_last

  #remove unwanted columns
  df = df.drop('Hopper_lb',axis=1)
  df = df.drop('Fe_per',axis=1)
  #print
  outFile = '/mnt/nas/Research/TBRC/derivOut/' + filename
  print(outFile)
  df.to_csv(outFile,index=False)
