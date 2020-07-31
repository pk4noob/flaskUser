from flask import Flask
from extensions.extensions import ma, db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    surname = db.Column(db.String(), nullable=False)
    nickname = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    # product_id = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String(), nullable=False)

    def pasword_hash(self):
        setattr(self, "password", generate_password_hash(self.password))

    def password_chech(self, password):
        return check_password_hash(self.password, password)

    def savedb(self):
        db.session.add(self)
        db.session.commit()

    def deletedb(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.savedb()
