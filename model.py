import numpy as np
import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('clean_data.csv')

X = df.drop(columns="binaryClass", axis = 1)
Y = df['binaryClass']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify = Y, random_state = 2)

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

model = joblib.load('RandomForestClassifierModel.pkl')

def predict_output(age, sex, on_thyroxine, sick, thyroid_surgery, I131_treatment, query_hypothyroid, query_hyperthyroid, goitre, TSH, T3, TT4, T4U, FTI):
    x = np.zeros(len(X.columns))
    
    x[0] = age
    x[1] = sex
    x[2] = on_thyroxine
    x[3] = sick
    x[4] = thyroid_surgery
    x[5] = I131_treatment
    x[6] = query_hypothyroid
    x[7] = query_hyperthyroid
    x[8] = goitre
    x[9] = TSH
    x[10] = T3
    x[11] = TT4
    x[12] = T4U
    x[13] = FTI
    
    x = sc.transform([x])[0]
    
    return model.predict([x])[0]