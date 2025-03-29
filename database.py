from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://root:EUanKNIMYbwiDVopYvxwwUpzgaRtRIgP@crossover.proxy.rlwy.net:29681/railway"
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    JOBS = []
    for row in result.all():
        JOBS.append(dict(row._mapping))
    return JOBS
    
    