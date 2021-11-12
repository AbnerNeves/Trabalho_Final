# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb
#from util import get_resampling
import pickle
import tensorflow as tf
import PIL
import numpy as np
from PIL import Image

from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth



def load_model():
    from tensorflow.keras.models import load_model
    return load_model('model.h5')

app = Flask(__name__)
# Rotas

## Rota 1
@app.route('/diagnostico/', methods=['POST'])
def diagnostico():
    file = request.files['image']
    img = Image.open(file.stream)
    img = img.resize((250,250))
    #image2 = tf.keras.preprocessing.image.load_img(Image.open(file.stream),color_mode="rgb",target_size=(250,250))
    input_array = tf.keras.preprocessing.image.img_to_array(img)
    input_array = np.array([input_array])
    modelo = load_model()
    predicao = modelo.predict(input_array)
    print(predicao)
    return f"O Diagnótico é "

## Rota Padrão
@app.route('/', methods=['POST'])
def home():
    return 'API de Diagnóstico'

app.run(debug=True,host="0.0.0.0")
