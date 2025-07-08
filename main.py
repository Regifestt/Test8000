from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/apitest1")
async def get_users():
    return {"message": "Hi from backend!"}  # Вернёт JSON: {"message": "Hi from backend!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
