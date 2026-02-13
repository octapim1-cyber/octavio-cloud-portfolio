from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	data: str

@app.get("/health")
def health():
	return {"status": "ok"}

@app.post("/predict")
def predict(item: Item):
	# placeholder: echo input (we'll replace with real model later)
	return {"prediction": f"echo: {item.data}"}
