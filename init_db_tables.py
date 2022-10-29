import sqlite3

telegram_logins_table = """
CREATE TABLE telegram_login(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    logo TEXT,
    name VARCHAR(191),
    login VARCHAR(191),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    );
"""

categories = """
CREATE TABLE telegram_login(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    parent_id INT,
    description VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    alias VARCHAR(255),
    type VARCHAR(255),
    meta_title VARCHAR(255),
    meta_description VARCHAR(255),
    );
"""

news = """
CREATE TABLE telegram_login(
    id INTEGER PRIMARY KEY AUTOINCREMENT,,
    logo TEXT,
    name VARCHAR(191),
    login VARCHAR(191),
    created_at TIMESTAMP,
    
    updated_at TIMESTAMP,
    
    );
"""

try:
    con = sqlite3.connect("laba.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    con.commit()
except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")


if __name__ == '__main__':
    pass