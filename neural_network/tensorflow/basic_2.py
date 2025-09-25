from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model

def create_model_functional():
  inp = Input(shape=(28, ))
  h1 = Dense(64, activation="relu", name="hidden_1")(inp)
  h2 = Dense(512 , activation="relu", name="hidden_2")(h1)
  out = Dense(4, activation="softmax", name="output")(h2)
  model = Model(inputs=inp, outputs=out, name="simple_nn")

  return model

model_functional = create_model_functional()
model_functional.summary()