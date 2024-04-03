import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("floods1.csv")
data = data.dropna()
X = data.iloc[:,2:7].values
y = data['flood'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=65)
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_pred,y_test)
print(f'Accuracy: {round(accuracy*100,2)}%')
pickle.dump(svm, open('svmmodel.pkl','wb'))