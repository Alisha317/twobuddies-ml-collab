import os
import pickle

import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier

with open("params.yaml") as f:
    params = yaml.safe_load(f)

X_train = pd.read_csv("data/processed/X_train.csv")
y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()

model = RandomForestClassifier(
    n_estimators=params["train"]["n_estimators"],
    max_depth=params["train"]["max_depth"],
    random_state=params["seed"],
)
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)
