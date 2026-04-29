import sqlite3

conn = sqlite3.connect("crm.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name TEXT,
    date TEXT,
    notes TEXT
)
""")
conn.commit()

def save_interaction(name, date, notes):
    cursor.execute(
        "INSERT INTO interactions (doctor_name, date, notes) VALUES (?, ?, ?)",
        (name, date, notes)
    )
    conn.commit()

def get_all_interactions():
    cursor.execute("SELECT * FROM interactions")
    return cursor.fetchall()

def update_interaction(id, name, date, notes):
    cursor.execute(
        "UPDATE interactions SET doctor_name=?, date=?, notes=? WHERE id=?",
        (name, date, notes, id)
    )
    conn.commit()