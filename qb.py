import csv
import sqlite3

class Qb:
    dbpath = ""
    tablename = "qb"

    def __init__(self,**kwargs):
        self.pk=kwargs.get("pk")
        self.subject_id=kwargs.get("subject_id")
        #subject is redundant
        self.topic = kwargs.get("topic")
        self.question_no = kwargs.get("question_no")
        self.question_name = kwargs.get("question_name")
        self.answer_a = kwargs.get("answer_a")
        self.answer_b = kwargs.get("answer_b")
        self.answer_c = kwargs.get("answer_c")
        self.answer_d = kwargs.get("answer_d")
        self.answer_e = kwargs.get("answer_e")
        self.true_answer_1 = kwargs.get("True_Answer_1")
        self.true_answer_2 = kwargs.get("True_Answer_2")

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO {} (subject_id, Topic, question_no, question_name, answer_a, answer_b, answer_c, 
                    answer_d, answer_e, true_answer_1, true_answer_2)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?);""".format(self.tablename)
            values = (self.subject_id, self.topic, self.question_no, self.question_name, self.answer_a, self.answer_b, 
                    self.answer_c, self.answer_d, self.answer_e, self.true_answer_1, self.true_answer_2)
            cursor.execute(sql, values)

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """UPDATE {} SET subject_id=?, topic=?, question_no=?, question_name=?, answer_a=?, 
                    answer_b=?, answer_c=?, answer_d=?, answer_e=?, true_answer_1=?, true_answer_2=?
                    WHERE pk=?;""".format(self.tablename)
            values = (self.subject_id, self.topic, self.question_no, self.question_name, self.answer_a, self.answer_b, 
                    self.answer_c, self.answer_d, self.Answer_e, self.true_answer_1, self.true_answer_2)
            cursor.execute(sql, values)

    @classmethod
    def questions_for_subject(cls, subject, limit=None):
        with sqlite3.connect(cls.dbpath) as connection:
            # connection.row_factory = sqlite3.Row # makes our code behave like a dict
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE subject_id=?"""
            if limit:
                sql += f" LIMIT {limit}"
            cursor.execute(sql, (subject,))
            questions = cursor.fetchall()
            return questions
            # return [cls(**question) for question in questions]

    @classmethod
    def all_questions(cls, limit=None):
        with sqlite3.connect(cls.dbpath) as conn:
            # conn.row_factory = sqlite3.Row # makes our code behave like a dict
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename}"""
            if limit:
                sql += f" LIMIT {limit}"
            cursor.execute(sql)
            questions = cursor.fetchall()
            return questions
            # return [cls(**question) for question in questions]



    
# if __name__=="__main__":
#     dump_qb('questionbank.csv')



