import sqlite3

import streamlit as st
import sqlite3

# Buat koneksi ke SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Buat tabel jika belum ada
cursor.execute("""



""")
conn.commit()

conn.close()
