# 🧬 Colorectal Cancer Survival Prediction

This project focuses on developing predictive models for colorectal cancer (CRC) survival using the SEER clinical dataset. Our goal is to accurately predict patient survival outcomes and extract meaningful clinical insights using ensemble machine learning techniques and statistical analysis.

---

## 📌 Overview

Colorectal cancer is one of the leading causes of cancer-related deaths globally. Early detection and accurate survival prediction can significantly improve patient management and treatment planning. This study uses structured clinical data from the SEER dataset to train ensemble-based machine learning models and analyze trends in survival across gender, tumor behavior, and time.

---

## 🧰 Tools & Technologies

- **Python**  
- **Pandas, NumPy, Matplotlib, Seaborn**  
- **Scikit-learn** (RandomForest, AdaBoost, VotingClassifier, etc.)  
- **SMOTE** (for handling class imbalance)  
- **Facebook Prophet** (for time-series survival trend analysis)

---

## 🧪 Methodology

### 1. **Data Preprocessing**
- Extracted clinical variables (tumor size, behavior, sex, diagnosis/death year)
- Handled missing values and normalized continuous features
- Balanced classes using **SMOTE**

### 2. **Feature Selection**
- Applied `SelectKBest` to select the top 10 features
- Validated using **Random Forest feature importance**

### 3. **Model Training**
- Trained multiple models: Random Forest, AdaBoost, Random Subspace
- Combined them using a **VotingClassifier** for better stability and accuracy

### 4. **Evaluation Metrics**
- Accuracy, Precision, Recall, F1-Score
- AUC (Area Under the Curve)
- Confusion Matrix and ROC Curve

---

## 📊 Key Results

- **VotingClassifier achieved 89% accuracy** and **0.91 AUC**
- **Tumor size** was the most important predictor
- Gender-based survival insights:
  - Males: Better outcomes for larger tumors post-surgery
  - Females: Higher survival with early detection and smaller tumors

---

## 📈 Survival Prediction (2022–2024)

| Year | Linear Regression (%) | Prophet (%) | Voting Classifier (%) |
|------|------------------------|-------------|------------------------|
| 2022 | 7.12                   | 0.59        | **8.96**               |
| 2023 | 6.81                   | -1.59       | **8.86**               |
| 2024 | 6.50                   | -3.76       | **8.76**               |

---

## 🔍 Insights

- Most common primary tumor sites: sigmoid colon, cecum, ascending colon
- Tumor size between **1–400 mm** was most prevalent
- Diagnosis trends show decline, while survival is steadily improving

---

## 🧠 Future Work

- 🖼 **Integrate pathology imaging** for multimodal learning
- 🧬 Add genetic/lifestyle risk factors (e.g., UK Biobank data)
- 🧪 Build hybrid models inspired by tools like Harvard’s **MOMA**
- 🧑‍⚕️ Translate models into usable tools for clinical settings

---

## 📷 Suggested Images to Include

Add these images to the `images/` directory and reference them in your README:

1. `feature_importance.png` – Bar plot from RandomForest feature importance
2. `confusion_matrix.png` – Model confusion matrix (from VotingClassifier)
3. `roc_curve.png` – ROC curve showing model performance
4. `survival_trends.png` – Line graph comparing survival predictions over years
5. `tumor_size_distribution.png` – Histogram of tumor size ranges
6. `gender_insights.png` – Graph showing survival rate differences by gender
7. `primary_tumor_sites.png` – Bar chart of tumor site frequencies

---

## 📄 References

- SEER Dataset: [https://seer.cancer.gov](https://seer.cancer.gov)  
- AlAgr13 et al., 2013 – Colon Cancer Survival Prediction Using Ensemble Data Mining  
- Deutelmoser et al., 2020 – Gene Expression in Colon Tissue

---

## 📁 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the main model script
python train_model.py
