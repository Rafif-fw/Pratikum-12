# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:09:30 2022

@author: Rafif Fernanda
"""

import pandas as pd

dataset = pd.read_csv("Negara1.csv")

df = pd.DataFrame(dataset)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()


print("Berikut Data Frame:")
print(df, "\n")

print("Berikut Data Mean:")
print(mean, "\n")

print("Berikut Data Standard Deviation:")
print(std, "\n")


mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandardDeviation.csv')
print("file Berhasil Dibuat")