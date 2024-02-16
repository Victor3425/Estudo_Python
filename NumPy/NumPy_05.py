import numpy as dsa
import pandas as pd


arquivo = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\NumPy\dataset.csv',sep=',')

arr1  = dsa.loadtxt(arquivo, delimiter= ',', usecols= (0,1,2,3),skiprows=1)

print(type(arr1))
#print(arr1)
