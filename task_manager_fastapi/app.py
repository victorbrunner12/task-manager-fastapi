from fastapi import FastAPI

app = FastAPI()


# Task Manager Fast API - First function
@app.get(path="/", status_code=200)
def read_root():
    return {"message": "Hello World!"}
