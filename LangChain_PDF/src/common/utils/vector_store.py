import numpy as np
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

# API 키 정보 로드
load_dotenv()

DB_INDEX = "MY_ASYNC_DB_INDEX"

async def store_embedding_to_faiss(docs, embeddings):
    try:
        # FAISS 인덱스 생성
        db = await FAISS.afrom_documents(docs, embeddings)
        db.save_local(DB_INDEX)
        print("FAISS 인덱스가 성공적으로 저장되었습니다.")
    except(Exception) as e:
        raise Exception(f"{store_embedding_to_faiss.__name__} function raise exception about : {str(e)}")


async def get_vector_store_local_db(embeddings):
    try:
        return FAISS.load_local(DB_INDEX, embeddings, allow_dangerous_deserialization=True)
    except(Exception) as e:
        raise Exception(f"{get_vector_store_local_db.__name__} function raise exception about : {str(e)}")