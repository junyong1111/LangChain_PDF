import os
import uuid
import json
from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import asyncio
import logging
from datetime import datetime, timedelta
import aiofiles
import hashlib
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class PDFService:
    @staticmethod
    async def save_pdf(self, file: UploadFile):
        try:
            file_id = str(uuid.uuid4())
            file_name = f"{file_id}_{file.filename}"
            file_location = os.path.join(self.UPLOAD_DIRECTORY, file_name)

            logger.info(f"Attempting to save file: {file_name}")
            async with aiofiles.open(file_location, "wb") as out_file:
                content = await file.read()
                await out_file.write(content)

            logger.info(f"PDF saved successfully: {file_id} at location: {file_location}")

            self.processing_status[file_id] = "Uploaded"
            self.update_status_expiry(file_id)
            self.save_status_info()
            logger.info(f"Status updated for file_id: {file_id}. Status: Uploaded")

            logger.info(f"Starting background processing for file_id: {file_id}")
            asyncio.create_task(self.process_pdf(file_location, file_id))

            return {"file_id": file_id, "file_location": file_location}
        except Exception as e:
            logger.error(f"Error saving PDF: {str(e)}")
            raise
