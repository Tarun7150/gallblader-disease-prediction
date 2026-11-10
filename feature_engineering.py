"""Feature engineering module for domain-specific clinical ratios."""
import pandas as pd
import numpy as np

def engineer_clinical_features(df):
    df_feat = df.copy()
    
    # 1. Direct-to-Total Bilirubin Ratio (Post-hepatic ductal stasis)
    df_feat['direct_bilirubin_ratio'] = np.where(
        df_feat['total_bilirubin'] > 0,
        df_feat['direct_bilirubin'] / df_feat['total_bilirubin'],
        0.0
    )
    
    # 2. Lithogenic Index (Non-HDL to HDL Ratio)
    df_feat['lithogenic_index'] = np.where(
        df_feat['hdl_cholesterol'] > 0,
        df_feat['non_hdl_cholesterol'] / df_feat['hdl_cholesterol'],
        0.0
    )
    
    # 3. Canalicular Cholestatic Interaction (ALP * GGT)
    df_feat['canalicular_cholestatic_score'] = np.sqrt(
        df_feat['alkaline_phosphatase'] * df_feat['gamma_glutamyl_transferase']
    )
    
    return df_feat
