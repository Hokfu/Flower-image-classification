import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('vgg16_v2_10_0.874.h5')

converter = tf.lite.TFLiteConverter.from_saved_model(model)

tflite_model = converter.convert()

with open('flower_classification_model.tflite', 'wb') as f_out:
    f_out.write(tflite_model)