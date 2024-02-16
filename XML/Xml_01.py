import pandas as pd
import re

arquivo = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\XML\Nota-11-10-2023015156teste.txt',sep=';')



df = arquivo[24:40]

CNPJre = re.findall(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}',str(df))

num = re.findall(r'[0-9]{6}',str(df))

codigore = re.findall(r'[0-9]{3}[A-Z]{1}.[0-9]{4}.[0-9]{4}.[0-9]{7}-[A-Z]{1}',str(arquivo))

#print(num)
#print(df)
#print(arquivo)
print(CNPJre)
#print(codigore)