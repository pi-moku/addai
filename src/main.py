import pandas as pd
import warnings

df = pd.read_csv('main.csv')

xcol = ['足される数','足す数']
x = df[xcol]
t = df['答え']

from sklearn import tree
warnings.simplefilter('ignore')
model = tree.DecisionTreeClassifier(max_depth=2, random_state=0)
model.fit(x,t)

print('AI電卓')
while True:
    s = input('足される数 ')
    y = input('足す数 ')
    test = [[s,y]]
    print(model.predict(test))
