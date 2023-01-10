import json
from fastapi import FastAPI, Query, HTTPException, Path
from pydantic import BaseModel

from transformers import pipeline
#from extractive_summarizer import Word2VecSummarizer

path_model = '/setneg-dir-02/saas-socmed/dev-nlp/unusual/Unusual_v2'
classifier = pipeline('sentiment-analysis', model = path_model)

def predict_class(title):
    cek_class = classifier(title)
    
    if cek_class[0]['label'] == 'LABEL_0':
        return('False')
    else:
        return('True')
    

app = FastAPI()

class News_unusual(BaseModel):
#    id: Optional[int] = None
    title: str

@app.post("/predict_unusual", status_code = 200)
async def predict_result(Items : News_unusual):
    label = predict_class(Items.title)
    return { "Unusual" : label}

if __name__ == '__main__':
    uvicorn.run("api_unusual:app", host='172.17.61.220', port=2012)


