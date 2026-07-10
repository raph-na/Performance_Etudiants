import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Copie du dataset Power BI
df = dataset.copy()

# Suppression des valeurs manquantes
df = df.dropna()

# Encodage automatique des colonnes texte
le = LabelEncoder()

for col in df.columns:

    if df[col].dtype == 'object':
        try:
            df[col] = le.fit_transform(df[col].astype(str))
        except:
            pass

# Conservation uniquement des colonnes numériques
df_num = df.select_dtypes(include=[np.number])

# Matrice de corrélation
corr_matrix = df_num.corr()

# Heatmap
plt.figure(figsize=(12,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    linewidths=0.5
)

plt.title("Facteurs associes a la reussite academique")

plt.tight_layout()

plt.show()