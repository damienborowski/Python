from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm,time

#Load data
X_train,y_train,X_test, y_test = lstm.load('sp500.csv',50,True)

#Building model
print(X_train)