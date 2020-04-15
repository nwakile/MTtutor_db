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
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO {} (qb_id, user_id,
                     testdate, answer_choice, success)
                    VALUES (?,?,?,?,?);""".format(self.tablename)
            values = (self.qb_id, self.user_id,
                      self.testdate, self.answer_choice, self.success)
            cursor.execute(sql, values)
    
    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """UPDATE {} SET qb_id=?, user_id=?,
                    testdate=?, answer_choice=?, success=? WHERE pk=?
                     ;""".format(self.tablename)
            values = (self.qb_id, self.user_id,
                      self.testdate, self.answer_choice, self.success), self.pk
            cursor.execute(sql, values)

    @classmethod
    def view_performance(cls, user_id, name):
        # success_rate = success.count('T')/qb_id.count()
        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row # makes our code behave like a dict
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} 
            JOIN qb ON performance.qb_id = qb.pk
            JOIN subject ON qb.subject_id=subject.pk
            WHERE performance.user_id=? AND subject.name=?"""

            cursor.execute(sql, (user_id, name))
            questions = cursor.fetchall()
            return questions

