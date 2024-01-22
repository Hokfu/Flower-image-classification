import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('vgg16', target_size=(150, 150))


interpreter = tflite.Interpreter(model_path='flower_classification_model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

# url = 'https://cdn.jwplayer.com/v2/media/C5w8jfIE/poster.jpg?width=720'

classes = ['daisy','dandelion']
def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    preds = 1 if (preds>=0.5) else 0
    
    return classes[preds]


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result