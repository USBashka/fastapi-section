from contextlib import asynccontextmanager
from fastapi import FastAPI

from src import cache as c



@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    finally:
        await c.shutdown()

app = FastAPI(lifespan=lifespan)


@app.get("/get_last_trading_days")
async def get_last_trading_days(count: int) -> list[str]:
    result: list[str] = []

    return result


@app.get("/get_dynamics")
async def get_dynamics(oil_id: int,
                       delivery_type_id: int,
                       delivery_basis_id: int,
                       start_date: str,
                       end_date: str) -> list:
    result: list = []

    return result


@app.get("/get_trading_results")
async def get_trading_results(oil_id: int,
                              delivery_type_id: int,
                              delivery_basis_id: int) -> list:
    result = []

    return result
