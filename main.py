from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# LIBERA ACESSO DO BASE44
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

@app.post("/process")
async def process_pdf(files: UploadFile = File(...)):

    return {
        "arquivo_recebido": files.filename,
        "status": "backend funcionando"
    }