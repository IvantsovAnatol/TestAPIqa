from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import create_tables, answers, questions


@asynccontextmanager
async def lifespan(app: FastAPI):

    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(questions.router)
app.include_router(answers.router)