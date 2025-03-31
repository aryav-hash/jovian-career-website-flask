import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ["DB_CONNECTION_STRING"]
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    JOBS = []
    for row in result.all():
        JOBS.append(dict(row._mapping))
    return JOBS
    
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
        return None
    return dict(rows[0]._mapping)
    