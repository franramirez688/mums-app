'''
    Create a SQLite DB with the final schema and some initial static data
'''

import sqlite3
import os


def create_data_base():
    """Create DB and apply migrations"""
    if os.path.exists('sqlite3.db'):
        os.remove('sqlite3.db')

    # Create the basedata and apply migrations


def save_static_data():
    """Save some valid static data"""
    # Save some static valid data
    conn = sqlite3.connect('sqlite3.db')

    c = conn.cursor()

    with open('static_data.sql', 'r') as f:
        all_sql_commands = f.readlines()

        for sql_command in all_sql_commands:
            # Insert a row of data
            c.execute(sql_command)

    # Save (commit) the changes
    conn.commit()

    # We can also fetclose the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def main():
    create_data_base()
    save_static_data()


if __name__ == '__main__':
    main()
