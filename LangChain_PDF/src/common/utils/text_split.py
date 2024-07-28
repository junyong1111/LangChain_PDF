from langchain_text_splitters import CharacterTextSplitter


# 텍스트를 청크 단위로 나누는 함수
async def chunk_text(documents, chunk_size=512, overlap=50):
    try:
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        return text_splitter.split_documents(documents)
    except(Exception) as e:
        raise Exception(f"{chunk_text.__name__} function raise exception about : {str(e)}")

