# Data Analysis and visualization tools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as inline
import pandas as pd
import seaborn as sns
import plotly as py
import plotly.graph_objs as go

#statistics tools
import statsmodels.api as sm
import scipy.stats as st
from scipy.stats import shapiro, mannwhitneyu, chi2_contingency

#scikit learn framework
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

import warnings
warnings.filterwarnings('ignore')
# Reading Database
data = pd.read_csv('dataset/online_shoppers_intention.csv')

# shape of the data(number of rows vs number of column)
data.shape
