from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online"}

@app.post("/process")
async def process_pdf(files: UploadFile = File(...)):

    return {
        "arquivo_recebido": files.filename,
        "status": "backend funcionando"
    }