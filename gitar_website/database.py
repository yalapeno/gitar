from datetime import datetime

from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

from gitar_website import app


class Base(object):
    @declared_attr
    def __tablename__(cls):
        """Table names are same as lowercase class names."""
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)  # every table has an id as primary key
    added = Column(TIMESTAMP, default=datetime.now())
    updated = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())


engine = create_engine(app.config["DATABASE_URI"], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base(cls=Base)
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


