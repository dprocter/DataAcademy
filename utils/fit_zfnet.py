"""
Fits the ZFnet CNN architecture
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Activation,
    Flatten,
    Dense,
    Dropout,
    BatchNormalization
)
from tensorflow.keras.metrics import BinaryAccuracy, AUC

def fit_zfnet(train, val, epochs, save_path):
    """
    define and fit a CNN, pretty basic architecture
    """
    cnn = Sequential()
    cnn.add(
        Conv2D(
            filters=96,
            kernel_size=(7, 7),
            strides=(2, 2),
            input_shape=(218, 178, 3),
            data_format="channels_last",
        )
    )
    cnn.add(Activation("relu"))
    cnn.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding = "same"))
    cnn.add(BatchNormalization(axis = 3))

    cnn.add(Conv2D(filters=256, kernel_size=(5, 5), strides=(4, 4)))
    cnn.add(Activation("relu"))
    cnn.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding = "same"))
    cnn.add(BatchNormalization(axis=3))

    cnn.add(Conv2D(filters=512, kernel_size=(3, 3), strides=(1, 1), padding = "same"))
    cnn.add(Activation("relu"))
    cnn.add(Conv2D(filters=1024, kernel_size=(3, 3), strides=(1, 1), padding = "same"))
    cnn.add(Activation("relu"))
    cnn.add(Conv2D(filters=512, kernel_size=(3, 3), strides=(1, 1), padding = "same"))
    cnn.add(Activation("relu"))
    cnn.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding = "same"))

    cnn.add(Flatten())
    cnn.add(Dense(256))
    cnn.add(Activation("relu"))
    cnn.add(Dense(256))
    cnn.add(Activation("relu"))
    cnn.add(Dropout(0.25))
    cnn.add(Dense(11))
    cnn.add(Activation("sigmoid"))
    cnn.compile(loss="binary_focal_crossentropy", optimizer="adam", metrics=[BinaryAccuracy(), AUC(from_logits=True)])

    cnn.fit(train, validation_data=val, epochs=epochs)

    cnn.save(f"{save_path}/fit_model.h5")