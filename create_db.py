import psycopg2
import os

# Database connection parameters
DB_NAME = os.getenv('DB_NAME', 'your_database')
DB_USER = os.getenv('DB_USER', 'your_user')
DB_PASSWORD = os.getenv('DB_PASS', 'your_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')

def create_db_and_table():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
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
