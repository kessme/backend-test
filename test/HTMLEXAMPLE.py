from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(
    title="sexapi"
)
@app.get("/")
async def root():
    return FileResponse("index.html")
