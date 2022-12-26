# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:39:07 2022

@author: Usuario
"""

import pandas as pd 
import re
import os


files = [x for x in os.listdir() if x.startswith('competencias_esp')]

lista = []

for x in files:
    lista.append(pd.read_excel(x))
    
    

for i in range(len(lista)):
    globals()[f"df_{i}"] = lista[i]


df_0['conteudo'] = "Arte"
df_0.columns = ['competencias', 'conteudo']

df_1['conteudo'] = "Ciências Humanas"
df_1.columns = ['competencias', 'conteudo']


df_2['conteudo'] = "Ciências da Natureza"
df_2.columns = ['competencias', 'conteudo']


df_3['conteudo'] = "Educacão Física"
df_3.columns = ['competencias', 'conteudo']


df_4['conteudo'] = "Ensino Religioso"
df_4.columns = ['competencias', 'conteudo']


df_5['conteudo'] = "Geografia"
df_5.columns = ['competencias', 'conteudo']


df_6['conteudo'] = "História"
df_6.columns = ['competencias', 'conteudo']


df_7['conteudo'] = "Língua Inglesa"
df_7.columns = ['competencias', 'conteudo']


df_8['conteudo'] = "Linguagens"
df_8.columns = ['competencias', 'conteudo']



df_9['conteudo'] = "Língua Portuguesa"
df_9.columns = ['competencias', 'conteudo']


df_10['conteudo'] = "Matemática"
df_10.columns = ['competencias', 'conteudo']



df = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, \
                df_6, df_7, df_8, df_9, df_10], ignore_index=True)


df.to_csv('competencias_especificas_por_area.csv')




