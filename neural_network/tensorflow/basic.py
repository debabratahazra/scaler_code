import tensorflow as tf 

model = tf.keras.models.Sequential()

# Create model
model.add(tf.keras.layers.Input(shape=(32, )))
model.add(tf.keras.layers.Dense( 512 , activation='relu'))
model.add(tf.keras.layers.Dense( 10, activation='softmax'))

model.summary()