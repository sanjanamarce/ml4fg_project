import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

import preparedata

X, y, feature_names = preparedata.getData('merged_genecounts.csv')
y = np.array([y]).transpose()

lasso_features = pd.read_csv('lasso_nonzero_features.csv')
lasso_features.columns = ['idx', 'gene']
replicates_lasso = X[:,lasso_features['idx']]
replicates_lasso = replicates_lasso[:,:20]
feature_names_lasso = feature_names[lasso_features['idx']]
feature_names_lasso = feature_names_lasso[:20]

feature_names_lasso.loc[len(feature_names_lasso.index)] = 'LABEL'

all_data = np.append(replicates_lasso, y, 1)
all_df = pd.DataFrame(all_data, columns = feature_names_lasso)

#ploting the heatmap for correlation
ax = sns.heatmap(all_df.corr().round(2), annot=False) 
plt.show()
