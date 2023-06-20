from fastapi import FastAPI

from src.datamodels.model_card_model import ModelCard

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/mc/update")
def read_item(mc: ModelCard):
    return {"name": mc.name}
