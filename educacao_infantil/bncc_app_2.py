# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:51:04 2022

@author: Usuario
"""



import pandas as pd
import numpy as np
import re 
import matplotlib.pyplot as plt 
import seaborn as sns
import os

files = [x for x in os.listdir() if x.endswith("_inf.csv") ]


for x,y  in enumerate(files):
    exec(f'df_{x} = pd.read_csv({"y"})')


#acrescenta detalhas da faixa etária

df_0['faixa_etaria'] = df_0['faixa_etaria'].apply(lambda x: re.sub(r'\(zero\b', '(0', x))
df_0['idade_anos_inicial'] = df_0['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\(?(\d+).*\sa\s(?=\d)', x)))
df_0['idade_meses_inicial'] = df_0['faixa_etaria'].apply(lambda x: re.findall(r'((?<=\(\d))\s\w+\s\w+\s(\d+)\s(?=m)', str(x)))
df_0['idade_meses_inicial'] = df_0['idade_meses_inicial'].apply(lambda x: re.sub(r"\)||,|\[|\]|\'|\(|\|\)|\s|\s+", '', str(x)))
df_0['idade_anos_final'] = df_0['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\ba\s(\d+)\s', x)))
df_0['idade_meses_final'] = df_0['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'(\d+)\s(?=m)\w+\)', str(x))))

df_1['faixa_etaria'] = df_1['faixa_etaria'].apply(lambda x: re.sub(r'\(zero\b', '(0', x))
df_1['idade_anos_inicial'] = df_1['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\(?(\d+).*\sa\s(?=\d)', x)))
df_1['idade_meses_inicial'] = df_1['faixa_etaria'].apply(lambda x: re.findall(r'((?<=\(\d))\s\w+\s\w+\s(\d+)\s(?=m)', str(x)))
df_1['idade_meses_inicial'] = df_1['idade_meses_inicial'].apply(lambda x: re.sub(r"\)||,|\[|\]|\'|\(|\|\)|\s|\s+", '', str(x)))
df_1['idade_anos_final'] = df_1['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\ba\s(\d+)\s', x)))
df_1['idade_meses_final'] = df_1['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'(\d+)\s(?=m)\w+\)', str(x))))

df_2['faixa_etaria'] = df_2['faixa_etaria'].apply(lambda x: re.sub(r'\(zero\b', '(0', x))
df_2['idade_anos_inicial'] = df_2['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\(?(\d+).*\sa\s(?=\d)', x)))
df_2['idade_meses_inicial'] = df_2['faixa_etaria'].apply(lambda x: re.findall(r'((?<=\(\d))\s\w+\s\w+\s(\d+)\s(?=m)', str(x)))
df_2['idade_meses_inicial'] = df_2['idade_meses_inicial'].apply(lambda x: re.sub(r"\)||,|\[|\]|\'|\(|\|\)|\s|\s+", '', str(x)))
df_2['idade_anos_final'] = df_2['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\ba\s(\d+)\s', x)))
df_2['idade_meses_final'] = df_2['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'(\d+)\s(?=m)\w+\)', str(x))))

df_3['faixa_etaria'] = df_3['faixa_etaria'].apply(lambda x: re.sub(r'\(zero\b', '(0', x))
df_3['idade_anos_inicial'] = df_3['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\(?(\d+).*\sa\s(?=\d)', x)))
df_3['idade_meses_inicial'] = df_3['faixa_etaria'].apply(lambda x: re.findall(r'((?<=\(\d))\s\w+\s\w+\s(\d+)\s(?=m)', str(x)))
df_3['idade_meses_inicial'] = df_3['idade_meses_inicial'].apply(lambda x: re.sub(r"\)||,|\[|\]|\'|\(|\|\)|\s|\s+", '', str(x)))
df_3['idade_anos_final'] = df_3['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\ba\s(\d+)\s', x)))
df_3['idade_meses_final'] = df_3['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'(\d+)\s(?=m)\w+\)', str(x))))

df_4['faixa_etaria'] = df_4['faixa_etaria'].apply(lambda x: re.sub(r'\(zero\b', '(0', x))
df_4['idade_anos_inicial'] = df_4['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\(?(\d+).*\sa\s(?=\d)', x)))
df_4['idade_meses_inicial'] = df_4['faixa_etaria'].apply(lambda x: re.findall(r'((?<=\(\d))\s\w+\s\w+\s(\d+)\s(?=m)', str(x)))
df_4['idade_meses_inicial'] = df_4['idade_meses_inicial'].apply(lambda x: re.sub(r"\)||,|\[|\]|\'|\(|\|\)|\s|\s+", '', str(x)))
df_4['idade_anos_final'] = df_4['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'\ba\s(\d+)\s', x)))
df_4['idade_meses_final'] = df_4['faixa_etaria'].apply(lambda x: ' '.join(re.findall(r'(\d+)\s(?=m)\w+\)', str(x))))

df_0.drop('Unnamed: 0', axis = 1, inplace=True)
df_1.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace=True)
df_2.drop('Unnamed: 0', axis =1, inplace=True)
df_3.drop('Unnamed: 0', axis = 1, inplace=True)
df_4.drop('Unnamed: 0', axis = 1, inplace=True)

df_0.to_csv('corpo_gestos_ed_inf.csv')
df_1.to_csv('df_edu_inf.csv')
df_2.to_csv('escuta_fala_ed_inf.csv')

df_3.to_csv('espaco_tempo_ed_inf.csv')

df_4.to_csv('eu_outro_nos_ed_inf.csv')


df_1['descricao_cod'].apply(lambda x: len(x))
