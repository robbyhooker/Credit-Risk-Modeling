# Credit Risk Modeling for Prediction

## Project Overview

This project aims to develop a statistical model to predict loan defaults based on borrower information. In deployment, the model could help financial institutions assess the risk associated with lending to various applicants, thereby reducing potential financial losses.

## Table of Contents

1. [Dataset Description](#dataset-description)
2. [Data Preprocessing](#data-preprocessing)
3. [Feature Engineering](#feature-engineering)
4. [Model Building](#model-building)
5. [Model Evaluation](#model-evaluation)
6. [Model Deployment](#model-deployment)
7. [API Usage](#api-usage)
8. [Results and Insights](#results-and-insights)
9. [Future Work](#future-work)
10. [Setup and Installation](#setup-and-installation)
11. [Usage](#usage)
12. [Contributing](#contributing)
13. [License](#license)
14. [Acknowledgements](#acknowledgements)

## Dataset Description

The dataset used in this project is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets). It includes features such as age, income, employment length, loan amount, loan interest rate, and others. The target variable is whether the borrower defaulted on the loan.

### Features

- `person_age`: Age of the borrower
- `person_income`: Annual income of the borrower
- `person_emp_length`: Length of employment in years
- `loan_amnt`: Loan amount requested
- `loan_int_rate`: Interest rate on the loan
- `loan_percent_income`: Percentage of income that goes towards loan payments
- `cb_person_cred_hist_length`: Length of credit history in years
- `person_home_ownership`: Home ownership status (OWN, RENT, MORTGAGE, OTHER)
- `loan_intent`: Purpose of the loan (EDUCATION, HOMEIMPROVEMENT, MEDICAL, PERSONAL, VENTURE)

## Data Preprocessing

### Steps Taken

1. **Handling Missing Values**: Missing values were imputed using median or mode values.
2. **Outlier Removal**: Outliers in numerical features were removed using the IQR method.
3. **Encoding Categorical Variables**: Categorical variables were encoded using one-hot encoding.

## Model Building

Multiple models were built and compared, including:
- Logistic Regression
- Decision Tree
- Random Forest

Hyperparameter tuning was performed using GridSearchCV to find the best parameters for the randon forest model.

## Model Evaluation

Models were evaluated using various metrics:
- **Confusion Matrix**: To visualize the performance in terms of true positives, true negatives, false positives, and false negatives.
- **ROC Curve**: To evaluate the model's ability to distinguish between classes.
- **AUC Score**: To quantify the overall performance.

### Model Performance

- **Logistic Regression**: ROC AUC = X.XX
- **Decision Tree**: ROC AUC = X.XX
- **Random Forest**: ROC AUC = X.XX (Best Performing Model)

### Request Example

```json
 {
  "person_age": 45,
  "person_income": 55000,
  "person_emp_length": 2,
  "loan_amnt": 15000,
  "loan_int_rate": 11.25,
  "loan_percent_income": 0.170203,
  "cb_person_cred_hist_length": 3,
  "person_home_ownership_OTHER": 0, 
  "person_home_ownership_OWN": 1,
  "person_home_ownership_RENT": 0, 
  "loan_intent_EDUCATION": 1,
  "loan_intent_HOMEIMPROVEMENT": 0, 
  "loan_intent_MEDICAL": 0,
  "loan_intent_PERSONAL": 0, 
  "loan_intent_VENTURE": 0,
  "loan_grade_B": 1,
  "loan_grade_C": 0,
  "loan_grade_D": 0,
  "loan_grade_E": 0,
  "loan_grade_F": 0,
  "loan_grade_G": 0,
  "cb_person_default_on_file_Y": 0
}

Response:</br>
Model Default Prediction: 0 (non-default) </br>
Model Confidence in Prediction: 0.95%
