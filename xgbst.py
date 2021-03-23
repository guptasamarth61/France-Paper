import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("Bank 2\Data.xlsx")
feature_names = ['sin_time', 'cos_time', 'QL', 'HOL', 'Day', 'Week']
X = df[feature_names].to_numpy()
y = df['X1'].to_numpy()
# data_dmatrix = xgb.DMatrix(data=X,label=y, feature_names=feature_names)
# params = {'colsample_bytree': 0.3,'learning_rate': 0.1, 'max_depth': 5, 'alpha': 10}
# cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=5, num_boost_round=50,early_stopping_rounds=10,metrics="mae", as_pandas=True, seed=123)
# print("MAE Mean", cv_results['test-mae-mean'].mean())
# print("MAE Standard Deviation", cv_results['test-mae-std'].mean())


# # to plot the feature importance
# xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=50)
# xgb.plot_importance(xg_reg)
# plt.rcParams['figure.figsize'] = [5, 5]
# plt.show()

from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
def rfr_model(X, y):
    gsc = GridSearchCV(estimator=RandomForestRegressor(),
        param_grid={
            'max_depth': range(3,7),
            'n_estimators': (10, 50, 100, 1000),
        },
        cv=5, scoring='neg_mean_squared_error', verbose=2, n_jobs=-1)
    grid_result = gsc.fit(X, y)
    best_params = grid_result.best_params_
    rfr = RandomForestRegressor(max_depth=best_params["max_depth"], n_estimators=best_params["n_estimators"], random_state=False, verbose = True)
    scores = cross_val_score(rfr, X, y, cv=10, scoring='neg_mean_absolute_error')
    print(scores)

rfr_model(X,y)