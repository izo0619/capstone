# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:53:32 2023

@author: xvssc
"""

#%% Import libraries
import csv
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from scipy.signal import find_peaks

#%% Read in datafile

df = pd.read_csv(r"C:\Users\xvssc\OneDrive - Northwestern University\Capstone\Stiffening\thickStrap.csv")

#%% 

time = df['Time']
sensor_0 = df['Sensor_0']
sensor_1 = df['Sensor_1']
sensor_2 = df['Sensor_2']
sensor_3 = df['Sensor_3']
sensor_4 = df['Sensor_4']
sensor_5 = df['Sensor_5']
sensor_6 = df['Sensor_6']
sensor_7 = df['Sensor_7']
sensor_8 = df['Sensor_8']

#%% plot data 

fig0 = plt.figure("Sensor 0")
plt.plot(time,sensor_0)
plt.title('Sensor 0')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig1 = plt.figure("Sensor 1")
plt.plot(time,sensor_1)
plt.title('Sensor 1')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig2 = plt.figure("Sensor 2")
plt.plot(time,sensor_2)
plt.title('Sensor 2')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig3 = plt.figure("Sensor 3")
plt.plot(time,sensor_3)
plt.title('Sensor 3')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig4 = plt.figure("Sensor 4")
plt.plot(time,sensor_4)
plt.title('Sensor 4')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig5 = plt.figure("Sensor 5")
plt.plot(time,sensor_5)
plt.title('Sensor 5')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig1 = plt.figure("Sensor 6")
plt.plot(time,sensor_6)
plt.title('Sensor 6')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig1 = plt.figure("Sensor 7")
plt.plot(time,sensor_7)
plt.title('Sensor 7')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

fig1 = plt.figure("Sensor 8")
plt.plot(time,sensor_8)
plt.title('Sensor 8')
plt.xlabel('Time [ms]')
plt.ylabel('grams-force (g)')

plt.show()
   
#%% iir filter

from scipy.signal import lfilter
from scipy.signal import filtfilt

mu, sigma = 0, 500
sensor_array_title = ['sensor_0', 'sensor_1', 'sensor_2', 'sensor_3',
                      'sensor_4','sensor_5','sensor_6','sensor_7','sensor_8']
sensor_array = [sensor_0, sensor_1, sensor_2,sensor_3,sensor_4,sensor_5,
                sensor_6, sensor_7, sensor_8]
sensor_hat = []
x = time  # x axis
n = 50
b = [1.0/n]*n
a = 1

for i in range(len(sensor_array)):
    sensor_name = sensor_array_title[i]
    sensor_data = sensor_array[i]   
    y = sensor_data # y axis
    yy= filtfilt(b, a, y)
    yy = 0.00980665*yy
    y = 0.00980665*y
    plt.figure()
    plt.plot(x, yy, linewidth = 0.5, linestyle = "-", c = "b")
  #  plt.plot(x, y, linewidth = 0.5, linestyle = "-", c = "r")
    plt.title('iir Filter ' +str(sensor_name))
    plt.ylabel('Newtons')
    plt.xlabel('Time [ms]')
    sensor_hat.append(yy)
    
#%% PeakFinding and amplitude calculation

all_amplitude_data = []
all_amplitude_time = []

for x in range(len(sensor_array)):
    sensor_name = sensor_array_title[x]
    peak_time = np.asarray(time)
    peak_data = np.asarray(sensor_hat[x])
    peak,_ = find_peaks(peak_data)
    valley_data = peak_data*(-1)
    valley,_ = find_peaks(valley_data)
    peak_data = 0.00980665*peak_data
    plt.scatter(peak_time[peak], peak_data[peak], color = 'orange', s = 5, zorder = 2)
    plt.scatter(peak_time[valley],peak_data[valley],color = 'green', s = 5, zorder = 2)
    plt.plot(peak_time,peak_data, linewidth = 0.5, zorder = 1)
    plt.title('Oscillations with Peaks and Troughs Identified ' + str(sensor_name))
    plt.xlabel('Time [ms]')
    plt.ylabel('Newtons')
    plt.show()
    
    amp_peak = peak[1:len(peak)-1]
    amp_valley = valley

    amplitude = []
    amplitude_time = []

    for i in range(len(amp_peak)):
        value = peak_data[amp_peak[i]] - peak_data[amp_valley[i]]
        amplitude.append(value)
        amplitude_time.append(peak_time[peak][i])

    plt.plot(amplitude_time, amplitude, linewidth = 0.5, color = 'grey')    
    plt.scatter(amplitude_time, amplitude,color = 'red', s = 5, zorder = 2)
    plt.title('Amplitude ' + str(sensor_name))
    plt.xlabel('Time [ms]')
    plt.ylabel('grams_force [g]')
    plt.show()

    all_amplitude_data.append(amplitude)
    all_amplitude_time.append(amplitude_time)
    
    

#%% Calculating Amplitude
import statistics as stat

ave = []
median_val = []

for x in range(len(sensor_array)):
    amplitude_data = all_amplitude_data[x]
    average = np.mean(amplitude_data)
    med = np.median(amplitude_data)
    ave.append(average)
    median_val.append(med)

#%%



