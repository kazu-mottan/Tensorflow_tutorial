from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Activation,Dropout,Dense
from keras.utils import up_utils

# 変数の制限
classes = 3
data_size = 75 * 75 * 3

def main():
    data = np.load("./photo-min.npz")
    x = data["x"]
    y = data["y"]
    x = np.reshape(x,(-1,data_size))
    x_train,x_test,y_train,y_test = train_test_split(x,y)
    model = trann(x_train,y_train)
    model_eval(model,x_test,y_test)

def train(x,y):
    model = Sequential()
    model.add(Dense(units=64,input_dim=(data_size)))
    model.add(Activation('relu'))
    model.add(Dense(units=classes))
    model.add(Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
    model.fit(x,y,epochs=60)
    return model
def model_eval(model,x_test,y_test):
    score = model.evaluate(x_test,y_test)
    print('loss=',score[0])
    print('accuracy=',score[1])
if __name__ == "__main__":
    main()
    