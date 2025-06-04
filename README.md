# 🌱 Carbon Footprint Predictor

### AI/ML Entry-Level Assessment Project by Basit Bashir Wani

---

## 📂 Dataset Used

* **Name:** Carbon Footprint.csv
* **Source:** Random dataset from web
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
* Checked for missing values and handled them appropriately.

* Developed a reusable preprocessing pipeline that:
  * Handled missing values using a median imputation strategy with SimpleImputer(strategy="median")

  * Encodes categorical variables (like Transport Mode) with OneHotEncoder

  * Scales numerical features using StandardScaler(for linear regressor)

* This pipeline ensures streamlined and consistent data handling for training and inference.
### 2. Model Building

* Implemented a **Decision Tree Regressor** to predict carbon footprint.
* Performed hyperparameter tuning using RandomizedSearchCV with the following parameter distributions:
  * criterion: ['squared_error', 'friedman_mse']
  * splitter: ['best', 'random']
  * max_depth: integers from 3 to 20
  * max_features: ['sqrt', 'log2', None]

* This comprehensive tuning helped optimize model performance and prevent overfitting.


### 3. Evaluation

* Used metrics:
   * Before Hyper Parameter Tunning: 
     * R² Score: 0.6720282827473432
     * Mean Squared Error (MSE): 472588.8262195122
     * Root Mean Squared Error (RMSE): 687
   * After Hyper Parameter Tunning: 
     * R² Score: 0.7404797613009263
     * Mean Squared Error (MSE): 373954.0897440275
     * Root Mean Squared Error (RMSE): 611
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
