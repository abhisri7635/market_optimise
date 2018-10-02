import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transact=[]
for i in range(0,7501):
    transact.append([str(data.values[i,j]) for j in range(0,20)])
from apyori import apriori
rules=apriori(transact,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2)
result=list(rules)
