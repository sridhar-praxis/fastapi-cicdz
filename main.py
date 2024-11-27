from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Update update. Hello, CI/CD with FastAPI!"}
