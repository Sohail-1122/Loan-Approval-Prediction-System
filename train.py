import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from src.logger import logger

# =====================================================
# LOAD DATA
# =====================================================

logger.info("Loading dataset...")

df = pd.read_csv("loan_data.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

logger.info(f"Dataset Shape: {df.shape}")

# =====================================================
# DROP UNNECESSARY COLUMN
# =====================================================

if "loan_id" in df.columns:
    df.drop("loan_id", axis=1, inplace=True)

# =====================================================
# ENCODE CATEGORICAL COLUMNS
# =====================================================

logger.info("Encoding categorical columns...")

label_encoders = {}

for col in df.select_dtypes(include=["object", "string"]).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

    if col == "loan_status":
        print(
            "Loan Status Mapping:",
            dict(zip(le.classes_, le.transform(le.classes_)))
        )


# =====================================================
# FEATURES AND TARGET
# =====================================================

X = df.drop("loan_status", axis=1)
y = df["loan_status"]

print("\nFeature Columns:")
print(X.columns.tolist())

print("\nTarget Distribution:")
print(y.value_counts())

print("\nUnique Target Values:")
print(y.unique())

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

logger.info("Train-Test Split Completed")

# =====================================================
# SCALING
# =====================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

logger.info("Scaler Saved Successfully")

# =====================================================
# LOGISTIC REGRESSION
# =====================================================

logger.info("Training Logistic Regression...")

log_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

log_model.fit(
    X_train_scaled,
    y_train
)

joblib.dump(
    log_model,
    "models/logistic_model.pkl"
)

logger.info("Logistic Regression Saved")

# =====================================================
# SVM
# =====================================================

logger.info("Training SVM...")

svm_model = SVC(
    probability=True,
    kernel="rbf",
    random_state=42
)

svm_model.fit(
    X_train_scaled,
    y_train
)

joblib.dump(
    svm_model,
    "models/svm_model.pkl"
)

logger.info("SVM Model Saved")

# =====================================================
# DEBUGGING OUTPUT
# =====================================================

print("\nSVM Classes:")
print(svm_model.classes_)

print("\nTraining Completed Successfully!")

logger.info("Training Completed Successfully")