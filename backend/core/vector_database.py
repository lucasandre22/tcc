import os
from rag.database.docs_rag_database import DocumentRagDatabase

print("Loading documents database...")
DOCUMENT_RAG_DATABASE = DocumentRagDatabase(os.getenv("DOCUMENT_DATABASE_PATH"))
DOCUMENT_RAG_DATABASE.load_db()
print("Documents database loaded")