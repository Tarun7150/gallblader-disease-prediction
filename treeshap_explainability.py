"""TreeSHAP explainability module for global and patient-level explanations."""
import shap
import matplotlib.pyplot as plt
import numpy as np

def compute_treeshap_values(model, X_train, X_test):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(X_test)
    return explainer, shap_values

def plot_shap_summary(shap_values, X_test, save_path="figures/shap_summary.png"):
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values.values, X_test, show=False)
    plt.title("Dual-Tier TreeSHAP Global Biomarker Beeswarm", fontsize=14, pad=15)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_patient_waterfall(shap_values, patient_idx=0, save_path="figures/shap_waterfall.png"):
    plt.figure(figsize=(9, 6))
    shap.plots.waterfall(shap_values[patient_idx], show=False)
    plt.title(f"Patient-Level Local TreeSHAP Waterfall Attribution (Sample #{patient_idx})", fontsize=13, pad=15)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
