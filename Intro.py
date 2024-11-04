#We list the libraries that we need

# Data manipulation and analysis
import pandas as pd
import numpy as np

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Machine learning and modeling
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

# Advanced ensemble methods
import xgboost as xgb
import lightgbm as lgb
import catboost as cb

# Time series analysis
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from prophet import Prophet
import pmdarima as pm

# Financial data (optional)
import yfinance as yf
import pandas_datareader.data as web

# Utility libraries
import joblib
from tqdm import tqdm

# Optional: Interactive visualization (comment out if not needed)
# import plotly.express as px
# import plotly.graph_objs as go

# Optional: Handling large datasets or parallel computing (comment out if not needed)
# import dask.dataframe as dd

