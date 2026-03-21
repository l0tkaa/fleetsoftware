from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# SQLite database file named fleet.db
DATABASE_URL = "sqlite:///fleet.db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create session class for DB operations
SessionLocal = sessionmaker(bind=engine)

# Base class for all models
Base = declarative_base()