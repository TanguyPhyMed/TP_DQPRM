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

stats, pval = scipy.stats.shapiro(men)
print(pval)

stats2, pval2 = scipy.stats.shapiro(men)
print(pval2)

if pval < 0.05:
    print("Hypothèse nulle rejetée")
else:
    print("Hypothèse nulle acceptée (Suit une loi normale)")

if pval2 < 0.05:
    print("Hypothèse nulle rejetée")
else:
    print("Hypothèse nulle acceptée (Suit une loi normale)")

if np.var(men) == np.var(women):
    print("Leur variance sont egales")
