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

plt.rcParams['figure.figsize'] = [12, 8]

#%% CT plots(original)

df_ct = pd.read_csv("processing_code/CT.csv")

agg_all_ct = np.array([df_ct['ave0'],df_ct['ave1'],df_ct['ave2']])

agg_final_ct = []

for i in range(len(df_ct['ave0'])):
    agg = np.mean(agg_all_ct[:,i])
    agg_final_ct.append(agg)

z_ct = np.array(agg_final_ct)
x_ct = np.array([-2, 0, 2, -2, 0, 2, -2, 0, 2])
y_ct = np.array([2, 2, 2, 0, 0, 0, -2, -2, -2])

triang = mtri.Triangulation(x_ct, y_ct)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
    markeredgecolor="black", markersize=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
# plt.show()
plt.close()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_trisurf(triang, z_ct)
ax.scatter(x_ct,y_ct,z_ct, marker='.', s=10, c="black", alpha=0.5)
ax.set_title('CT Pressure Distribution - Original')
#ax.view_init(elev=60, azim=-45)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# plt.show()
plt.close()

#%% Corset (Original)
df_corset = pd.read_csv("processing_code/corset10_data.csv")

agg_all_corset = np.array([df_corset['ave0'],df_corset['ave1'],df_corset['ave2']])
agg_final_corset = []

for i in range(len(df_corset['ave1'])):
    agg = np.mean(agg_all_corset[:,i])
    agg_final_corset.append(agg)

z_corset = np.array(agg_final_corset)
x_corset = np.array([-2, 0, 2, -2, 0, 2, -2, 0, 2])
y_corset = np.array([2, 2, 2, 0, 0, 0, -2, -2, -2])

triang = mtri.Triangulation(x_corset, y_corset)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
    markeredgecolor="black", markersize=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
# plt.show()
plt.close()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_trisurf(triang, z_corset)
ax.scatter(x_corset,y_corset,z_corset, marker='.', s=10, c="black", alpha=0.5)
ax.set_title('Corset Pressure Distribution - Original')
#ax.view_init(elev=60, azim=-45)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# plt.show()
plt.close()

#%% board (Original)
df_board = pd.read_csv("processing_code/board3_data.csv")

agg_all_board = np.array([df_board['ave0'],df_board['ave1'],df_board['ave2']])
agg_final_board = []

for i in range(len(df_board['ave1'])):
    agg = np.mean(agg_all_board[:,i])
    agg_final_board.append(agg)

z_board = np.array(agg_final_board)
x_board = np.array([-2, 0, 2, -2, 0, 2, -2, 0, 2])
y_board = np.array([2, 2, 2, 0, 0, 0, -2, -2, -2])

#%% CT interpolated
ax = plt.axes(projection='3d')

xi_ct= np.linspace(x_ct.min(),x_ct.max(),100)
yi_ct = np.linspace(y_ct.min(),y_ct.max(),100)
zi_ct = griddata((x_ct, y_ct), z_ct, (xi_ct[None,:], yi_ct[:,None]), method='cubic')

xig_ct, yig_ct = np.meshgrid(xi_ct, yi_ct)
surf = ax.plot_surface(xig_ct, yig_ct, zi_ct, cmap = 'Spectral')
fig.colorbar(surf, location = 'left')
ax.set_title('Mean Force Distribution (CT)', fontsize = 20)
ax.set_xlabel('ML')
ax.set_ylabel('SI')
ax.set_zlabel('grams_force (g)')
# ax.set_zlim3d(0,50)
# ax.view_init(30,140)
plt.savefig('CT_interpolated.png')
plt.show()


#%% Corset interpolated

# fig = plt.figure()
ax = plt.axes(projection='3d')
# ax = Axes3D(fig, auto_add_to_figure = False)
# fig.add_axes(ax)

xi_corset = np.linspace(x_corset.min(),x_corset.max(),100)
yi_corset = np.linspace(y_corset.min(),y_corset.max(),100)
zi_corset = griddata((x_corset, y_corset), z_corset, (xi_corset[None,:], yi_corset[:,None]), method='cubic')

xig_corset, yig_corset = np.meshgrid(xi_corset, yi_corset)

surf = ax.plot_surface(xig_corset, yig_corset, zi_corset, cmap = 'Spectral')
fig.colorbar(surf, location = 'left')
ax.set_xlabel('ML')
ax.set_ylabel('SI')
ax.set_zlabel('grams_force (g)')
ax.set_title('Mean Force Distribution (Corset)', fontsize = 20)
# ax.set_zlim3d(0,50)
# ax.view_init(30,140)
plt.savefig('Corset_interpolated.png')
plt.show()

#%% board interpolated

# fig = plt.figure()
ax = plt.axes(projection='3d')

xi_board = np.linspace(x_board.min(),x_board.max(),100)
yi_board = np.linspace(y_board.min(),y_board.max(),100)
zi_board = griddata((x_board, y_board), z_board, (xi_board[None,:], yi_board[:,None]), method='cubic')

xig_board, yig_board = np.meshgrid(xi_board, yi_board)

surf = ax.plot_surface(xig_board, yig_board, zi_board, cmap = 'Spectral')
fig.colorbar(surf, location = 'left')
ax.set_xlabel('ML')
ax.set_ylabel('SI')
ax.set_zlabel('grams_force (g)')
ax.set_title('Mean Force Distribution (Board)', fontsize = 20)
# ax.set_zlim3d(0,50)
# ax.view_init(30,140)
plt.savefig('Board_interpolated.png')
plt.show()