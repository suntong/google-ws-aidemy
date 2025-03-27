import os
import base64
import sqlalchemy
from google.cloud.sql.connector import Connector, IPTypes
import pg8000


project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
location = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
instance_name = os.environ.get("INSTANCE_NAME") 
instance_connection_name = f"{project_id}:{location}:{instance_name}"
print(f"--------------------------->Instance connection name: {instance_connection_name}")


def connect_with_connector() -> sqlalchemy.engine.base.Engine:

    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_name = os.environ["DB_NAME"]

    print(f"--------------------------->db_user: {db_user!r}")
    print(f"--------------------------->db_pass: {db_pass!r}")
    print(f"--------------------------->db_name: {db_name!r}")

    connector = Connector()

    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=lambda: connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
        ),
        pool_size=2,
        max_overflow=2,
        pool_timeout=30,  # 30 seconds
        pool_recycle=1800,  # 30 minutes
    )
    return pool

def get_curriculum(year: int, subject: str):
    """
    Get school curriculum

    Args:
        subject: User's request subject string
        year: User's request year int
    """
    try:
        stmt = sqlalchemy.text(
            "SELECT description FROM curriculums WHERE year = :year AND subject = :subject"
        )

        with db.connect() as conn:
            result = conn.execute(stmt, parameters={"year": year, "subject": subject})
            row = result.fetchone()
        if row:
            return row[0]
        else:
            return None

    except Exception as e:
        print(e)
        return None

db = connect_with_connector()


# if __name__ == "__main__":
#     print(get_curriculum(6, "Mathematics"))
