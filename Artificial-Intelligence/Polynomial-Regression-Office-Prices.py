import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

F, N = map(int, input().split())

train_data = [list(map(float, input().split())) for _ in range(N)]
train_data = np.array(train_data)

X_train = train_data[:, :-1]  
y_train = train_data[:, -1]  

T = int(input())
X_test = [list(map(float, input().split())) for _ in range(T)]
X_test = np.array(X_test)

poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

predictions = model.predict(X_test_poly)

for p in predictions:
    print(round(p, 2))
