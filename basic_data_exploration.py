# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex2 import *
import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Print summary statistics in next line
home_data.describe()

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = int(round(home_data[['LotArea']].mean()))

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = int(2021 - home_data[['YearBuilt']].max())
#print(type(avg_lot_size))
print(avg_lot_size)
print(newest_home_age)