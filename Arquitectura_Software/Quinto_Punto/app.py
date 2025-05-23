from flask import Flask, render_template, request, redirect, session
from db_config import get_connection

app = Flask(__name__)
app.secret_key = 'secretoGustambo123'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    email = request.form['email']
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre FROM estudiantes WHERE email = %s", (email,))
    user = cur.fetchone()
    conn.close()

    if user:
        session['usuario'] = user[1]
        session['id'] = user[0]
        return redirect('/notas')
    else:
        return "Usuario no encontrado"

@app.route('/notas')
def notas():
    if 'usuario' not in session:
        return redirect('/')

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT m.nombre, n.nota
        FROM notas n
        JOIN materias m ON n.materia_id = m.id
        WHERE n.estudiante_id = %s
    """, (session['id'],))
    notas = cur.fetchall()
    conn.close()

    return render_template('notas.html', nombre=session['usuario'], notas=notas)
