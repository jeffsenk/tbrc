import os
import numpy as np
import pandas as pd
import sys
from datetime import datetime
inDir = '/mnt/nas/Research/TBRC/in/'

for filename in os.listdir(inDir):
  print(inDir + filename)
  df = pd.read_csv(inDir + filename)
  newDf = df.drop(['alloy_lb','feFeed_lb','feSlag_lb'],axis=1)
  newDf.set_value(0,'Fe_per',0)
  outFile = '/mnt/nas/Research/TBRC/raw-in/' + filename
  print(outFile)
  newDf.to_csv(outFile,index=False)
