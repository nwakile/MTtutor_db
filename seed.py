import sqlite3
import csv
import os

DIR = os.path.dirname(__file__)
DATAPATH = os.path.join(DIR, "questionbank.csv")
DBPATH = os.path.join(DIR, "qb.db")
# print(DATAPATH)

def seed(DBPATH):
    users = [
        
        ("nwakileojike@yahoo.com", "password2", "502-718-9620", "wakil"),
        ("user2@userz.com", "password2", "555-555-5555", "user2"),
        ("user3@userz.com", "password3", "333-333-3333", "user3")   
    ]

    for user in users:
        add_user(user[0], user[1], user[2], user[3])
    
    questions =[

        ("2", "usmle3", "Gastroenterology and Hepatology", "21", "A 48-year-old woman is evaluated for shortness of breath of 6 weeks duration. She has cirrhosis due to primary biliary cholangitis. On physical examination, vital signs are normal. Spider nevi are present on the skin. The cardiopulmonary examination is normal. There is no edema. When the patient is supine, oxygen saturation  is 98 percent breathing ambient air, but oxygen saturation  drops to 92% with standing.A radiograph of the chest is normal. Which of the following is the most appropriate diagnostic test?", 
        "Bronchoscopy", "CT Angiography", "Echocardiography with agitated saline", "Pulmonary function testing",
        "DLCO testing", "C", ""	),
        ("2", "usmle3", "Gastroenterology and Hepatology", "22", "A 45-year-old man is evaluated for severe lower back and hip pain related to degenerative joint disease. His pain responds to naproxen, but he was hospitalized 6 months earlier for a bleeding gastric ulcer attributed to daily naproxen use. Naproxen was stopped, and twice-daily omeprazole was initiated at that time. Three months later, the ulcer had healed completely and omeprazole was discontinued. The patient's pain did not respond to trials of acetaminophen. He did not tolerate tramadol. The patient has no other medical problems and currently takes only acetaminophen. Which of the following is the most appropriate treatment regimen?", 
        "Celecoxib", "Celecoxib and omeprazole", "Ibuprofen and misoprostol", "Naproxen and ranitidine","Tylenol", "B", ""
        )
    ]
    
    for question in questions:
        add_qb(question[0], question[1], question[2], question[3], question[4], question[5], question[6],
        question[7], question[8], question[9], question[10])  

    

    subjects = [
        ("gmat_math", "image1", 49.99),
        ("usmle", "image2", 59.99),
        ("gre", "image3", 39.99)
    ]
    for subject in subjects:
        add_subject(subject[0], subject[1], subject[2])

def add_user(email, password, phone, username):
    with sqlite3.connect("qb.db") as conn:
        cursor = conn.cursor()
        SQL = """INSERT INTO user(email, password, phone, username) VALUES(?,?,?,?)"""

        cursor.execute(SQL, (email, password, phone, username))

def add_subject(name, image_path, price):
    with sqlite3.connect("qb.db") as conn:
        cursor = conn.cursor()
        SQL = """INSERT INTO Subjects(subject, image_path, price) VALUES(?,?,?)"""

        cursor.execute(SQL, (name, image_path, price))


def dump_qb(filepath):
    with open(filepath, 'r') as input_csv:
        reader = csv.reader(input_csv)
        # next(reader)
        header = next(reader)
        current_pk = 1
        for row in reader:
            Subject_ID, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2 = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]
            add_qb(Subject_ID, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2)
            # for Section in row[0:1]:
            #     add_user(email, current_pk)

            # current_pk += 1

def add_qb(Subject_ID, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1,	True_Answer_2):
    with sqlite3.connect(DBPATH) as conn:
        cursor = conn.cursor()
        SQL = """INSERT INTO qb(Subject_ID, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2) VALUES(?,?,?,?,?,?,?,?,?,?,?)"""

        cursor.execute(SQL, (Subject_ID, Topic, Question_No, Question_Name, Answer_A, Answer_B, Answer_C, Answer_D, Answer_E, True_Answer_1, True_Answer_2))




# if __name__=="__main__":
#     seed(DBPATH)

if __name__=="__main__":
    dump_qb(DATAPATH)


