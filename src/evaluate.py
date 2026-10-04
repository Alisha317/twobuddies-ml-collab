import pandas as pd
import pickle
import json
import subprocess
from sklearn.metrics import accuracy_score

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

try:
    commit_sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
except Exception:
    commit_sha = "unknown"

metrics = {"accuracy": accuracy, "commit_sha": commit_sha}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(f"Accuracy: {accuracy:.4f}")
