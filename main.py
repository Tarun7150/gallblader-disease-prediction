"""End-to-End Execution Pipeline for Explainable Gallbladder Disease Prediction."""
import os
import sys
from src.data_preprocessing import load_data, clean_and_split_data
from src.feature_engineering import engineer_clinical_features
from src.model_training import train_xgboost, train_baseline_models
from src.evaluate_models import evaluate_classifier

def run_pipeline():
    print("==========================================================================")
    print("Explainable Clinical AI: Gallbladder Disease Prediction Pipeline")
    print("VIT Chennai CSE | Team: Rohith, Karthik, Harsha, Tarun")
    print("==========================================================================")
    
    # 1. Load Data
    data_path = os.path.join(os.path.dirname(__file__), "..", "02_Dataset", "nhanes_gallbladder_cohort.csv")
    if not os.path.exists(data_path):
        data_path = "data/nhanes_gallbladder_cohort.csv"
    print(f"\n[1/4] Loading CDC NHANES Cohort from: {data_path}")
    df = load_data(data_path)
    print(f"      Total records loaded: N = {len(df)} | Columns: {len(df.columns)}")
    
    # 2. Preprocess & Split
    print("\n[2/4] Preprocessing & Stratified 80/20 Train-Test Splitting...")
    X_train, X_test, y_train, y_test = clean_and_split_data(df)
    print(f"      Training partition: N_train = {len(X_train)} (80%)")
    print(f"      Holdout test partition: N_test = {len(X_test)} (20%)")
    
    # 3. Model Training
    print("\n[3/4] Training Proposed Cost-Sensitive XGBoost Classifier...")
    xgb_model = train_xgboost(X_train, y_train)
    print("      Model trained successfully with cost-sensitive scale_pos_weight.")
    
    # 4. Evaluation
    print("\n[4/4] Evaluating on Holdout Test Partition (N_test = 1,326)...")
    metrics = evaluate_classifier(xgb_model, X_test, y_test)
    print("--------------------------------------------------------------------------")
    print(f"  Test Accuracy:     {metrics['Accuracy']*100:.2f}%")
    print(f"  Sensitivity:       {metrics['Sensitivity']*100:.2f}% (True Positive Rate)")
    print(f"  Specificity:       {metrics['Specificity']*100:.2f}% (True Negative Rate)")
    print(f"  Precision:         {metrics['Precision']*100:.2f}%")
    print(f"  F1-Score:          {metrics['F1-Score']*100:.2f}%")
    print(f"  ROC-AUC:           {metrics['ROC-AUC']:.3f}")
    print(f"  PR-AUC:            {metrics['PR-AUC']:.3f}")
    print(f"  Confusion Matrix:  TN={metrics['Confusion_Matrix']['TN']}, FP={metrics['Confusion_Matrix']['FP']}, "
          f"FN={metrics['Confusion_Matrix']['FN']}, TP={metrics['Confusion_Matrix']['TP']}")
    print("--------------------------------------------------------------------------")
    print("Pipeline completed successfully!\n")

if __name__ == "__main__":
    run_pipeline()
