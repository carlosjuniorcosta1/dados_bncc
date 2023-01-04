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
    

