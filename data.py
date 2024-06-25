from sqlalchemy import create_engine, text

db_connection_string = "mysql+mysqldb://2MarNVgMbkgBoNS.root:RnQDXvM0Zs4GT2DS@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl_mode=VERIFY_IDENTITY&ssl_ca=/etc/ssl/certs/ca-certificates.crt"

engine = create_engine(db_connection_string)
# We are connecting this page with the another one.


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs
