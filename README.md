# House Price Prediction - End-to-End Machine Learning Project

An end-to-end Machine Learning project that predicts house prices using multiple regression algorithms. The project follows a modular production-style architecture with separate training and prediction pipelines and exposes predictions through a FastAPI REST API.

---

# Features

- Modular project architecture
- Custom logging and exception handling
- Data ingestion pipeline
- Data transformation pipeline
- Scikit-learn Pipeline and ColumnTransformer
- Multiple model training and evaluation
- Automatic best model selection
- Model serialization using Joblib
- Separate training and prediction pipelines
- FastAPI REST API
- Interactive Swagger UI

---

# Project Structure

```text
House-Price-Prediction/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── raw.csv
│   ├── train.csv
│   └── test.csv
│
├── logs/
│
├── src/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── app.py
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# Machine Learning Workflow

```text
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Train/Test Split
      │
      ▼
Data Transformation
      │
      ├── Missing Value Handling
      ├── Standard Scaling
      ├── One Hot Encoding
      └── Feature Transformation
      │
      ▼
Model Training
      │
      ├── Linear Regression
      ├── Decision Tree
      ├── Random Forest
      ├── Gradient Boosting
      └── XGBoost
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
model.pkl
preprocessor.pkl
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Uvicorn
- Joblib
- Pydantic

---

# Models Evaluated

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

The project automatically evaluates every model using the R² score and saves the best-performing model.

---

# Data Preprocessing

### Numerical Features

- Median Imputation
- Standard Scaling

### Categorical Features

- Most Frequent Imputation
- One Hot Encoding
- Unknown Category Handling

Implemented using:

- Pipeline
- ColumnTransformer

---

# Project Components

## Data Ingestion

- Reads dataset
- Splits into train and test sets
- Stores processed CSV files

---

## Data Transformation

- Creates preprocessing pipeline
- Handles missing values
- Encodes categorical features
- Scales numerical features
- Saves `preprocessor.pkl`

---

## Model Trainer

- Trains multiple ML models
- Evaluates each model
- Selects the best-performing model
- Saves `model.pkl`

---

## Train Pipeline

Orchestrates the complete training workflow.

```text
Dataset
   │
   ▼
Data Ingestion
   │
   ▼
Data Transformation
   │
   ▼
Model Trainer
```

---

## Prediction Pipeline

Loads saved artifacts and performs inference.

```text
User Input
      │
      ▼
Preprocessor
      │
      ▼
Model
      │
      ▼
Prediction
```

---

# FastAPI

## Start the API

```bash
uvicorn app:app --reload
```

---

## Swagger Documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

---

## Root Endpoint

```http
GET /
```

Response

```json
{
  "message": "House price prediction API"
}
```

---

## Prediction Endpoint

```http
POST /predict
```

Example Request

```json
{
  "area": 7420,
  "bedrooms": 4,
  "bathrooms": 2,
  "stories": 3,
  "parking": 2,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "no",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "prefarea": "yes",
  "furnishingstatus": "furnished"
}
```

Example Response

```json
{
  "predicted_price": 13542000.0
}
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/chandrasekharaila/house_price_prediction.git
```

Move into the project directory

```bash
cd House-Price-Prediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Train the Model

Run the training pipeline

```bash
python main.py
```

Artifacts generated:

- `artifacts/model.pkl`
- `artifacts/preprocessor.pkl`

---

# Logging

The project includes centralized logging to monitor:

- Data ingestion
- Data transformation
- Model training
- Model evaluation
- Prediction pipeline

---

# Exception Handling

A custom exception module captures detailed information including:

- File name
- Line number
- Error message

This makes debugging significantly easier.

---

# Future Improvements

- Hyperparameter tuning with GridSearchCV / RandomizedSearchCV
- Cross-validation
- MLflow experiment tracking
- Docker support
- CI/CD pipeline
- Cloud deployment
- Model monitoring
- Configuration management using YAML
- Unit and integration tests

---

# Author

Developed as an end-to-end Machine Learning project to demonstrate production-style ML engineering practices, including modular architecture, reusable pipelines, model evaluation, and API deployment.

If you found this project useful, consider giving it a ⭐ on GitHub.
