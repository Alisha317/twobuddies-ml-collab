def clean_titanic_data(df, age_median=None, embarked_mode=None):
    df = df.copy()

    if age_median is None:
        age_median = df["Age"].median()
    if embarked_mode is None:
        embarked_mode = df["Embarked"].mode()[0]

    df["Age"] = df["Age"].fillna(age_median)
    df["Embarked"] = df["Embarked"].fillna(embarked_mode)
    return df
