import psycopg2
import time
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app, version='1.0', title='Alunos API', description='API para conexão com PostgreSQL', doc='/swagger')

ns = api.namespace('alunos', description='Alunos operations')

def get_connection():
    conn = psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

@ns.route('/')
class Alunos(Resource):
    def get(self):
        time.sleep(5)
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS alunos (id serial PRIMARY KEY, nome VARCHAR(255) NOT NULL)")
        conn.commit()

        cursor.execute("INSERT INTO alunos (nome) VALUES ('Rafael')")
        conn.commit()

        cursor.execute("INSERT INTO alunos (nome) VALUES ('Maria')")
        conn.commit()

        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        cursor.close()
        conn.close()

        return {"alunos": [{"id": aluno[0], "nome": aluno[1]} for aluno in alunos]}