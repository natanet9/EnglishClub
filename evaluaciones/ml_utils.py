import joblib
import os
from django.conf import settings
import numpy as np
import pandas as pd

# Cargar modelo y encoder solo una vez
MODEL_PATH = os.path.join(settings.BASE_DIR, 'Analisis', 'modelo_vark.pkl')
ENCODER_PATH = os.path.join(settings.BASE_DIR, 'Analisis', 'label_encoder.pkl')

modelo = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

def predecir_recurso(visual, auditivo, lectura, kinestesico):
    entrada = pd.DataFrame([{
        'visual': visual,
        'aural': auditivo,
        'read_write': lectura,
        'kinesthetic': kinestesico
    }])
    pred = modelo.predict(entrada)
    return encoder.inverse_transform(pred)[0]
