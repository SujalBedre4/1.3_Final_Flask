from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_FLASK_STRING']

engine = create_engine(db_connection_string)
# We are connecting this page with the another one.


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs
