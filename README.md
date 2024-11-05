# Forecasting-Data---ML-series
Some forecasting because I am bored on Monday night

What I want to do : Try to predict a tendency in some penny currencies prices! This project is only recreational, and for now I am mainly interested 
in finding statistically meaningful results rather than actually implementing a trading strategy (of course, I will if I find some exciting results!)

Let's dive into this and see if we can find some cool results!

Also, there are things that I would be very interested to implement on my own, and I will list them here :
- Ensemble learning for predicting continuous data : I have already used random forest in the past for classification problem, let's try now to do it 
for mean of random forests
- Boosting methods instead of random forest! Something that I was asked for during my interviews and I wasn't very comfortable with it. After some research,
the topic seems very interesting and worth the try
- I would also like to try later with a lot and lots of stock prices and perform PCA for dimensionality reduction

Overall, this project is just a warm-up for a larger project that I have in mind! Stay tuned!

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

