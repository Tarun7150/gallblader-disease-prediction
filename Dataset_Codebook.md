# CDC NHANES Gallbladder Disease Cohort Codebook

## Dataset Metadata
- **Source:** Centers for Disease Control and Prevention (CDC) National Health and Nutrition Examination Survey (NHANES)
- **Total Patient Sample (N):** 6,629 adults
- **Class Breakdown:**
  - **Healthy Controls (Class 0):** 5,894 (88.91%)
  - **Gallbladder Disease Cases (Class 1):** 735 (11.09%)
- **Class Imbalance Ratio:** 1 : 8.019 (~1:8.02)
- **Primary Diagnostic Target:** Clinically confirmed or ultrasound-verified gallbladder pathology (cholelithiasis, acute/chronic cholecystitis, biliary obstruction).

## Variable Dictionary

| Field Name | Type | Units | Clinical Description | Controls (Mean ± SD) | Cases (Mean ± SD) | Significance (p-value) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `respondent_id` | Integer | - | Unique NHANES survey respondent identifier | - | - | - |
| `age` | Float | Years | Chronological age at clinical screening | 45.6 ± 16.2 | 54.2 ± 15.1 | p < 0.001 |
| `gender_female` | Binary | 0/1 | Biological sex (1 = Female, 0 = Male) | 49.8% | 66.4% | p < 0.001 |
| `bmi` | Float | kg/m² | Body Mass Index (anthropometric obesity metric) | 28.3 ± 6.4 | 31.7 ± 7.2 | p < 0.001 |
| `total_bilirubin` | Float | mg/dL | Total serum bilirubin concentration | 0.68 ± 0.32 | 0.89 ± 0.45 | p < 0.001 |
| `direct_bilirubin` | Float | mg/dL | Conjugated bilirubin (cholestatic injury indicator) | 0.14 ± 0.08 | 0.24 ± 0.15 | p < 0.001 |
| `alkaline_phosphatase` | Float | IU/L | Serum ALP (biliary canalicular enzyme) | 72.4 ± 24.1 | 96.8 ± 38.6 | p < 0.001 |
| `gamma_glutamyl_transferase` | Float | IU/L | Serum GGT (sensitive hepatobiliary marker) | 26.8 ± 21.4 | 48.5 ± 42.1 | p < 0.001 |
| `hs_crp` | Float | mg/L | High-sensitivity C-Reactive Protein (systemic inflammation) | 2.84 ± 3.92 | 5.62 ± 6.48 | p < 0.001 |
| `hdl_cholesterol` | Float | mg/dL | High-Density Lipoprotein (protective reverse transport) | 54.2 ± 15.6 | 46.1 ± 13.4 | p < 0.001 |
| `non_hdl_cholesterol` | Float | mg/dL | Pro-atherogenic and lithogenic cholesterol fraction | 134.2 ± 39.5 | 152.1 ± 43.8 | p < 0.001 |
| `deritis_ratio` | Float | - | De Ritis Ratio (AST / ALT transaminase balance) | 1.04 ± 0.38 | 1.18 ± 0.44 | p < 0.001 |
| `gallbladder_disease` | Binary | 0/1 | Ground-Truth Diagnostic Label (0 = Control, 1 = Case) | 88.91% | 11.09% | Primary Target |
