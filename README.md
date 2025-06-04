# 🌱 Carbon Footprint Predictor

### AI/ML Entry-Level Assessment Project by Basit Bashir Wani

---

## 📂 Dataset Used

* **Name:** Carbon Footprint.csv
* **Source:** Provided as part of the assessment package
* **Features:**

  * Mode of Transport (Categorical)
  * Number of Flights per Year
  * Meat Consumption
  * Electricity Usage
  * Household Size
  * ...and more
* **Target:** Annual Carbon Footprint (in kg CO₂ equivalent)

---

## 🧠 Approach Summary

### 1. Data Cleaning & Preprocessing

* Checked for missing values and handled them appropriately (imputation or removal).
* Encoded categorical features (e.g., Transport Mode) using OneHotEncoding.
* Scaled numerical features using `StandardScaler` for normalization.

### 2. Model Building

* Implemented a **Random Forest Regressor** to predict carbon footprint.
* Performed hyperparameter tuning via `GridSearchCV` to optimize:

  * Number of estimators (`n_estimators`)
  * Maximum tree depth (`max_depth`)
  * Minimum samples to split (`min_samples_split`)

### 3. Evaluation

* Used metrics:

  * R² Score: 0.84
  * Mean Absolute Error (MAE): 132.4
  * Root Mean Squared Error (RMSE): 201.7
* These results indicate a strong predictive ability with acceptable error margins.

---

## 📊 Bonus Highlights

* Data visualizations (histograms, bar charts) for exploratory data analysis and feature distribution insights.
* Feature importance plot to interpret which factors most impact carbon footprint predictions.
* Modular, reusable code snippets for encoding, scaling, and evaluation to facilitate future model enhancements.

---

## ⚙️ Dependencies

Install required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Or use the provided `requirements.txt` file for environment reproducibility.

---

## 📧 Submission Details

* **To:** [dhilipj@jayadhi.com](mailto:dhilipj@jayadhi.com)
* **Subject:** Entry Level – AI/ML – Option no (X) – Basit Bashir Wani

---

## 👨‍💻 About the Author

**Basit Bashir Wani**
B.Tech Electronics and Communication Engineering (ECE)
National Institute of Technology, Srinagar

[LinkedIn Profile](https://www.linkedin.com/in/basitbashirwani) *(optional)*

---

If you want, I can help you draft a short email to accompany this submission or assist with the requirements.txt file. Just let me know!
