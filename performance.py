import sqlite3


class Performance:
    dbpath = ""
    tablename = "performance"

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.qb_id = kwargs.get("qb_id")
        self.user_id = kwargs.get("user_id")
        self.testdate = kwargs.get("testdate")
        self.answer_choice = kwargs.get("answer_choice")
        self.success = kwargs.get("success")
       

    def save(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO {} (qb_id, user_id,
                     testdate, answer_choice, success)
                    VALUES (?,?,?,?,?);""".format(self.tablename)
            values = (self.qb_id, self.user_id,
                      self.testdate, self.answer_choice, self.success)
            cursor.execute(sql, values)
