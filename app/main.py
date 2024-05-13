from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.category import router as category_router



app = FastAPI()

app.include_router(category_router, prefix='/categories', tags=['categories'])



@app.get("/")
def read_root():
    return {"Hello": "World"}
