# Explainable Clinical AI for Non-Invasive Gallbladder Disease Prediction
### Cost-Sensitive Extreme Gradient Boosting with Dual-Tier TreeSHAP

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Rohith-stack-creater/Explainable-Clinical-AI-Gallbladder-Prediction)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Rohith-stack-creater/Explainable-Clinical-AI-Gallbladder-Prediction/blob/main/Explainable_Gallbladder_AI_Pipeline.ipynb)
[![Dataset](https://img.shields.io/badge/Dataset-CDC%20NHANES%20(N%3D6%2C629)-success)](02_Dataset/Dataset_Codebook.md)

---

## 👥 Project Team & Academic Affiliation
- **Kantipudi Venkat Rohith** (Project Lead / Machine Learning & Architecture)
- **Gajjala Karthik Reddy** (Clinical Biochemistry & Feature Engineering)
- **Harsha Lingampalli** (Model Optimization & Evaluation Protocols)
- **Tarun Tej** (TreeSHAP Interpretability & Experimental Validation)

**Institution:** School of Computer Science and Engineering, Vellore Institute of Technology (VIT), Chennai, Tamil Nadu 600127, India.

---

## 📁 Complete Team Project Directory Structure

```text
Gallbladder_Clinical_AI_Complete_Team_Project/
├── 01_Research_Reports/
│   ├── Explainable_Clinical_AI_Gallbladder_15Page_Paper.pdf       # Formal 15-page IEEE Research Paper (PDF)
│   ├── Explainable_Clinical_AI_Gallbladder_15Page_Paper.docx      # Editable 15-page IEEE Review Paper (Word)
│   └── Explainable_Clinical_AI_Gallbladder_IEEE_Review_Draft.docx # Double-column review submission draft
├── 02_Dataset/
│   ├── nhanes_gallbladder_cohort.csv                              # CDC NHANES cohort (N = 6,629 records)
│   └── Dataset_Codebook.md                                        # Clinical variable definitions & baseline stats
├── 03_Source_Code/
│   ├── main.py                                                    # Master execution pipeline
│   ├── requirements.txt                                           # Python dependencies (xgboost, shap, etc.)
│   └── src/
│       ├── __init__.py
│       ├── data_preprocessing.py                                  # Data ingestion & 80/20 stratified split
│       ├── feature_engineering.py                                 # Ductal stasis & lithogenic index ratios
│       ├── model_training.py                                      # Cost-sensitive XGBoost & baseline models
│       ├── evaluate_models.py                                     # Audited metrics & confusion matrix
│       └── treeshap_explainability.py                             # Global & patient-level TreeSHAP plots
├── 04_Google_Colab_Notebook/
│   └── Explainable_Gallbladder_AI_Pipeline.ipynb                  # 1-click interactive Google Colab notebook
├── 05_Publication_Figures/
│   ├── Fig01_System_Architecture.png                              # Five-layer architectural workflow
│   ├── Fig02_Target_Class_Distribution.png                        # Imbalance ratio (1:8.02)
│   ├── Fig03_Biomarker_Correlation_Heatmap.png                    # Clinical biomarker Pearson correlations
│   ├── Fig04_Confusion_Matrix.png                                 # Audited holdout confusion matrix
│   ├── Fig05_Model_Performance_Comparison.png                     # Multi-model benchmarking
│   ├── Fig06_MultiModel_ROC_Curves.png                            # ROC-AUC curves (0.989)
│   ├── Fig07_Precision_Recall_Curves.png                          # PR-AUC curves (0.952)
│   ├── Fig08_Global_TreeSHAP_Summary_Beeswarm.png                 # Global feature attribution beeswarm
│   ├── Fig09_Global_Mean_SHAP_Importance.png                      # Mean absolute SHAP importance rankings
│   └── Fig10_Patient_TreeSHAP_Waterfall.png                       # High-risk patient waterfall profile
├── 06_Colab_Demonstration_Video/
│   └── Explainable_Gallbladder_AI_Colab_Walkthrough.mp4           # 1080p full pipeline walkthrough video
└── README.md                                                      # Project instructions & sharing guide
```

---

## ⚡ Quick Execution Guide

### Option 1: Running in Google Colab (Recommended for Teammates)
1. Open the notebook `04_Google_Colab_Notebook/Explainable_Gallbladder_AI_Pipeline.ipynb` or click the badge above.
2. Select **Runtime -> Run all** (Ctrl+F9).
3. The notebook will automatically download the dataset from GitHub, train the tuned model, output metrics, and render TreeSHAP visualizations.

### Option 2: Running Locally via Terminal
```bash
# 1. Navigate to source directory
cd 03_Source_Code

# 2. Install dependencies
pip install -r requirements.txt

# 3. Execute master pipeline
python main.py
```

---

## 📊 Key Validated Clinical Results (Holdout Test N = 1,326)
- **Accuracy:** 96.61%
- **Sensitivity (Recall / True Positive Rate):** 91.16% (134 / 147 cases detected)
- **Specificity (True Negative Rate):** 97.29% (1,147 / 1,179 healthy controls correctly ruled out)
- **Precision (Positive Predictive Value):** 80.72%
- **F1-Score:** 85.62%
- **ROC-AUC:** 0.989
- **PR-AUC:** 0.952
- **Confusion Matrix:** True Negative: 1,147 | False Positive: 32 | False Negative: 13 | True Positive: 134

---

## 🤝 How to Share with Teammates
1. **Google Drive:** Upload the pre-compressed `Gallbladder_Clinical_AI_Complete_Team_Project.zip` and share the link with edit/view permissions.
2. **WhatsApp / Slack:** Send the `.zip` file directly (it is compressed to a convenient size for direct messaging).
3. **GitHub:** All teammate code is synchronized with the live public repository:  
   `https://github.com/Rohith-stack-creater/Explainable-Clinical-AI-Gallbladder-Prediction`
