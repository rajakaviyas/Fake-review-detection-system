import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import sklearn
from matplotlib import pyplot as plt
##from sklearn.model_selection import train_test_split
##from sklearn.model_selection import StratifiedShuffleSplit
##from sklearn.preprocessing import OneHotEncoder, LabelEncoder
##from sklearn.naive_bayes import GaussianNB 
##from sklearn import metrics 
##from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
##from sklearn.metrics import roc_auc_score
##from sklearn.metrics import log_loss
##from sklearn.model_selection import cross_val_score
##from sklearn.dummy import DummyClassifier

# Read data and display data head

shopping = pd.read_csv('dataset/online_shoppers_intention.csv')
shopping.head()
