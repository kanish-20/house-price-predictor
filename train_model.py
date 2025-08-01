import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df=pd.read_csv('House_dataset.csv')

X=df[['Area','Bedrooms']]
y=df['Price']

model=LinearRegression()
model.fit(X,y)

joblib.dump(model,'model.pkl')
print("Model trained and saved successfully!!..")