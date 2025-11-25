from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def hello(name: str, message: str):
    return Response(
        content=f"Hello {name}! {message}!",
        media_type="text/plain"
    )
