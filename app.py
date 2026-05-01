from flask import Flask, jsonify, request
import psycopg2
import os
import time

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/health")
def health():
    return {"status":"ok"}, 200

app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users;")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {"id": u[0], "name": u[1]} for u in users
    ])

def init_db():
    for _ in range(10):
        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            );
            """)

            conn.commit()
            cur.close()
            conn.close()
            print("DB initialized")
            return
        except Exception as e:
            print("Waiting for DB...", e)
            time.sleep(2)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    return conn


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (name,))
    user_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": user_id, "name": name})


@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users;")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {"id": u[0], "name": u[1]} for u in users
    ])


@app.route("/")
def hello():
    return {"message": "Version 3"} 
def home():
    return jsonify({
        "message": "Hello from Flask via Gunicorn _ Nginx🚀"
    })

@app.route("/db")
def db_test():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()

        return jsonify({
            "database": "connected",
            "version": version[0]
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        })


    init_db()
    

