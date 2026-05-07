import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

class SnowflakeManager:
    def __init__(self):
        self.conn = snowflake.connector.connect(
            user=os.getenv('SNOW_USER'),
            password=os.getenv('SNOW_PASS'),
            account=os.getenv('SNOW_ACCT'),
            warehouse=os.getenv('SNOW_WH'),
            database=os.getenv('SNOW_DB'),
            schema=os.getenv('SNOW_SCHEMA')
        )

    def execute_query(self, sql):
        """Executes a query and returns results."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            return f"Error: {str(e)}"

    def get_table_schema(self, table_name):
        """Helps the AI understand what columns are available."""
        return self.execute_query(f"DESCRIBE TABLE {table_name}")

    def close(self):
        """Closes the Snowflake connection."""
        if self.conn:
            self.conn.close()
            print("🔒 Snowflake connection closed.")
if __name__ == "__main__":
    # Test the connection
    sm = SnowflakeManager()
    print("Testing Connection...")
    version = sm.execute_query("SELECT CURRENT_VERSION()")
    print(f"Connected to Snowflake! Version: {version[0][0]}")
