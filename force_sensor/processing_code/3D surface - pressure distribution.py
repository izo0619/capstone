# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:03:36 2023

@author: xvssc
"""
import pandas as pd
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

#%% CT plots(original)

df_ct = pd.read_csv(r"C:\Users\xvssc\OneDrive - Northwestern University\Capstone\CT final\CT.csv")

med_all_ct = np.array([df_ct['med1'],df_ct['med2'],df_ct['med3']])

med_final_ct = []

for i in range(len(df_ct['med1'])):
    med = np.median(med_all_ct[:,i])
    med_final_ct.append(med)

z_ct = np.array(med_final_ct)
x_ct = np.array([-2, 0, 2, -2, 0, 2, -2, 0, 2])
y_ct = np.array([2, 2, 2, 0, 0, 0, -2, -2, -2])

triang = mtri.Triangulation(x_ct, y_ct)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
    markeredgecolor="black", markersize=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_trisurf(triang, z_ct)
ax.scatter(x_ct,y_ct,z_ct, marker='.', s=10, c="black", alpha=0.5)
ax.set_title('CT Pressure Distribution - Original')
#ax.view_init(elev=60, azim=-45)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

#%% Corset (Original)
df_corset = pd.read_csv(r"C:\Users\xvssc\OneDrive - Northwestern University\Capstone\corset10\corset10_data.csv")

med_all_corset = np.array([df_corset['med0'],df_corset['med1'],df_corset['med2']])
#,
 #                          df_corset['med3'],df_corset['med4'],df_corset['med5'],
  #                         df_corset['med6'],df_corset['med7'],df_corset['med8'],
   #                        df_corset['med9']])

med_final_corset = []

for i in range(len(df_corset['med1'])):
    med = np.median(med_all_corset[:,i])
    med_final_corset.append(med)

z_corset = np.array(med_final_corset)
x_corset = np.array([2, 0, -2, 2, 0, -2, 2, 0, -2])
y_corset = np.array([2, 2, 2, 0, 0, 0, -2, -2, -2])

triang = mtri.Triangulation(x_corset, y_corset)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
    markeredgecolor="black", markersize=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_trisurf(triang, z_corset)
ax.scatter(x_corset,y_corset,z_corset, marker='.', s=10, c="black", alpha=0.5)
ax.set_title('Corset Pressure Distribution - Original')
#ax.view_init(elev=60, azim=-45)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

#%% CT interpolated

fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure = False)
fig.add_axes(ax)

xi_ct= np.linspace(x_ct.min(),x_ct.max(),100)
yi_ct = np.linspace(y_ct.min(),y_ct.max(),100)
zi_ct = griddata((x_ct, y_ct), z_ct, (xi_ct[None,:], yi_ct[:,None]), method='cubic')

xig_ct, yig_ct = np.meshgrid(xi_ct, yi_ct)
surf = ax.plot_surface(xig_ct, yig_ct, zi_ct, cmap = 'Spectral')
fig.colorbar(surf, location = 'left')
ax.set_title('Median Pressure Distribution (CT)', fontsize = 20)
ax.set_xlabel('ML')
ax.set_ylabel('SI')
ax.set_zlabel('grams_force (g)')
ax.set_zlim3d(0,50)
#ax.view_init(30,140)


#%% Corset interpolated

fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure = False)
fig.add_axes(ax)

xi_corset = np.linspace(x_corset.min(),x_corset.max(),100)
yi_corset = np.linspace(y_corset.min(),y_corset.max(),100)
zi_corset = griddata((x_corset, y_corset), z_corset, (xi_corset[None,:], yi_corset[:,None]), method='cubic')

xig_corset, yig_corset = np.meshgrid(xi_corset, yi_corset)

surf = ax.plot_surface(xig_corset, yig_corset, zi_corset, cmap = 'Spectral')
fig.colorbar(surf, location = 'left')
ax.set_title('Median Pressure Distribution (Corset)', fontsize = 20)
ax.set_xlabel('ML')
ax.set_ylabel('SI')
ax.set_zlabel('grams_force (g)')
#ax.set_zlim3d(0,50)
#ax.view_init(30,140)