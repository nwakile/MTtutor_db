import csv
import sqlite3

class Qb:
    dbpath = ""
    tablename = "qb"

def dump_qb(filepath):
    with open(filepath, 'r') as input_csv:
        reader = csv.reader(input_csv)
        # next(reader)
        header = next(reader)
        current_pk = 1
        for row in reader:
            Subject_ID, Subject, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2 = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]
            add_qb(Subject_ID, Subject, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2)
            # for Section in row[0:1]:
            #     add_user(email, current_pk)

            # current_pk += 1

def add_qb(Subject_ID, Subject, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1,	True_Answer_2):
    with sqlite3.connect("qb.db") as conn:
        cursor = conn.cursor()
        SQL = """INSERT INTO qb(Subject_ID, Subject, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"""

        cursor.execute(SQL, (Subject_ID, Subject, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2))

# def add_user(name, email, country):
#     with sqlite3.connect("user.db") as conn:
#         cursor = conn.cursor()
#         SQL = """INSERT INTO users(name, email, country) VALUES(?,?,?)"""

#         cursor.execute(SQL, (name, email, country))


if __name__=="__main__":
    dump_qb('questionbank.csv')



