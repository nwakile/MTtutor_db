import sqlite3
from secrets import token_hex

class User:
    dbpath = ""
    tablename = "user"

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.email = kwargs.get("email")
        self.password_hash = kwargs.get("password")
        self.phone = kwargs.get("phone")
        self.username = kwargs.get("username")
        self.token = kwargs.get("auth_token")

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO {} (email, password, 
                    phone, username)
                    VALUES (?,?,?,?);""".format(self.tablename)
            values = (self.email,self.password_hash,self.phone,
                      self.username)
            cursor.execute(sql, values)

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = """UPDATE {} SET email=?, password=?, 
                    phone=?, username=?, auth_token=?
                    WHERE pk=?;""".format(self.tablename)
            values = (self.email,self.password_hash,self.phone,
                      self.username,self.pk,self.token)
            cursor.execute(sql, values)

    def set_token(self):
        self.token = token_hex(32)

    @classmethod
    def login(cls, email, password):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            sql = """SELECT * FROM {} WHERE email=? AND password=?;"""
            cursor.execute(sql.format(cls.tablename), (email, password))
            row = cursor.fetchone()
            if row:
                return cls(**row)
            else:
                return None

    @classmethod
    def token_authenticate(cls, token):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            sql = """SELECT * FROM {} WHERE auth_token=?;"""
            cursor.execute(sql.format(cls.tablename), (token,))
            row = cursor.fetchone()
            if row:
                return cls(**row)
            else:
                return None