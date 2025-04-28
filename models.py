from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class User(db.Model):
    srn = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    answers = db.relationship('Answer', backref='user', lazy=True)

class Answer(db.Model):
    user_srn = db.Column(db.String(20), db.ForeignKey('user.srn'), primary_key=True)
    answer1 = db.Column(db.Text, nullable=False)
    answer2 = db.Column(db.Text, nullable=False)
    answer3 = db.Column(db.Text, nullable=False)
    answer4 = db.Column(db.Text, nullable=False)
    answer5 = db.Column(db.Text, nullable=False)
    answer6 = db.Column(db.Text, nullable=False)
    answer7 = db.Column(db.Text, nullable=False)

    __table_args__ = (
        UniqueConstraint('answer1', name='uq_answer1'),
        UniqueConstraint('answer2', name='uq_answer2'),
        UniqueConstraint('answer3', name='uq_answer3'),
        UniqueConstraint('answer4', name='uq_answer4'),
        UniqueConstraint('answer5', name='uq_answer5'),
        UniqueConstraint('answer6', name='uq_answer6'),
        UniqueConstraint('answer7', name='uq_answer7'),
    )



















# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import UniqueConstraint

# db = SQLAlchemy()

# class User(db.Model):
#     srn = db.Column(db.String(20),primary_key=True)  # SRN as primary key
#     name = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     answers = db.relationship('Answer', backref='author', lazy=True)

#     def __repr__(self):
#         return f'<User {self.srn}>'

# class Answer(db.Model):
#     user_srn = db.Column(db.String(20), db.ForeignKey('user.srn'), primary_key=True)
#     answer1 = db.Column(db.Text, nullable=False, unique=True)
#     answer2 = db.Column(db.Text, nullable=False, unique=True)
#     answer3 = db.Column(db.Text, nullable=False, unique=True)
#     answer4 = db.Column(db.Text, nullable=False, unique=True)
#     answer5 = db.Column(db.Text, nullable=False, unique=True)
#     answer6 = db.Column(db.Text, nullable=False, unique=True)
#     answer7 = db.Column(db.Text, nullable=False, unique=True)

#     def __repr__(self):
#         return f'<Answer of User {self.user_srn}>'


# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import UniqueConstraint

# db = SQLAlchemy()

# class User(db.Model):
#     srn = db.Column(db.String(20), primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     answers = db.relationship('Answer', backref='author', lazy=True)

#     def __repr__(self):
#         return f''

# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # Add an ID as primary key
#     user_srn = db.Column(db.String(20), db.ForeignKey('user.srn'), nullable=False)
#     answer1 = db.Column(db.Text, nullable=False)
#     answer2 = db.Column(db.Text, nullable=False)
#     answer3 = db.Column(db.Text, nullable=False)
#     answer4 = db.Column(db.Text, nullable=False)
#     answer5 = db.Column(db.Text, nullable=False)
#     answer6 = db.Column(db.Text, nullable=False)
#     answer7 = db.Column(db.Text, nullable=False)

#     __table_args__ = (UniqueConstraint('user_srn', 'answer1', name='uq_user_answer1'),
#                        UniqueConstraint('user_srn', 'answer2', name='uq_user_answer2'),
#                        UniqueConstraint('user_srn', 'answer3', name='uq_user_answer3'),
#                        UniqueConstraint('user_srn', 'answer4', name='uq_user_answer4'),
#                        UniqueConstraint('user_srn', 'answer5', name='uq_user_answer5'),
#                        UniqueConstraint('user_srn', 'answer6', name='uq_user_answer6'),
#                        UniqueConstraint('user_srn', 'answer7', name='uq_user_answer7'))

#     def __repr__(self):
#         return f''
