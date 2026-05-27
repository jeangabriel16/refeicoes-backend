from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "online"}

@app.api_route("/process", methods=["GET", "POST", "PUT", "OPTIONS"])
async def process_pdf(request: Request):

    print("METHOD:", request.method)

    return {
        "status": "ok",
        "method": request.method
    }