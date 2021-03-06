import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_cwd = os.path.dirname(os.path.abspath(__file__))
db_path = 'sqlite:///' + os.path.join(_cwd, 'catalog.db')


# From http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
engine = create_engine(db_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    ''' Creates tables for models in db '''
    import models
    Base.metadata.create_all(bind=engine)
