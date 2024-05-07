from fastapi import FastAPI

import router.router_todo

app = FastAPI(
    title="Todo List",
    docs_url='/',
)

app.include_router(router.router_todo.router)