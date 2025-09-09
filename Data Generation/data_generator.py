#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:10:10 2020

@author: rajs
desc: Inspired from Sairam Numpy Version (pke.py)
"""


import numpy as np
from waveforms import gen_inputs, plot
from pke_model import pke
import os
import glob

"""
generate reactivity sequence
"""

# Tsim, dt = 100, 50e-03
# rhos = gen_inputs(Tsim/dt, events = [0, 0.2, 0.3, 0.6, 0.8], values = [0, -1e-3, -2e-3, -1e-3, 0])()
# Tsim, dt = 100, 50e-03
# rhos.extend(gen_inputs(Tsim/dt, shape = 'step', events = [0, 0.2, 0.3, 0.6, 0.8], values = [0, -1e-3, -2e-3, -1e-3, 0])())
# Tsim, dt = 100, 50e-03
# rhos.extend(gen_inputs(Tsim/dt, shape = 'triangle', events = [0, 0.2, 0.3, 0.6, 0.8], values = [0, 0, -1e-3, -2e-3, -1e-3])())
# Tsim, dt = 10, 50e-03
# rhos.extend(gen_inputs(Tsim/dt, shape = 'sine', events = [0, 0.5, 1], values = [[1e-3, 1, 0, -1e-3, dt],
#                                                                                 [2e-3, 1, 0, -2e-3, dt]])())

save_dir = './pke_data/'
last_file_idx = -1
try:
    os.mkdir(save_dir)    
except FileExistsError:
    try:
        last_file_idx = int(sorted(glob.glob(save_dir + '*.txt'))[-1].strip('.txt').strip(save_dir))
    except IndexError:
        pass

print('1')
Tsim, dt = 100, 50e-03
cnt = last_file_idx + 1
for i in np.arange(0.0, 1, 0.05):
    rhos = []
    rhos.extend(gen_inputs(Tsim/dt, shape = 'step', events = [0, i], values = [0, -1e-3])())

    powers, precurs = pke()(rhos, dt)
    plot(rhos, dt, powers = powers, precurs = precurs)
    
    with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
        rhos = str(rhos)[1:-1]
        f.writelines(rhos)
        f.writelines('\n')
                
        powers = str(powers)[1:-1]
        f.writelines(powers)
        f.writelines('\n')
        
        precurs = np.array(precurs).T
        for p in precurs:
            p = list(p)
            p = str(p)[1:-1]
            f.writelines(p)
            f.writelines('\n')
            
        f.flush()
        f.close()
    cnt+=1
    break
print('1')

# print('2')
# for i in np.arange(0.05, 1, 0.05):
#     for j in np.arange(i + 0.05, 1-0.05, 0.05):        
#         rhos = []
#         rhos.extend(gen_inputs(Tsim/dt, shape = 'step', events = [0, i, j], values = [0, -1e-3, 0])())        
#         powers, precurs = pke()(rhos, dt)
#         plot(rhos, dt, powers = powers, precurs = precurs)
        
#         with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
#             rhos = str(rhos)[1:-1]
#             f.writelines(rhos)
#             f.writelines('\n')
                    
#             powers = str(powers)[1:-1]
#             f.writelines(powers)
#             f.writelines('\n')
            
#             precurs = np.array(precurs).T
#             for p in precurs:
#                 p = list(p)
#                 p = str(p)[1:-1]
#                 f.writelines(p)
#                 f.writelines('\n')
                
#             f.flush()
#             f.close()            
#         cnt+=1
# print('2')

# print('3')
# for i in np.arange(0.05, 1, 0.05):
#     for j in np.arange(i + 0.05, 1 - 0.05, 0.05):
#         for k in np.arange(j + 0.05, 1 - 0.05, 0.05):
#             rhos = []
#             rhos.extend(gen_inputs(Tsim/dt, shape = 'step', events = [0, i, j, k], values = [0, -1e-3, -2e-3, 0])())
#             powers, precurs = pke()(rhos, dt)
#             plot(rhos, dt, powers = powers, precurs = precurs)
            
#             with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
#                 rhos = str(rhos)[1:-1]
#                 f.writelines(rhos)
#                 f.writelines('\n')
                        
#                 powers = str(powers)[1:-1]
#                 f.writelines(powers)
#                 f.writelines('\n')
                
#                 precurs = np.array(precurs).T
#                 for p in precurs:
#                     p = list(p)
#                     p = str(p)[1:-1]
#                     f.writelines(p)
#                     f.writelines('\n')
                    
#                 f.flush()
#                 f.close()            
#             cnt+=1
# print('3')

# print('4')
# for i in np.arange(0.05, 1, 0.05):
#     for j in np.arange(i + 0.05, 1 - 0.05, 0.05):
#         for k in np.arange(j + 0.05, 1 - 0.05, 0.05):
#             for l in np.arange(k + 0.05, 1 - 0.05, 0.05):
#                 rhos = []
#                 rhos.extend(gen_inputs(Tsim/dt, shape = 'step', events = [0, i, j, k,l], values = [0, -1e-3, -2e-3, -1e-3, 0])())
#                 powers, precurs = pke()(rhos, dt)
#                 plot(rhos, dt, powers = powers, precurs = precurs)
                
#                 with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
#                     rhos = str(rhos)[1:-1]
#                     f.writelines(rhos)
#                     f.writelines('\n')
                            
#                     powers = str(powers)[1:-1]
#                     f.writelines(powers)
#                     f.writelines('\n')
                    
#                     precurs = np.array(precurs).T
#                     for p in precurs:
#                         p = list(p)
#                         p = str(p)[1:-1]
#                         f.writelines(p)
#                         f.writelines('\n')
                        
#                     f.flush()
#                     f.close()            
#                 cnt+=1
# print('4')

# print('5')
# for i in np.arange(-5e-3, 6e-03, 1e-3):    
#     rhos = []
#     rhos.extend(gen_inputs(Tsim/dt, shape = 'step', events = [0], values = [i])())
    
#     powers, precurs = pke()(rhos, dt)
#     plot(rhos, dt, powers = powers, precurs = precurs)
    
#     with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
#         rhos = str(rhos)[1:-1]
#         f.writelines(rhos)
#         f.writelines('\n')
                
#         powers = str(powers)[1:-1]
#         f.writelines(powers)
#         f.writelines('\n')
        
#         precurs = np.array(precurs).T
#         for p in precurs:
#             p = list(p)
#             p = str(p)[1:-1]
#             f.writelines(p)
#             f.writelines('\n')
            
#         f.flush()
#         f.close()
#     cnt+=1
# print('5')

# # Tsim, dt = 100, 50e-03
# #rhos.extend(gen_inputs(Tsim/dt, shape = 'triangle', events = [0, 0.2, 0.3, 0.6, 0.8], values = [0, 0, -1e-3, -2e-3, -1e-3])()) 

# for i in np.arange(0.05, 0.75, 0.05):
#     rhos = []    
#     rhos.extend(gen_inputs(Tsim/dt, shape = 'triangle', events = [0, i, 0.8], values = [0, 1e-3, 0])())

#     powers, precurs = pke()(rhos, dt)
#     plot(rhos, dt, powers = powers, precurs = precurs)
    
#     with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
#         rhos = str(rhos)[1:-1]
#         f.writelines(rhos)
#         f.writelines('\n')
                
#         powers = str(powers)[1:-1]
#         f.writelines(powers)
#         f.writelines('\n')
        
#         precurs = np.array(precurs).T
#         for p in precurs:
#             p = list(p)
#             p = str(p)[1:-1]
#             f.writelines(p)
#             f.writelines('\n')
            
#         f.flush()
#         f.close()
#     cnt+=1
# print('1')

# print('2')
# for i in np.arange(0.25, 0.75, 0.05):
#     for j in np.arange(i + 0.25, 0.75 - 0.05, 0.05):
#         rhos = []
#         rhos.extend(gen_inputs(Tsim/dt, shape = 'triangle', events = [0, 0.2, i, j, 0.8], values = [0, 0, 1e-3, -2e-3, 1e-3])())
#         powers, precurs = pke()(rhos, dt)
#         plot(rhos, dt, powers = powers, precurs = precurs)
        
#         with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
#             rhos = str(rhos)[1:-1]
#             f.writelines(rhos)
#             f.writelines('\n')
                    
#             powers = str(powers)[1:-1]
#             f.writelines(powers)
#             f.writelines('\n')
            
#             precurs = np.array(precurs).T
#             for p in precurs:
#                 p = list(p)
#                 p = str(p)[1:-1]
#                 f.writelines(p)
#                 f.writelines('\n')
                
#             f.flush()
#             f.close()            
#         cnt+=1
# print('2')


# for i in np.arange(0.25, 0.75, 0.05):
#     rhos = []
#     rhos.extend(gen_inputs(Tsim/dt, shape = 'sine', events = [0, i, 1], values = [[1e-3, 1, 0, 0, dt],
#                                                                                     [2e-3, 1, 0, 0, dt]])())
#     powers, precurs = pke()(rhos, dt)
#     plot(rhos, dt, powers = powers, precurs = precurs)
    
#     with open(save_dir +  '{:06d}.txt'.format(cnt), 'w') as f:
#         rhos = str(rhos)[1:-1]
#         f.writelines(rhos)
#         f.writelines('\n')
                
#         powers = str(powers)[1:-1]
#         f.writelines(powers)
#         f.writelines('\n')
        
#         precurs = np.array(precurs).T
#         for p in precurs:
#             p = list(p)
#             p = str(p)[1:-1]
#             f.writelines(p)
#             f.writelines('\n')
            
#         f.flush()
#         f.close()            
#     cnt+=1


