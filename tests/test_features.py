import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from features import clean_titanic_data


def test_clean_titanic_data_fills_missing_age():
    df = pd.DataFrame({"Age": [22, None, 30], "Embarked": ["S", "C", None]})
    result = clean_titanic_data(df)
    assert result["Age"].isnull().sum() == 0
    assert result["Embarked"].isnull().sum() == 0


def test_clean_titanic_data_uses_provided_values():
    df = pd.DataFrame({"Age": [None], "Embarked": [None]})
    result = clean_titanic_data(df, age_median=25, embarked_mode="S")
    assert result["Age"].iloc[0] == 25
    assert result["Embarked"].iloc[0] == "S"
