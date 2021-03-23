from sklearn.svm import SVR
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
df = pd.read_excel("Bank 2\Data.xlsx")
feature_names = ['sin_time', 'cos_time', 'QL', 'HOL', 'Day', 'Week']
X = df[feature_names].to_numpy()
y = df['X1'].to_numpy()
# regr = make_pipeline(StandardScaler(), SVR())
# scores = cross_val_score(regr, X, y, scoring="neg_mean_absolute_error", cv=5)
# print(scores.mean()*-1)

from sklearn.linear_model import LinearRegression
regr = LinearRegression().fit(X, y)
scores = cross_val_score(regr, X, y, cv=5)
print(scores)
