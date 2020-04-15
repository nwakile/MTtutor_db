import sqlite3
import os

DIR = os.path.dirname(__file__)
DBNAME = "qb.db"
DBPATH = os.path.join(DIR, DBNAME)

def schema(dbpath):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        
        #Questions
        SQL = "DROP TABLE IF EXISTS qb;"

        cursor.execute(SQL)

        SQL = """CREATE TABLE qb (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id VARCHAR(6),
            subject VARCHAR(32),
            topic VARCHAR(32),
            question_no VARCHAR(6),
            Question_Name TEXT,
            answer_a TEXT,
            answer_b TEXT,
            answer_c TEXT,
            answer_d TEXT,
            answer_e TEXT,
            True_Answer_1 VARCHAR(6),
            True_Answer_2 VARCHAR(6),
            FOREIGN KEY(subject_id) REFERENCES catalogue(pk)
          

        );"""

        cursor.execute(SQL)


        #User
        SQL = "DROP TABLE IF EXISTS user;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE user (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(128),
            password VARCHAR(128),
            phone VARCHAR(64),
            username VARCHAR(128),
            auth_token VARCHAR(32)
            );"""
        cursor.execute(SQL)

        # Performance
        SQL = "DROP TABLE IF EXISTS performance;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE performance(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                qb_id INTEGER,
                user_id INTEGER,
                testdate DATETIME,
                answer_choice VARCHAR(6),
                success BOOLEAN,
                FOREIGN KEY(qb_id) REFERENCES qb(pk),
                FOREIGN KEY(user_id) REFERENCES user(pk)
                
                
        );"""
        cursor.execute(SQL)


        # Subjects
        SQL = "DROP TABLE IF EXISTS Subjects;"
        cursor.execute(SQL)

        sql = """CREATE TABLE Subjects(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            subject VARCHAR(32),
            image_path TEXT,
            price FLOAT
            
        );"""
        cursor.execute(sql)


if __name__== "__main__":
    schema(DBPATH)
