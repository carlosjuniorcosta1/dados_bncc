# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:52:43 2022

@author: Usuario
"""

import pandas as pd
import numpy as np
import re 
import matplotlib.pyplot as plt 
import seaborn as sns
import os

files = [x for x in os.listdir() if x.endswith("_inf.csv") ]


df_ef_1 = pd.read_excel("corpo_gestos_movimentos.xlsx")

df_ef_2 = pd.read_excel('escuta_fala_pensamento.xlsx')

df_ef_3 = pd.read_excel('espaco_tempos_quantidades_ed_inf.xlsx')

df_ef_4 = pd.read_excel('eu_outro_nos_ed_inf.xlsx')

df_ef = pd.concat([df_ef_1, df_ef_2, df_ef_3, df_ef_4], ignore_index=True)

df_ef.columns = ['campos_experiencias', 'faixas_etarias', 
      'obj_apr', 'cod_apr']
      







#df_ef.to_csv('df_ef_completo.csv')

#df_ef.drop(['ms_abordagem', 'ms_sugestoes'], axis = 1, inplace=True)


"""
df_ef_1 = df_ef.query('campos_experiencias in "Corpo, gestos e movimentos"')
df_ef_2 = df_ef.query('campos_experiencias in "Escuta, fala, pensamento e imaginação"')
df_ef_3 = df_ef.query('campos_experiencias in "Espaços, tempos, quantidades, relações e transformações"')
df_ef_4 = df_ef.query('campos_experiencias in "O eu, o outro e o nós"')
"""

#a partir daqui

df_ef_1['cod_apr'] = df_ef_1['obj'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_ef_2['cod_apr'] = df_ef_2['obj'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_ef_3['cod_apr'] = df_ef_3['obj'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_ef_4['cod_apr'] = df_ef_4['obj'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_ef_1['descricao_cod'] = df_ef_1['obj'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s\n(.*.)', x)))
df_ef_2['descricao_cod'] = df_ef_2['obj'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s\n(.*.)', x)))
df_ef_3['descricao_cod'] = df_ef_3['obj'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s\n(.*.)', x)))
df_ef_4['descricao_cod'] = df_ef_4['obj'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s\n(.*.)', x)))




df_ef_1.to_csv('corpo_gestos_ed_if.csv')
df_ef_2.to_csv('escuta_fala_ed_if.csv')
df_ef_3.to_csv('espacos_tempos_ed_if.csv')
df_ef_4.to_csv('eu_outro_ed_if.csv')




#falta concatenar

df_ef_1 = pd.read_csv('corpo_gestos_ed_if.csv')

df_ef_2 = pd.read_csv('escuta_fala_ed_if.csv')
df_ef_3 = pd.read_csv('espacos_tempos_ed_if.csv')
df_ef_4 = pd.read_csv('eu_outro_ed_if.csv')


df = pd.concat([df_ef_1, df_ef_2, df_ef_3, df_ef_4], ignore_index= True)
df.drop('obj', axis=1, inplace=True)

df.to_csv('df_edu_if.csv')

from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)















