from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, BatchNormalization, ZeroPadding2D, Input, concatenate
from keras import Model

from tensorflow.keras.metrics import BinaryAccuracy, AUC
from tensorflow.keras.callbacks import EarlyStopping

def fit_modified_zfnet(train, val, epochs, save_path):

    img_input = Input(shape = (218,178,3))
    x = ZeroPadding2D((3,3))(img_input)
    x = Conv2D(96, (7,7), strides = (2,2), name = "conv1", activation= "relu")(x)
    x = MaxPool2D(pool_size=(3,3), strides = (2,2), padding = "same", name = "pool1")(x)
    x = BatchNormalization(axis = 3, name = "bn_conv1")(x)

    x = Conv2D(256, (4,4), strides = (2,2), name = "conv2", activation = "relu")(x)
    x = MaxPool2D(pool_size=(3,3), strides=(2,2), padding = "same", name="pool2")(x)
    x = BatchNormalization(axis = 3, name = "bn_conv2")(x)

    x = Conv2D(512, (3,3), strides = (1,1), padding="same", name = "conv3", activation="relu")(x)
    #x = Conv2D(1024, (3,3), strides = (1,1), padding="same", name = "conv4", activation="relu")(x)
    #x = Conv2D(512, (3,3), strides = (1,1), padding="same", name = "conv5", activation="relu")(x)
    x = MaxPool2D(pool_size=(3,3), strides=(2,2), padding = "same", name="pool3")(x)

    x = Flatten()(x)

    x= Dense(1024, activation="relu")(x)
    targ1 = Dense(128, activation="relu")(x)
    targ2 = Dense(128, activation="relu")(x)
    targ3 = Dense(128, activation="relu")(x)
    targ4 = Dense(128, activation="relu")(x)
    targ5 = Dense(128, activation="relu")(x)
    targ6 = Dense(128, activation="relu")(x)
    targ7 = Dense(128, activation="relu")(x)
    targ8 = Dense(128, activation="relu")(x)
    targ9 = Dense(128, activation="relu")(x)
    targ10 = Dense(128, activation="relu")(x)
    targ11 = Dense(128, activation="relu")(x)
    targ12 = Dense(128, activation="relu")(x)

    output = concatenate([targ1, targ2, targ3, targ4, targ5, targ6, targ7, targ8, targ9, targ10, targ11, targ12])
    output = Dense(12, activation="sigmoid")(output)

    cnn = Model(inputs = img_input, outputs = output, name = "ZFNet")

    cnn.compile(optimizer = "Adam", loss = "binary_focal_crossentropy", metrics=[BinaryAccuracy(), AUC(from_logits=True)])

    es = EarlyStopping(patience = 5)

    cnn.fit(train, validation_data=val, epochs=epochs, callbacks = [es])

    cnn.save(f"{save_path}/fit_mutlilabel_model.h5")