from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://billy:root@127.0.0.1:5432/devdb"

engine = create_engine(DATABASE_URL)

# Test Connection
with engine.connect() as connection:
    result = connection.exec_driver_sql("SELECT 1").scalar()
    print(f"Connection successfull! Test query returned {result}")