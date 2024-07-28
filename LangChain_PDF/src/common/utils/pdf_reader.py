

from langchain_community.document_loaders import PyMuPDFLoader


async def upload_pdf(file_path):
    try:
        # LangChain PyMuPDFLoader를 사용하여 문서 로드
        loader = PyMuPDFLoader(file_path)
        documents = loader.load()
        # return [page_data.page_content for page_data in data]
        return documents
    except(Exception) as e:
        raise Exception(f"{upload_pdf.__name__} function raise exception about : {str(e)}")

