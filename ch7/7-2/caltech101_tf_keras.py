import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
import numpy as np
from PIL import Image
import os

categories = ["chair", "camera", "butterfly", "elephant", "flamingo"]
nb_classes = len(categories)

image_w = 64
image_h = 64

np_load_old = np.load

np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

X_train, X_test, y_train, y_test = np.load("./image/5obj.npy")

np.load = np_load_old

X_train = X_train.astype("float") / 256
X_test = X_test.astype("float") / 256
print("X_train shape:", X_train.shape)

model = Sequential()
model.add(Convolution2D(32, 3, 3, padding='same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, padding='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics='accuracy')

hdf5_file = "./image/5obj-model.hdf5"
if os.path.exists(hdf5_file):
    model.load_weights(hdf5_file)
else:
    model.fit(X_train, y_train, batch_size=32, epochs=50)
    model.save_weights(hdf5_file)

pre = model.predict(X_test)
for i,v in enumerate(pre):
    pre_ans = v.argmax()
    ans = y_test[i].argmax()
    dat = X_test[i]
    if ans == pre_ans:
        continue
    print("[NG]", categories[pre_ans], "!=", categories[ans])
    print(v)
    fname = "image/error/" + str(i) + "-" + categories[pre_ans] + "-ne-" + categories[ans] + ".png"
    dat *= 256
    img = Image.fromarray(np.uint8(dat))
    img.save(fname)

score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])