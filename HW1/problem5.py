import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import math
import os

df = pd.read_csv(os.getcwd() + "\HW1\PatientData.csv", header=None)
print("# Patients = " + str(len(df)))
print("# Features = " + str(len(df.columns)))
# print(df.head())
print("The first four features seem to be age, sex(0m, 1f), height(cm), and weight(kg).")
for column in df:
    temp = df[column]
    # print(temp)
    temp.replace(to_replace='?', value=None)
    mean = temp.mean()
    temp.fillna(value=mean)