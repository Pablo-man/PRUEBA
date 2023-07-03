from typing import Union

from fastapi import FastAPI
from desarrollo.modelo.openAIModel import Document, inference
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#PUERTO CAMBIADO POR DEFECTO DE 8000 -> 9053 (MEDIANTE LA CONFIGURACIÓN DEL ARCHIVO MAIN QUE SE
# ENCUENTRA EN LA CARPETA DEL ENTORNO VIRTUAL DEL PROYECTO)


#ENDPOINT TIPO POST
@app.post('/inference')
def inference_endpoint(doc: Document):
    response= inference(doc.prompt)
    return {
        'calculo': response[0],
        'tokkens utilizados': response[1]
    }