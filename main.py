from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

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

@app.api_route("/process-pdf", methods=["GET", "POST", "OPTIONS"])
@app.api_route("/process-pdf/", methods=["GET", "POST", "OPTIONS"])
async def process_pdf(
    request: Request,
    files: Optional[UploadFile] = File(None)
):

    if files:
        return {
            "status": "sucesso",
            "arquivo_recebido": files.filename,
            "method": request.method
        }

    return {
        "status": "erro",
        "mensagem": "nenhum arquivo recebido",
        "method": request.method
    }