from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello Again"}

@app.get("/")
def get_root():
    return {"message": "Hello"}