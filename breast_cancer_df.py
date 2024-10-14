'''
Data credits: Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature
extraction for breast tumor diagnosis. SPIE Proceedings. https://doi.org/10.1117/12.148698
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the data
cancer_df = pd.read_csv('breast_cancer.csv')

# Drawing scatter plot between radius and texture mean
plt.figure(facecolor='white')
sns.regplot(x='radius_mean', y='texture_mean', data=cancer_df, x_ci='sd')
plt.axvline(x=cancer_df['radius_mean'].mean(), color='black', linewidth=1, linestyle='dashed')
plt.axvline(x=cancer_df['texture_mean'].mean(), color='black', linewidth=1, linestyle='dashed')
plt.title('Radius vs Texture')
plt.show()

# Calculating correlation between radius and texture mean
correlation = cancer_df['radius_mean'].corr(cancer_df['texture_mean'])
print(f"Correlation between radius_mean and texture_mean: {correlation: .2f}")

# Drawing correlation matrix as a heatmap
selected_columns = list(filter(lambda x: 'mean' in x, cancer_df.columns))
corr_matrix = cancer_df[selected_columns].corr()
plt.plot(figsize=(8,7), facecolor='white')
sns.heatmap(data=corr_matrix, cmap="YlGnBu")
plt.title("Correlation Among Variables")
plt.show()