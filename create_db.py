import psycopg2
import os

def create_db_and_table():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME', 'your_database'),
            user=os.getenv('DB_USER', 'your_user'),
            password=os.getenv('DB_PASS', 'your_password'),
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '12312') 
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dummy_data (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                city VARCHAR(100)
            );
        ''')

        cursor.execute("SELECT COUNT(*) FROM dummy_data")
        if cursor.fetchone()[0] == 0:
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
