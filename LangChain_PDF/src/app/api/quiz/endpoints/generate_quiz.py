from fastapi import APIRouter, UploadFile, File, HTTPException
from src.app.api.quiz.services.generate_quiz import PDFService
from fastapi.responses import JSONResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
async def health_check():
    return {"message": "It's Working On PDF Controller Service!"}


@router.post("/upload-pdf")
async def store_pdf_to_faiss(
        file: UploadFile = File(...),
):
    try:
        result = await PDFService.store_pdf_to_faiss(file)
        return JSONResponse(content={
            "message": "PDF upload successful. Processing started in background.",
            "file_id": result["file_id"]
        })
    except Exception as e:
        logger.error(f"Error uploading PDF: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during PDF upload")