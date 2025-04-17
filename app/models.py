from app import db



class User(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False ,unique=True)
    firstname = db.Column(db.String(50), nullable=False)  # Uncommented firstname
    lastname = db.Column(db.String(50), nullable=False)   # Uncommented lastname
    password = db.Column(db.String(100), nullable=False)
    task = db.relationship('Task', backref='user', lazy=True)
    def __repr__(self):
        return f' {self.firstname} {self.lastname}'
class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f'<Task {self.title} {self.completed}>'


   