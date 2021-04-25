import pandas as pd
import numpy as np

def getData(genecount_filename):
	merged_counts = pd.read_csv(genecount_filename)
	feature_names = merged_counts['gene']

	features = merged_counts[["drought_1_cnt", "drought_2_cnt","drought_3_cnt","control_1_cnt","control_2_cnt","control_3_cnt"]]
	feature_np = features.to_numpy()
	X = np.transpose(feature_np)
	y = np.array([1,1,1,0,0,0])

	return X, y, feature_names

