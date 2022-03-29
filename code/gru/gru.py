import numpy
from tensorflow import keras
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM, GRU, SimpleRNN, Activation
from keras.layers import Dropout
from keras.regularizers import l2
import numpy as np
from keras import optimizers


class GRUModel(object):
    def __init__(self, inputDim, hiddenNum, outputDim, lr):
        self.inputDim = inputDim
        self.hiddenNum = hiddenNum
        self.outputDim = outputDim
        self.opt = optimizers.rmsprop_v2.RMSProp(lr=lr, rho=0.9, epsilon=1e-06)
        self.buildModel()

    def buildModel(self):
        self.model = Sequential()
        self.model.add(GRU(self.hiddenNum, input_shape=(None, self.inputDim), return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(GRU(self.hiddenNum, input_shape=(None, self.inputDim)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(self.outputDim))
        self.model.add(Activation("tanh"))
        self.model.compile(loss='mean_squared_error', optimizer=self.opt)

    def train(self, trainX, trainY, epoch, batchSize):
        self.model.fit(trainX, trainY, epochs=epoch, batch_size=batchSize, verbose=1, validation_split=0.0)

    def predict(self, testX):
        pred = self.model.predict(testX)
        return pred

    # def predictVarLen(self, vtestX, minLen, maxLen, step):
    #     lagNum = (maxLen-minLen) // step + 1
    #     predAns = []
    #     pred = self.model.predict(vtestX)
    #     for i in range(0, len(pred), lagNum):
    #         predAns.append(np.mean(pred[i:i+lagNum]))
    #     return np.array(predAns)
