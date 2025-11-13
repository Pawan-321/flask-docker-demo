from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Get database connection info from environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route('/')
def hello():
    return "Hello, Docker + PostgreSQL! 🚀"

@app.route('/db-test')
def db_test():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL! Version: {version[0]}"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

