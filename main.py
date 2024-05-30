from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def hello():
    dt_now = datetime.datetime.now()
    print(dt_now)
    return {"message": "TEST DESU YO!!", "date": dt_now.isoformat()}
