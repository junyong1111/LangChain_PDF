
import logging
from dotenv import load_dotenv
from src.common.utils.pdf_reader import upload_pdf
from src.common.utils.text_split import chunk_text
from src.common.utils.text_to_embedding import text_to_embedding
from src.common.utils.vector_store import store_embedding_to_faiss

load_dotenv()

logger = logging.getLogger(__name__)

class PDFService:
    @staticmethod
    async def store_pdf_to_faiss(file_path):
        try:
            # -- Spdf 업로드
            documents = await upload_pdf(file_path)
            # -- 청크 단위로 분할
            docs = await chunk_text(documents)
            embeddings = await text_to_embedding()
            await store_embedding_to_faiss(docs=docs, embeddings=embeddings)
        except(Exception) as e:
            raise Exception(f"{file_path.store_pdf_to_faiss.__name__} function raise exception about : {str(e)}") from e