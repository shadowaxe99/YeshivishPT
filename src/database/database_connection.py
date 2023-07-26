```python
import psycopg2
from psycopg2 import pool

class DatabaseConnectionPool(object):
    def __init__(self):
        self.connection_pool = self.create_pool()

    @staticmethod
    def create_pool():
        return psycopg2.pool.SimpleConnectionPool(
            1,  # minconn
            20,  # maxconn
            host="your_host",
            database="your_database",
            user="your_user",
            password="your_password"
        )

    def get_conn(self):
        return self.connection_pool.getconn()

    def put_conn(self, conn):
        self.connection_pool.putconn(conn)

    def close_all_conn(self):
        self.connection_pool.closeall()

database_connection_pool = DatabaseConnectionPool()
```