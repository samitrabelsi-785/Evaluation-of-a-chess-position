from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import conversion
import numpy as np

donnees = open("C:\\Users\\samit\\OneDrive\\Desktop\\code\\projet ia echecs\\output.csv").readlines()
donnees = [line.strip().split(",") for line in donnees]
print(donnees.pop(0)) #Enlève la première ligne qui contient les titres des colonnes
for i in range(len(donnees)):
    donnees[i] = conversion.conversionall(donnees[i][0]) + donnees[i][1:]
    for j in range(1, len(donnees[i])):
        donnees[i][j] = int(donnees[i][j])

infos,resultats = [ligne[:-1] for ligne in donnees], [ligne[-1] for ligne in donnees]

X_train,X_test,y_train,y_test = train_test_split(infos, resultats, test_size=0.2, random_state=42)

print("x_train_sample: ", X_train[0:10])
print("------------------------------------")
print("y_train_sample: ", y_train[0:10])
print("------------------------------------")
print("x_test_sample: ", X_test[0:10])
print("------------------------------------")
print("y_test_sample: ", y_test[0:10])


X_train = np.array(X_train)
X_test  = np.array(X_test)
y_train = np.array(y_train)
y_test  = np.array(y_test)


clf_lr = LinearRegression() 

clf_lr.fit(X_train, y_train) 
print(X_train.shape)

print(f"intercept: {clf_lr.intercept_}")
print(f"weights:   {clf_lr.coef_}")

t = X_test[:1,:] # build array only containing the first example from test using slicing
pred = clf_lr.predict(t) 

t_pred = pred[0]
print(f"Prediction: {t_pred}")


# Let's compute the error the model performs on the training and test sets
# We can use the score() function to do so
train_score = clf_lr.score(X_train,y_train)
test_score = clf_lr.score(X_test,y_test)

print(f"Training set score: {train_score:.2f} ")
print(f"Test set score: {test_score:.2f} ")
