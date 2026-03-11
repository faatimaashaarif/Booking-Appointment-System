from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_FILE = "bookings.db"

# ----- Database Setup ----- #
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            email TEXT NOT NULL,
            resource TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            status TEXT DEFAULT 'Confirmed'
        )
    ''')
    conn.commit()
    conn.close()

# ----- Helper Functions ----- #
def add_booking(user_name, email, resource, date, time):
    if is_conflict(resource, date, time):
        return False
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bookings (user_name, email, resource, date, time)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_name, email, resource, date, time))
    conn.commit()
    conn.close()
    return True

def is_conflict(resource, date, time):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM bookings WHERE resource=? AND date=? AND time=?
    ''', (resource, date, time))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def get_all_bookings():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings ORDER BY date, time")
    rows = cursor.fetchall()
    conn.close()
    bookings = []
    for row in rows:
        bookings.append({
            "id": row[0],
            "user_name": row[1],
            "email": row[2],
            "resource": row[3],
            "date": row[4],
            "time": row[5],
            "status": row[6]
        })
    return bookings

# ----- Routes ----- #
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    user_name = request.form['user_name']
    email = request.form['email']
    resource = request.form['resource']
    date = request.form['date']
    time = request.form['time']
    success = add_booking(user_name, email, resource, date, time)
    return render_template('index.html', message="Booking successful!" if success else "Time slot already booked!")

@app.route('/admin')
def admin():
    bookings = get_all_bookings()
    return render_template('admin.html', bookings=bookings)

@app.route('/export_json')
def export_json():
    bookings = get_all_bookings()
    return jsonify(bookings)

# ----- Main ----- #
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
