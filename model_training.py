"""Cost-sensitive model training module with XGBoost and baselines."""
import numpy as np
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

def calculate_cost_sensitive_weight(y_train):
    n_neg = (y_train == 0).sum()
    n_pos = (y_train == 1).sum()
    scale_pos_weight = float(n_neg) / float(n_pos)
    return scale_pos_weight

def train_xgboost(X_train, y_train, scale_pos_weight=None):
    if scale_pos_weight is None:
        scale_pos_weight = calculate_cost_sensitive_weight(y_train)
        
    model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.08,
        subsample=0.85,
        colsample_bytree=0.85,
        scale_pos_weight=scale_pos_weight,
        random_state=42,
        eval_metric="logloss"
    )
    model.fit(X_train, y_train)
    return model

def train_baseline_models(X_train, y_train):
    scale_pos_weight = calculate_cost_sensitive_weight(y_train)
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=6, class_weight="balanced", random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, class_weight="balanced", random_state=42),
        "Support Vector Machine": SVC(probability=True, class_weight="balanced", random_state=42)
    }
    trained_models = {}
    for name, clf in models.items():
        clf.fit(X_train, y_train)
        trained_models[name] = clf
    return trained_models
