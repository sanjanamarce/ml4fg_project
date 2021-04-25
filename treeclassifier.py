import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier

import pandas as pd
import numpy as np
import preparedata

X, y, feature_names = preparedata.getData('merged_genecounts.csv')

# Building the model
extra_tree_forest = ExtraTreesClassifier(n_estimators = 10000, criterion ='entropy')
extra_tree_forest.fit(X, y)
feature_importance = extra_tree_forest.feature_importances_
feature_importance_normalized = np.std([tree.feature_importances_ for tree in 
                                        extra_tree_forest.estimators_],
                                        axis = 0)

genes = np.array([feature_names, feature_importance_normalized]).transpose()


# Keep genes with non-zero importance
nonzero_gene_importance = genes[np.nonzero(genes[:,1]), :]
#print(nonzero_gene_importance)
#print(nonzero_gene_importance[0,:,0].shape)
#print(nonzero_gene_importance[0,:,1].shape)
plt.bar(nonzero_gene_importance[0,:,0], nonzero_gene_importance[0,:,1])
plt.xlabel('Feature Labels')
plt.xticks(rotation = 10) 
plt.ylabel('Feature Importances')
plt.title('Relative Gene Importance to Drought-Resistance using Extra Trees Classifier')
plt.show()


sorted_gene_importance = genes[np.argsort(genes[:, 1])]
sorted_gene_importance = np.flip(sorted_gene_importance, axis=0)
sorted_gene_importance = sorted_gene_importance[:20,:]
print(sorted_gene_importance)
plt.bar(sorted_gene_importance[:,0], sorted_gene_importance[:,1])
plt.xlabel('Feature Labels')
plt.xticks(rotation = 25) 
plt.ylabel('Feature Importances')
plt.title('Relative Gene Importance of 25 Most Important Genes to Drought-Resistance')
plt.show()

