# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:40:16 2023

@author: Usuario
"""

import pandas as pd 
import re 
import os

files = [x for x in os.listdir() if x.startswith('comp') ]


for x,y  in enumerate(files):
    exec(f'df_{x} = pd.read_excel({"y"})')
        
df_0['area'] = 'chs'

df_1['area'] = 'cnt'

df_3['area']= 'lgg'

df_4['area'] = 'mat'


df_competencias_area = pd.concat([df_0, df_1, df_3, df_4], ignore_index= True)
df_competencias_area.drop('Unnamed: 0', axis = 1, inplace=True)
df_competencias_area.to_csv('competencias_area_em.csv')

df_3.drop('Unnamed: 0', axis = 1, inplace=True)
df_3.to_csv('competencias_gerais_em.csv')