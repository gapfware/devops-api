from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.category import router as category_router
from middleware.error_handler import ErrorHandler


app = FastAPI()

app.add_middleware(ErrorHandler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(category_router, prefix='/categories', tags=['categories'])


@app.get("/")
def read_root():
    return {"Hello": "World"}
