# import asyncio
# import sys
#
# from packages.decorators.logging_decorator import log_decorator
# from packages.decorators.processing_time import measure_func_execution_time_decorator
# from utils.pdf_reader import upload_pdf
# from utils.text_split import chunk_text
# from utils.text_to_embedding import text_to_embedding
# from utils.vector_store import get_vector_store_local_db, store_embedding_to_faiss
#
#
# @measure_func_execution_time_decorator()
# @log_decorator()
# async def store_pdf_to_faiss(file_path):
#     try:
#         #-- Spdf 업로드
#         documents = await upload_pdf(file_path)
#         #-- 청크 단위로 분할
#         docs = await chunk_text(documents)
#         embeddings = await text_to_embedding()
#         await store_embedding_to_faiss(docs=docs, embeddings=embeddings)
#     except(Exception) as e:
#         raise Exception(f"{store_pdf_to_faiss.__name__} function raise exception about : {str(e)}") from e
#
#
# async def serach_my_db_store(query):
#     try:
#         embeddings = await text_to_embedding()
#         new_db = await get_vector_store_local_db(embeddings)
#         docs = await new_db.asimilarity_search(query)
#         return docs[0]
#     except(Exception) as e:
#         raise Exception(f"{store_pdf_to_faiss.__name__} function raise exception about : {str(e)}") from e
#
# async def do_my_job(file_path , query):
#    await store_pdf_to_faiss(file_path)
#    text =  await serach_my_db_store(query)
#    print(text)
#
# if __name__ == "__main__":
#     try:
#         file_path = "../../../../../../../../Downloads/아카이브 (1)/sample_pdf.pdf"
#         asyncio.run(do_my_job(file_path, "웹(web)이란 무엇인가요?"))
#     except Exception as e:
#         print(f"Main caught exception: {str(e)}")
#         sys.exit(1)
#
