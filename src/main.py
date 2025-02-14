#  ##   ###
#  Import LIBRARIES
from fastapi import FastAPI, HTTPException
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


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID) -> Task | HTTPException:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task) -> Task | HTTPException:
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            # task.title = task_update.title
            # task.description = task_update.description
            # task.completed = task_update.completed
            # return task
            # updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            updated_task = task.model_copy(
                update=task_update.model_dump(exclude_unset=True)
            )
            tasks[idx] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID) -> Task | HTTPException:
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(idx)
    raise HTTPException(status_code=404, detail="Task not found")


# @app.get("/")
# def read_root() -> dict[str, str]:
#     return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    #  Import FILES LIBRARIES
    uvicorn.run(app, host="0.0.0.0", port=8000)


# {
#   "title": "Task 1",
#   "description": "This the description of Task 1",
#   "completed": false
# }
# {
#   "title": "Task 2",
#   "description": "This the description of Task 2",
#   "completed": true
# }
# {
#   "title": "Task 3",
#   "description": "Hello, this the description of Task 3",
#   "completed": false
# }
#  {
#   "title": "Task 4",
#   "description": "YES, this the description of not Task 3 but Task 4 ",
#   "completed": false
# }
# {
#     "title": "Task 5",
#     "description": "NEW Task 5",
#     "completed": true
# }
