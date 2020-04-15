import sqlite3


class Subject:
    dbpath = ""
    tablename = "Subjects"

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.name = kwargs.get("name")
        self.image_path = kwargs.get("image_path")
        # self.quantity = kwargs.get("quantity")
        self.price = kwargs.get("price")
        # self.seller_pk = kwargs.get("seller_pk")

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO {} (name, image_path, 
                     price) VALUES (?,?,?)
                     ;""".format(self.tablename)
            values = (self.name,self.image_path,
                      self.price)
            cursor.execute(sql, values)

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """UPDATE {} SET name=?, image_path=?,
                    price=? WHERE pk=?
                     ;""".format(self.tablename)
            values = (self.name,self.image_path,
                      self.price), self.pk
            cursor.execute(sql, values)
    
    @classmethod
    def view_subjects(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            # conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            sql = """SELECT * FROM {} WHERE price > 0;"""
            cursor.execute(sql.format(cls.tablename))
            subjects = cursor.fetchall()
            return subjects
            # return [cls(**subject) for subject in subjects]
            

