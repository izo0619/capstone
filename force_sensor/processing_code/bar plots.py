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
df_corset = pd.read_csv(r"processing_code/corset10_data.csv")
df_CT = pd.read_csv(r"processing_code/CT.csv")
df_board = pd.read_csv(r"processing_code/board3_data.csv")

corset_median = []
med_all_corset = np.array([df_corset['ave0'],df_corset['ave1'],df_corset['ave2']])
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
med_all_ct = np.array([df_CT['ave0'],df_CT['ave1'],df_CT['ave2']])

for i in range(len(df_CT['ave1'])):
    med = np.mean(med_all_ct[:,i])
    ct_median.append(med)
    
ct_err = []
ct_median = np.array(ct_median)
ct_err = []
for i in range(len(ct_median)):
    ct_std =  np.std(med_all_ct[:,i])   
    ct_err.append(ct_std/(3**(1/2)))

board_median = []
med_all_board = np.array([df_board['ave0'],df_board['ave1'],df_board['ave2']])

for i in range(len(df_board['ave1'])):
    med = np.mean(med_all_board[:,i])
    board_median.append(med)
    
board_err = []
board_median = np.array(board_median)
board_err = []
for i in range(len(board_median)):
    board_std =  np.std(med_all_board[:,i])   
    board_err.append(board_std/(3**(1/2)))




n=9
r = np.arange(n)
width = 0.2
labels_x = ['s0','s1','s2','s3','s4','s5','s6','s7','s8']
plt.figure()
plt.bar(r,ct_median, yerr = ct_err, width = 0.2, color = 'blue')
plt.bar(r + width,corset_median,yerr=corset_err, width = 0.2, color = 'red')
plt.bar(r + width*2,board_median, yerr = board_err, width = 0.2, color = 'green')
plt.axhline(y=0, color = 'black')
plt.xticks(r + width/2, labels_x)
plt.ylabel('grams_force [g]')
plt.xlabel('Sensor')
plt.title('Average Amplitude')
colors = {'CT':'blue', 'Corset':'red', 'Board':'green'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.savefig('Average Amplitude.png')
plt.show()


