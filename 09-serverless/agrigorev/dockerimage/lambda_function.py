#import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite
import json
import os
import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image

file_path = "model_2024_hairstyle_v2.tflite"

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def prepare_input(x):
    return x / 255.0

interpreter = tflite.Interpreter(model_path=file_path)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

# url = "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"

def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(200, 200))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    
    preds = interpreter.get_tensor(output_index)

    # return float(preds[0,0])
    result = float(preds[0][0])
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result