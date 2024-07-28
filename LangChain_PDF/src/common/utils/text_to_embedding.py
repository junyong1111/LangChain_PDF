from langchain_openai import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer


#-- 텍스트 임베딩 모델 로드
async def text_to_embedding():
    try:
        embeddings = OpenAIEmbeddings()
        # 청크 단위 텍스트를 임베딩으로 변환
        return embeddings
    except(Exception) as e:
        raise Exception(f"{text_to_embedding.__name__} function raise exception about : {str(e)}")