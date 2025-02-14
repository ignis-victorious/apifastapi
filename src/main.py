#  ##   ###
#  Import LIBRARIES
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
#  Import FILES
#  ##   ###


app = FastAPI()


class Task(BaseModel):
    id: UUID | None = None
    title: str
    description: str | None = None
    completed: bool = False


tasks: list[Task] = []


@app.post("/tasks/", response_model=Task)
def create_task(task: Task) -> Task:
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/tasks/", response_model=list[Task])
def read_tasks() -> list[Task]:
    return tasks


# @app.get("/")
# def read_root() -> dict[str, str]:
#     return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    #  Import FILES LIBRARIES
    uvicorn.run(app, host="0.0.0.0", port=8000)
