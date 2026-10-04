import os
import sys

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

sys.path.insert(0, os.path.dirname(__file__))
from features import clean_titanic_data

with open("params.yaml") as f:
    params = yaml.safe_load(f)

df = pd.read_csv("data/raw/titanic.csv")

age_median = df["Age"].median()
embarked_mode = df["Embarked"].mode()[0]
df = clean_titanic_data(df, age_median=age_median, embarked_mode=embarked_mode)

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
X = df[features]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=params["split"]["test_size"], random_state=params["seed"]
)

os.makedirs("data/processed", exist_ok=True)
X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)
