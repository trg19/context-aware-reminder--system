import sqlite3
import os

def initialize():
    # Path to the database file
    db_path = 'reminders.db'
    
    # Connect to (and create) the database file
    connection = sqlite3.connect(db_path)
    
    with open('schema.sql') as f:
        connection.executescript(f.read())
    
    connection.commit()
    connection.close()
    print("Database initialized successfully! File 'reminders.db' created.")

if __name__ == '__main__':
    initialize()