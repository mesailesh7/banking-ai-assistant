from sqlalchemy_utils import create_database, database_exists

from app.db.session import engine
from app.models.base import Base

# Import all models
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.models.user_role import UserRole
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.audit_log import AuditLog

if not database_exists(engine.url):
    create_database(engine.url)
    print("Database created successfully")

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")
