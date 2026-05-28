print("VERSAO NOVA PROCESS-PDF")

from fastapi import FastAPI, UploadFile, File
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

@app.post("/process-pdf")
async def process_pdf_route(file: UploadFile = File(...)):

    return {
        "message": "File processed successfully",
        "filename": file.filename
    }