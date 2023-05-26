# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:48:59 2023

@author: Luca Rosignoli
Script to red a tms run and plot the pose evolution (x,y,z,rx,rx,rz) and their corrections.
"""


from tms_data_new import tms_data
import matplotlib.pyplot as plt
import os
import numpy as np

path = 'C:/Users/rodeghiero/Desktop/LBT_TMS/Etalon_run'
timestamp = '20230510'

#Load data
tms_run = tms_data(path, timestamp)

#pose sx plots
id_ref = tms_run.data['pose.sx']['#timestamp'][tms_run.data['pose.sx']['#timestamp']
                                               == tms_run.data['ref.sx']['#timestamp'][0]
                                               ].index[0]
posesx_ref = tms_run.data['pose.sx'][tms_run.data['pose.sx']['#timestamp'] ==
                                     tms_run.data['ref.sx']['#timestamp'][0]]

fig, axs = plt.subplots(2, 3, tight_layout=True)
fig.suptitle('LEFT', fontweight='bold')

for i, key in enumerate(zip(tms_run.data['pose.sx'].columns[1:],
                            tms_run.data['correction.sx'].columns[1:])):
    if i <= 2: 
        j = 0
        k = i
    else: 
        j = 1
        k = i-3
    axs[j, k].scatter(tms_run.data['pose.sx']['#timestamp'][id_ref+1:],
               tms_run.data['pose.sx'][key[0]][id_ref+1:].values-posesx_ref[key[0]].values[0],
               marker='x',
               s=1,
               c='blue',
               label = 'Pose')
    if key[0] == 'z':
        axs[j, k].scatter(np.arange(id_ref, len(tms_run.data['correction.sx'][key[1]])),
                   tms_run.data['correction.sx'][key[1]][id_ref:]+
                   tms_run.data['thermalz4.sx']['thermal_z4'][id_ref:],
                   marker='x',
                   s=1,
                   c='red',
                   label = 'Correction+ZTh')
    else:
        axs[j, k].scatter(np.arange(id_ref, len(tms_run.data['correction.sx'][key[1]])),
                   tms_run.data['correction.sx'][key[1]][id_ref:],
                   marker='x',
                   s=1,
                   c='red',
                   label = 'Correction') 
    axs[j, k].xaxis.set_major_locator(plt.MaxNLocator(5))
    axs[j, k].set_xticks([])
    axs[j, k].set_title(f'{key[0]}', fontweight='semibold')
    axs[j, k].set_xlabel('Time')
    if j == 0:
        axs[j, k].set_ylabel('Deviation mm')
    else:
        axs[j, k].set_ylabel('Deviation arcsec')
    axs[j, k].legend(fontsize='xx-small')
    
plt.savefig(os.path.join(path, f'plots/{timestamp}_sx_plots.png'), dpi=1000)

#pose dx plots
id_ref = tms_run.data['pose.dx']['#timestamp'][tms_run.data['pose.dx']['#timestamp']
                                               == tms_run.data['ref.dx']['#timestamp'][0]
                                               ].index[0]
posedx_ref = tms_run.data['pose.dx'][tms_run.data['pose.dx']['#timestamp'] ==
                                     tms_run.data['ref.dx']['#timestamp'][0]]

fig, axs = plt.subplots(2, 3, tight_layout=True)
fig.suptitle('RIGHT', fontweight='bold')

for i, key in enumerate(zip(tms_run.data['pose.dx'].columns[1:],
                            tms_run.data['correction.dx'].columns[1:])):
    if i <= 2: 
        j = 0
        k = i
    else: 
        j = 1
        k = i-3
    axs[j, k].scatter(tms_run.data['pose.dx']['#timestamp'][id_ref+1:],
               tms_run.data['pose.dx'][key[0]][id_ref+1:].values-posedx_ref[key[0]].values[0],
               marker='x',
               s=1,
               c='blue',
               label = 'Pose')
    if key[0] == 'z':
        axs[j, k].scatter(np.arange(id_ref, len(tms_run.data['correction.dx'][key[1]])),
                   tms_run.data['correction.dx'][key[1]][id_ref:]+
                   tms_run.data['thermalz4.dx']['thermal_z4'][id_ref:],
                   marker='x',
                   s=1,
                   c='red',
                   label = 'Correction+ZTh')
    else:
        axs[j, k].scatter(np.arange(id_ref, len(tms_run.data['correction.dx'][key[1]])),
                   tms_run.data['correction.dx'][key[1]][id_ref:],
                   marker='x',
                   s=1,
                   c='red',
                   label = 'Correction') 
    axs[j, k].xaxis.set_major_locator(plt.MaxNLocator(5))
    axs[j, k].set_xticks([])
    axs[j, k].set_title(f'{key[0]}', fontweight='semibold')
    axs[j, k].set_xlabel('Time')
    if j == 0:
        axs[j, k].set_ylabel('Deviation mm')
    else:
        axs[j, k].set_ylabel('Deviation arcsec')
    axs[j, k].legend(fontsize='xx-small')
    
plt.savefig(os.path.join(path, f'plots/{timestamp}_dx_plots.png'), dpi=1000)

