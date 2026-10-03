import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from features import clean_titanic_data

def test_clean_titanic_data_fills_missing_age():
    df = pd.DataFrame({
        "Age": [22, None, 30],
        "Embarked": ["S", "C", None]
    })
    result = clean_titanic_data(df)
    assert result["Age"].isnull().sum() == 0
    assert result["Embarked"].isnull().sum() == 0
