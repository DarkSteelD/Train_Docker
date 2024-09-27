import psycopg2
import os

# Database connection parameters
DB_NAME = os.getenv('DB_NAME', 'your_database')
DB_USER = os.getenv('DB_USER', 'your_user')
DB_PASSWORD = os.getenv('DB_PASS', 'your_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'), 
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )
    return conn
def create_db_and_table():
    try:
        conn = get_db_connection()
        conn.autocommit = True
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dummy_data (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                city VARCHAR(100)
            )
        ''')

        # Insert dummy data if table is empty
        cursor.execute("SELECT COUNT(*) FROM dummy_data")
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.execute('''
                INSERT INTO dummy_data (name, age, city)
                VALUES
                ('Alice', 30, 'New York'),
                ('Bob', 25, 'Los Angeles'),
                ('Charlie', 35, 'Chicago')
            ''')

        cursor.close()
        conn.close()
        print("Database and table created, dummy data inserted successfully.")

    except Exception as error:
        print(f"Error creating database or table: {error}")

if __name__ == '__main__':
    create_db_and_table()
