# Exercice 6



import pandas as pd 			# Importe du fichier csv 
df = pd.read_csv('./data/ages.csv')
df.describe() 			# description du fichier et des données à l'intérieur
df

df.groupby(df['grouping']== 'men').describe()

men = df.query('grouping == "men"')['height']
women = df.query('grouping == "women"')['height']
plt.boxplot([men,women], labels = ['hommes','femmes'])
plt.grid()
plt.show()
