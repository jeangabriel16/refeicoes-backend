from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online"}

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):

    return {
        "arquivo_recebido": file.filename,
        "status": "backend funcionando"
    }