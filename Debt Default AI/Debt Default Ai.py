import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

# 데이터 불러오기
train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")

# 🔍 UID 확인 (파일 불러온 직후)
print("🔹 test.csv에서 UID 확인 (처음 5개):")
print(test[["UID"]].head())

# 숫자형 컬럼만 결측값 처리
num_cols = train.select_dtypes(include=[np.number]).columns
num_cols_test = [col for col in num_cols if col in test.columns]

train[num_cols] = train[num_cols].fillna(train[num_cols].median())
test[num_cols_test] = test[num_cols_test].fillna(test[num_cols_test].median())

# 🔄 UID 인코딩에서 제외하고 문자형 데이터 변환
cat_cols = train.select_dtypes(include=["object"]).columns
label_encoders = {}

# UID를 제외한 문자형 컬럼만 인코딩
cat_cols = cat_cols.drop("UID", errors='ignore')

for col in cat_cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    if col in test.columns:  
        test[col] = test[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])  
        test[col] = le.transform(test[col])  
    label_encoders[col] = le  

# 🔍 UID 변형 여부 확인 (전처리 후)
print("🔹 UID 변형 여부 확인 (전처리 후):")
print(test[["UID"]].head())

# UID를 문자열로 유지
test["UID"] = test["UID"].astype(str)

# 입력 변수(X)와 타겟 변수(y) 분리
X = train.drop(columns=["UID", "채무 불이행 여부"])  
y = train["채무 불이행 여부"]
X_test = test.drop(columns=["UID"])

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)

# 학습 데이터 분할
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 랜덤포레스트 모델 기본 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 검증 데이터 평가
val_preds = model.predict_proba(X_val)[:, 1]
print("Validation AUC (기본 모델):", roc_auc_score(y_val, val_preds))

# 모델 하이퍼파라미터 튜닝
param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None]  
}

random_search = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_distributions=param_dist, n_iter=10, cv=3, random_state=42)
random_search.fit(X_train, y_train)

# 최적 하이퍼파라미터 출력
print("Best parameters:", random_search.best_params_)
best_model = random_search.best_estimator_

# 최적 모델로 검증 데이터 평가
val_preds_best = best_model.predict_proba(X_val)[:, 1]
print("Validation AUC (최적 모델):", roc_auc_score(y_val, val_preds_best))

# 테스트 데이터 예측 및 제출 파일 생성
test_preds = best_model.predict_proba(X_test_scaled)[:, 1]

# 제출 파일 생성
submission = pd.DataFrame({"UID": test["UID"], "채무 불이행 확률": test_preds})

# 🔍 최종 제출 데이터 확인
print("🔹 최종 제출 데이터 확인 (상위 5개):")
print(submission.head())

# CSV 저장
submission.to_csv("submission.csv", index=False)
print("✅ 최종 제출 파일이 'submission.csv'로 저장되었습니다.")
