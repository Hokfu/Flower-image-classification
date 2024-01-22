from flask import Flask
from flask import request
from flask import jsonify
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor('vgg16', target_size=(150, 150))


interpreter = tflite.Interpreter(model_path='flower_classification_model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = ['daisy','dandelion']

app = Flask("flower_classification")
@app.route("/predict",methods=['POST'])

def predict():
    url = request.get_json()
    print(url)
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    preds = 1 if (preds>=0.5) else 0
    result = {
        "flower_type" : str(classes[preds])
    }
    return jsonify(result)
    
    

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=9696)