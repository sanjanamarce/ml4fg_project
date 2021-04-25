import preparedata
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X, y, feature_names = preparedata.getData('merged_genecounts.csv')
scaler = StandardScaler()
scaler.fit(X)

sel_ = SelectFromModel(LogisticRegression(C=1, penalty='l1', solver='liblinear'))
sel_.fit(scaler.transform(X), y)

selected_feat = feature_names[np.where(sel_.get_support())[0]]
print('total features: {}'.format((X.shape[1])))
print('selected features: {}'.format(len(selected_feat)))
print('features with coefficients shrank to zero: {}'.format(
      np.sum(sel_.estimator_.coef_ == 0)))

print(selected_feat)
selected_feat.to_csv('lasso_nonzero_features.csv', index=True)