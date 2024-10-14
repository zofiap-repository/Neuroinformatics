'''
Data credits: Daniel S. Marcus, Tracy H. Wang, Jamie Parker, John G. Csernansky, John C. Morris, Randy L. Buckner;
Open Access Series of Imaging Studies (OASIS): Cross-sectional MRI Data in Young, Middle Aged, Nondemented, and
Demented Older Adults. J Cogn Neurosci 2007; 19 (9): 1498–1507. doi: https://doi.org/10.1162/jocn.2007.19.9.1498
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the data
dementia_df = pd.read_csv('oasis_cross-sectional.csv')

# Plotting
custom_palette = {"M": "steelblue", "F": "salmon"}
plt.figure(figsize=(10,7), facecolor="white")
columns_to_plot = ["Age", "Educ", "SES", "MMSE"]

for (i, column) in enumerate(columns_to_plot):
    plt.subplot(2,2,i+1)
    sns.barplot(
        x='CDR', data=dementia_df, y=column,
        hue='M/F', errorbar="sd", palette=custom_palette)    
    plt.title(f"{column} (Mean ± SD)")

plt.tight_layout()
plt.savefig('dementia_bar_plots.png')
plt.show()
plt.close()

print("Summary statistics:")

summary_stats = dementia_df.groupby(by=["CDR", "M/F"]).agg(
    {"ID": "count", "Age": ["mean", "std"], "Educ": ["mean", "std"],
     "SES": ["mean", "std"], "MMSE": ["mean", "std"]}).round(2)

display(summary_stats)