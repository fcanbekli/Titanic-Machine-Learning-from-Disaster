import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn import metrics

x_train = pd.read_csv("./data/train.csv")
y_train = x_train.iloc[:, 1]
x_test = pd.read_csv("./data/test.csv")
y_test = pd.read_csv("./data/gender_submission.csv").Survived.values

x_test = x_test.drop('Name', axis=1)
x_test = x_test.drop('Ticket', axis=1)
x_test = x_test.drop('Cabin', axis=1)
x_test = x_test.drop('Embarked', axis=1)

x_train = x_train.drop('Name', axis=1)
x_train = x_train.drop('Ticket', axis=1)
x_train = x_train.drop('Cabin', axis=1)
x_train = x_train.drop('Embarked', axis=1)
x_train = x_train.drop('Survived', axis=1)

labelEncoder = LabelEncoder()
x_train.iloc[:, 2] = labelEncoder.fit_transform(x_train.iloc[:, 2])
x_test.iloc[:, 2] = labelEncoder.fit_transform(x_test.iloc[:, 2])

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)


imputer = SimpleImputer(missing_values = np.nan,
                        strategy ='mean')

imputer = imputer.fit(x_train)
x_train = imputer.transform(x_train)

imputer = imputer.fit(x_test)
x_test = imputer.transform(x_test)

classifier = RandomForestClassifier(n_estimators=20, random_state=2)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
y_pred = pd.DataFrame({'Predictions': y_pred})
y_pred.to_csv('submission.csv' , index=False)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))