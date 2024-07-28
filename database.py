from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = DB_URI = 'mysql+pymysql://root:Jeffry#123@localhost/medically'

engine = create_engine(SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()