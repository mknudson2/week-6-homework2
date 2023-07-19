from collection_app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30))    
    username = db.Column(db.String(80), nullable=False, unique = True)    
    email = db.Column(db.String(150), nullable=False, unique = True)
    password_hash = db.Column(db.String(), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return password== check_password_hash(self.password_hash, password)