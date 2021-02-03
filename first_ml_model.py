# Code you have previously used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex3 import *

# print the list of columns in the dataset to find the name of the prediction target
home_data.columns

y = home_data.SalePrice

# Create the list of features below
feature_names = home_data.columns
# Select data corresponding to features in feature_names
home_data = home_data[['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']]
home_data.columns = [''] * len(home_data.columns)
X = home_data

# Review data
# print description or statistics from X
print(X)

# print the top few lines
for i in range(10):
    print(y[i])

#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X, y)

#overfitted due to course requirements
predictions = iowa_model.predict(X)

