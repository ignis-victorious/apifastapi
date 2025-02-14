#  ##   ###
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ##   ###


app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    #  Import FILES LIBRARIES
    uvicorn.run(app, host="0.0.0.0", port=8000)
