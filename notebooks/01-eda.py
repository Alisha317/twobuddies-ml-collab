# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

df = pd.read_csv("../data/raw/titanic.csv")
df.head()

# %%
df.info()

# %%
df.isnull().sum()

# %%
df.groupby("Sex")["Survived"].mean()

# %%
df.groupby("Pclass")["Survived"].mean()

# %%
df.describe()

# %%
import sys
sys.path.insert(0, "../src")
from features import clean_titanic_data

df_clean = clean_titanic_data(df)
df_clean.isnull().sum()

# %%
