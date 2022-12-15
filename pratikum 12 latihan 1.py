# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:25:44 2022

@author: Rafif Fernanda
"""

import pandas as pd

dataset = pd.read_csv("Negara1.csv")

df = pd.DataFrame(dataset)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(dataset.head(20))
print(mean)
print(std)
