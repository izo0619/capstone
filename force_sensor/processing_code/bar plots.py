# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:35:26 2023

@author: xvssc
"""
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from scipy.signal import find_peaks

#%% One plot
df_corset = pd.read_csv(r"C:\Users\xvssc\OneDrive - Northwestern University\Capstone\corset10\corset10_data.csv")
df_CT = pd.read_csv(r"C:\Users\xvssc\OneDrive - Northwestern University\Capstone\CT final\CT.csv")

corset_median = []
med_all_corset = np.array([df_corset['med0'],df_corset['med1'],df_corset['med2']])
#,
 #                          df_corset['med3'],df_corset['med4'],df_corset['med5'],
  #                         df_corset['med6'],df_corset['med7'],df_corset['med8'],
   #                        df_corset['med9']])
for i in range(len(df_corset['ave1'])):
    med = np.mean(med_all_corset[:,i])
    corset_median.append(med)
    
corset_median = np.array(corset_median)

corset_err = []
for i in range(len(corset_median)):
    corset_std =  np.std(med_all_corset[:,i])   
    corset_err.append(corset_std/(3**(1/2)))


ct_median = []
med_all_ct = np.array([df_CT['ave1'],df_CT['ave2'],df_CT['ave3']])

for i in range(len(df_CT['ave1'])):
    med = np.mean(med_all_ct[:,i])
    ct_median.append(med)
    
ct_err = []
ct_median = np.array(ct_median)
ct_err = []
for i in range(len(ct_median)):
    ct_std =  np.std(med_all_ct[:,i])   
    ct_err.append(ct_std/(3**(1/2)))


n=9
r = np.arange(n)
width = 0.2
labels_x = ['s0','s1','s2','s3','s4','s5','s6','s7','s8']
plt.figure()
plt.bar(r,corset_median,yerr=corset_err, width = 0.2, color = 'red')
plt.bar(r + width,ct_median, yerr = ct_err, width = 0.2, color = 'blue')
plt.axhline(y=0, color = 'black')
plt.xticks(r + width/2, labels_x, fontsize = 30)
plt.ylabel('grams_force [g]', fontsize = 30)
plt.xlabel('Sensor', fontsize = 30)
plt.title('Average Amplitude', fontsize = 50)
colors = {'Corset':'red', 'CT':'blue'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.yticks(fontsize = 30)
plt.legend(handles, labels, fontsize = 30)

