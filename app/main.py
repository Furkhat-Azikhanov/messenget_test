from fastapi import FastAPI

app = FastAPI(title="Messenger App")

@app.get("/")
async def root():
    return {"message": "Hello from Messenger!"}
