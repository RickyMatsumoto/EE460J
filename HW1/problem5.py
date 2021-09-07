import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import math
import os

df = pd.read_csv(os.getcwd() + "\HW1\PatientData.csv", header=None)
print("# Patients = " + str(len(df)))
print("# Features = " + str(len(df.columns)))
print("The first four features seem to be age, sex(0m, 1f), height(cm), and weight(kg).")
for column in df:
    temp = df[column]
    temp.replace('?', np.nan, inplace=True)
    temp = pd.to_numeric(temp)
    mean = temp.mean()
    temp.replace(np.nan, mean, inplace=True)
    df[column] = temp
print("By plotting different features alongside the patient condition(i.e. x = feature, y = condition), we could find which features correlate the strongest positively/negatively with patient condition by seeing how clutered the points are. From there, we could hypothesize which features impact patient condition the strongest by measuring the correlation, and hopefully be able to predict patient condition by using a combination of those features in the future.")
print("We think that the 3 most important features would be the ones that cluster most strongly in our graphs. We could measure this by finding the average or 'center' of all of our points on each graph, and then finding the average distance from center on each graph, perhaps accounting for outliers.")