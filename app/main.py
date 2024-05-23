from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.category import router as category_router
from app.middleware.error_handler import ErrorHandler
from app.config.database import engine, Base
from fastapi.responses import RedirectResponse



app = FastAPI(
    title="Devops API",
    version="0.1",
)
Base.metadata.create_all(bind=engine)

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
    return RedirectResponse(url="/docs")
