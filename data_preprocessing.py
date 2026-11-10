"""Data preprocessing module for CDC NHANES gallbladder cohort."""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_data(filepath="data/nhanes_gallbladder_cohort.csv"):
    df = pd.read_csv(filepath)
    return df

def clean_and_split_data(df, test_size=0.20, random_state=42):
    X = df.drop(columns=['respondent_id', 'gallbladder_disease'])
    y = df['gallbladder_disease']
    
    # 80/20 Stratified Partitioning preserving 1:8.02 epidemiological ratio
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test
