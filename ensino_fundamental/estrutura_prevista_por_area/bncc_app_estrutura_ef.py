# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:08:44 2022

@author: Usuario
"""

import pandas as pd
import os
import re


files = [x for x in os.listdir() if x.startswith("estrutura") and not x.endswith('csv')]


for x, y in enumerate(files):
    exec(f'df_{x} = pd.read_excel({"y"})')
    


#artes
df_0['cod_hab'] = df_0['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_0['descricao_cod'] = df_0['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_0['primeiro_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_0['segundo_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_0['terceiro_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_0['quarto_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_0['quinto_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_0['sexto_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_0['setimo_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_0['oitavo_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_0['nono_ef'] = df_0['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))

df_0.columns = ['componente', 'ano_faixa', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']

df_0.to_csv('bncc_artes.csv')
#ciencias

df_1['cod_hab'] = df_1['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_1['descricao_cod'] = df_1['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_1['primeiro_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_1['segundo_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_1['terceiro_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_1['quarto_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_1['quinto_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_1['sexto_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_1['setimo_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_1['oitavo_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_1['nono_ef'] = df_1['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))
df_1.columns = ['componente', 'ano_faixa', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']
df_1.to_csv('bncc_ciencias.csv')

#educacao_fisica

df_2['cod_hab'] = df_2['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_2['descricao_cod'] = df_2['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_2['primeiro_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_2['segundo_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_2['terceiro_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_2['quarto_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_2['quinto_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_2['sexto_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_2['setimo_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_2['oitavo_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_2['nono_ef'] = df_2['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))

df_2.columns = ['componente', 'ano_faixa', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']

df_2.to_csv('bncc_educacao_fisica.csv')
#ensino religioso

df_3['cod_hab'] = df_3['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_3['descricao_cod'] = df_3['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_3['primeiro_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_3['segundo_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_3['terceiro_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_3['quarto_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_3['quinto_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_3['sexto_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_3['setimo_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_3['oitavo_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_3['nono_ef'] = df_3['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))
df_3.columns = ['componente', 'ano_faixa', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']

df_3.to_csv('bncc_ensino_religioso.csv')

#geografia

df_4['cod_hab'] = df_4['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_4['descricao_cod'] = df_4['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_4['primeiro_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_4['segundo_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_4['terceiro_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_4['quarto_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_4['quinto_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_4['sexto_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_4['setimo_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_4['oitavo_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_4['nono_ef'] = df_4['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))
df_4.columns = ['componente', 'ano_faixa', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']

df_4.to_csv('bncc_geografia.csv')
#historia

df_5['cod_hab'] = df_5['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_5['descricao_cod'] = df_5['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_5['primeiro_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_5['segundo_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_5['terceiro_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_5['quarto_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_5['quinto_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_5['sexto_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_5['setimo_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_5['oitavo_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_5['nono_ef'] = df_5['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))

df_5.columns = ['componente', 'ano_faixa', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']

df_5.to_csv('bncc_historia.csv')

#lingua inglesa

df_6['cod_hab'] = df_6['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_6['descricao_cod'] = df_6['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_6['primeiro_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_6['segundo_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_6['terceiro_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_6['quarto_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_6['quinto_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_6['sexto_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_6['setimo_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_6['oitavo_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_6['nono_ef'] = df_6['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))

df_6.columns
df_6.columns = ['componente', 'ano_faixa', 'eixo', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']
df_6.to_csv('bncc_lingua_inglesa.csv')
#lingua portuguesa

df_7['cod_hab'] = df_7['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_7['descricao_cod'] = df_7['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_7['primeiro_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_7['segundo_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_7['terceiro_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_7['quarto_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_7['quinto_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_7['sexto_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_7['setimo_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_7['oitavo_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_7['nono_ef'] = df_7['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))

df_7.columns = ['componente', 'ano_faixa', 'campo_atuacao', 'praticas_linguagem',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']

df_7.to_csv('bncc_lingua_portuguesa.csv')
#matematica

df_8['cod_hab'] = df_8['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\((.*\d)', x)))

df_8['descricao_cod'] = df_8['HABILIDADES'].apply(lambda x: ' '.join(re.findall(r'\(.*\d\)\s(.*.)', x)))
df_8['primeiro_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('1º', x)))
df_8['segundo_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('2º', x)))
df_8['terceiro_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('3º', x)))
df_8['quarto_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('4º', x)))
df_8['quinto_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('5º', x)))
df_8['sexto_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('6º', x)))
df_8['setimo_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('7º', x)))
df_8['oitavo_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('8º', x)))
df_8['nono_ef'] = df_8['ANO/FAIXA'].apply(lambda x: len(re.findall('9º', x)))




df_8.columns = ['componente', 'ano_faixa', 'unidades_tematicas',
       'objetos_conhecimento', 'habilidades', 'cod_hab', 'descricao_cod',
       'primeiro_ef', 'segundo_ef', 'terceiro_ef', 'quarto_ef', 'quinto_ef',
       'sexto_ef', 'setimo_ef', 'oitavo_ef', 'nono_ef']


df_8.to_csv('bncc_matematica.csv')

df.to_csv('estrutura_componentes.csv')
















