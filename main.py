# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
import tensorflow as tf
import PIL
import os
import numpy as np
from PIL import Image
from flask import Flask, request
from flask_basicauth import BasicAuth
from tensorflow.keras.models import load_model

# COnfiguração do Flask
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

# Habilitando autenticação
basic_auth = BasicAuth(app)

# Rotas

## Rota 1
@app.route('/diagnostico/', methods=['POST'])
@basic_auth.required
def diagnostico():
    # Recebe o arquivo em formato Stream
    file = request.files['image']
    # Abre o arquivo e converte para Image PIL
    img = Image.open(file.stream)
    # Redimensiona a imagem para o tamanho da entrada do modelo
    img = img.resize((250,250))
    #image2 = tf.keras.preprocessing.image.load_img(Image.open(file.stream),color_mode="rgb",target_size=(250,250))
    # Converte a imagem em um Ndarray
    input_array = tf.keras.preprocessing.image.img_to_array(img)
    # Ajuste para entrada do modelo
    input_array = np.array([input_array])
    # Carrega o modelo
    modelo = load_model('model.h5')
    # Efetua a predição
    predicao = modelo.predict(input_array)
    diag = f"Glioma {predicao[0][0]:0.3f}, Meningioma {predicao[0][1]:0.3f}, No Tumor {predicao[0][2]:0.3f}, Pituitaria {predicao[0][3]:0.3f}"
    return f"O Diagnóstico é {diag}"
    

## Rota Padrão
@app.route('/', methods=['POST'])
def home():
    return 'API de Diagnóstico'




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")

#app.run(debug=True,host="0.0.0.0")
