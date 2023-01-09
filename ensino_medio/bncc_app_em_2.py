# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:07:28 2023

@author: Usuario
"""

import pandas as pd
import os
import re

files = [x for x in os.listdir() if x.startswith('hab')]

for x, y in enumerate(files):
    exec(f'df_{x} = pd.read_excel({"y"})')
    

df_0['primeiro_ano'] = "sim"
df_0['segundo_ano'] = "sim"
df_0['terceiro_ano']= 'sim'
df_0['area'] = 'chs'

df_1['primeiro_ano'] = "sim"
df_1['segundo_ano'] = "sim"
df_1['terceiro_ano']= 'sim'
df_1['area'] = 'cnt'


df_2['primeiro_ano'] = "sim"
df_2['segundo_ano'] = "sim"
df_2['terceiro_ano']= 'sim'
df_2['area'] = 'lgg'


 
df_3['primeiro_ano'] = "sim"
df_3['segundo_ano'] = "sim"
df_3['terceiro_ano']= 'sim'
df_3['area'] = 'por'



df_4['primeiro_ano'] = "sim"
df_4['segundo_ano'] = "sim"
df_4['terceiro_ano']= 'sim'

df_4['area'] = 'mat'


df_hab_em = pd.concat([df_0, df_1, df_2, df_3, df_4], ignore_index=True)

df_competencias = pd.read_csv('competencias_area_em.csv')

df_hab_em.to_csv('df_habilidades_em.csv')




