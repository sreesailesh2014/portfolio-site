from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT NOT NULL, roll_no TEXT UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS attendance
                 (id INTEGER PRIMARY KEY, student_id INTEGER, date TEXT, status TEXT,
                  FOREIGN KEY(student_id) REFERENCES students(id))''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    today = date.today().isoformat()
    c.execute("SELECT student_id, status FROM attendance WHERE date =?", (today,))
    marked = dict(c.fetchall())
    conn.close()
    return render_template('index.html', students=students, marked=marked, today=today)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    roll_no = request.form['roll_no']
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO students (name, roll_no) VALUES (?,?)", (name, roll_no))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()
    return redirect(url_for('index'))

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    today = date.today().isoformat()
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("DELETE FROM attendance WHERE date =?", (today,))
    for student_id, status in request.form.items():
        if student_id.startswith('status_'):
            sid = student_id.split('_')[1]
            c.execute("INSERT INTO attendance (student_id, date, status) VALUES (?,?,?)",
                      (sid, today, status))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/report')
def report():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''SELECT s.name, s.roll_no, a.date, a.status
                 FROM attendance a
                 JOIN students s ON a.student_id = s.id
                 ORDER BY a.date DESC, s.name''')
    records = c.fetchall()
    conn.close()
    return render_template('report.html', records=records)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)