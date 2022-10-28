from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, BatchNormalization, ZeroPadding2D, Input
from keras import Model

from tensorflow.keras.metrics import BinaryAccuracy, AUC
from tensorflow.keras.callbacks import EarlyStopping

def fit_multihead(train, val, epochs, save_path):
    """
    Yeah this is called multihead but it is just a multilabel classifier, didn't have time to test out a multihead architecture
    :param train: the train dataset
    :param val: the validation set
    :param epochs: number of epochs to train the model for
    :param save_path: path to save the model out to
    :return:
    """

    img_input = Input(shape = (218,178,3))
    x = ZeroPadding2D((3,3))(img_input)
    x = Conv2D(96, (7,7), strides = (2,2), name = "conv1", activation= "relu")(x)
    x = MaxPool2D(pool_size=(3,3), strides = (2,2), padding = "same", name = "pool1")(x)
    x = BatchNormalization(axis = 3, name = "bn_conv1")(x)

    x = Conv2D(256, (4,4), strides = (2,2), name = "conv2", activation = "relu")(x)
    x = MaxPool2D(pool_size=(3,3), strides=(2,2), padding = "same", name="pool2")(x)
    x = BatchNormalization(axis = 3, name = "bn_conv2")(x)

    x = Conv2D(512, (3,3), strides = (1,1), padding="same", name = "conv3", activation="relu")(x)
    # these convolutions are in zfnet, but reduce image size too much on ours
    #x = Conv2D(1024, (3,3), strides = (1,1), padding="same", name = "conv4", activation="relu")(x)
    #x = Conv2D(512, (3,3), strides = (1,1), padding="same", name = "conv5", activation="relu")(x)
    x = MaxPool2D(pool_size=(3,3), strides=(2,2), padding = "same", name="pool3")(x)

    x = Flatten()(x)

    x= Dense(1024, activation="relu")(x)
    x= Dense(1024, activation="relu")(x)

    out = Dense(12, activation = "sigmoid")(x)

    cnn = Model(inputs = img_input, outputs = out, name = "ZFNet")

    cnn.compile(optimizer = "Adam", loss = "binary_focal_crossentropy", metrics=[BinaryAccuracy(), AUC(from_logits=True)])

    es = EarlyStopping(patience = 5)

    cnn.fit(train, validation_data=val, epochs=epochs, callbacks = [es])

    cnn.save(f"{save_path}/fit_mutlilabel_model.h5")