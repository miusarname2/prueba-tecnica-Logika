from sqlalchemy import Column, Integer, String, DateTime, Enum, Index
from sqlalchemy.sql import func
import enum
from app.database.database import Base

class TaskStatus(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Índices en status y created_at para filtrado y ordenamiento eficiente
    __table_args__ = (
        Index('ix_tasks_status', 'status'),
        Index('ix_tasks_created_at', 'created_at'),
    )