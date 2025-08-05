import sys
from sklearn.linear_model import LinearRegression


with open("trainingdata.txt", 'r') as f:
    lines = f.readlines()
    
X = []
y = []
    
for line in lines:
    a, b = map(float, line.strip().split(","))
    if a == 0.0 and b == 0.0:
        continue
    if b < 8.0:  
        X.append([a])  
        y.append(b)
    
model = LinearRegression()
model.fit(X,y)

if __name__ == '__main__':
    timeCharged = float(input().strip())
    pred = model.predict([[timeCharged]])[0]
    print(f"{min(pred, 8.0):.2f}")