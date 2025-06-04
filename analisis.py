import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('albumes_pop.csv')

print(df.head())

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='artista', y='popularidad', hue=None, legend=False, palette='viridis')
plt.title('Popularidad por artista')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='año', hue=None, legend=False, palette='pastel')
plt.title('Cantidad de álbumes por año')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='album', y='canciones', hue=None, legend=False, palette='rocket')
plt.title('Número de canciones por álbum')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()