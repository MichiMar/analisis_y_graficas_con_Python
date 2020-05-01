import pandas as pd # Pandas: sirve para manejo de datos
import numpy as np # Numpy: sirve para Algebra lineal
import matplotlib.pyplot as plt # Graficar
import seaborn as sns # Seaborn: Graficas de estadistica

df = pd.read_csv("https://raw.githubusercontent.com/bcbarsness/machine-learning/master/USA_Housing.csv")
df.head()
# df.tail()
# df.info()
# df.columns # como quiero informacion de todas las columnas no le pongo (), a meno9s que quiera especificamente una


# df['Price'] # [] para sacar la informacion de esa columna (Precios, Area Population, etc)
# df['Area Population']
# df[0:3]

# Para dos elementos

df.loc[0:5, ['Price', 'Area Population']]

precios = df.sort_values('Price')['Price']
# precios.plot()  //  si lo subo asi me va a graficar por indice y se ve desordenado
precios.plot(use_index=False)  # asi anulo que vaya segun el orden de la tabal original

