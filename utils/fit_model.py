"""
define and fit CNN
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Activation,
    Flatten,
    Dense,
    Dropout,
)


def fit_model(train, val, epochs, save_path):
    """
    define and fit a CNN, pretty basic architecture
    """
    cnn = Sequential()
    cnn.add(
        Conv2D(
            filters=32,
            kernel_size=(2, 2),
            strides=(1, 1),
            padding="same",
            input_shape=(218, 178, 3),
            data_format="channels_last",
        )
    )
    cnn.add(Activation("relu"))
    cnn.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    cnn.add(Conv2D(filters=64, kernel_size=(2, 2), strides=(1, 1), padding="valid"))
    cnn.add(Activation("relu"))
    cnn.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    cnn.add(Flatten())
    cnn.add(Dense(64))
    cnn.add(Activation("relu"))
    cnn.add(Dropout(0.25))
    cnn.add(Dense(11))
    cnn.add(Activation("sigmoid"))
    cnn.compile(loss="binary_focal_crossentropy", optimizer="adam", metrics=["accuracy"])

    cnn.fit(train, validation_data=val, epochs=epochs)

    cnn.save(f"{save_path}/fit_model")
